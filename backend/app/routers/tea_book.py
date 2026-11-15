"""茶书典籍接口：维护茶学典籍，覆盖开始校勘、完成校勘、确认刊行等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query, Request

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.tea_book import TeaBookService

router = APIRouter(prefix="/api/tea_book", tags=["茶书典籍"])

service = TeaBookService()

LIST_FIELDS = ["典籍编号", "典籍名称", "作者朝代", "版本类型", "典藏地点", "录入日期", "校勘人员", "典籍状态"]
STATUSES = ["待校勘", "校勘中", "已校勘", "已刊行"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    request: Request,
    keyword: str | None = Query(default=None, description="按典籍编号检索"),
    status: str | None = Query(default=None, description="待校勘、校勘中、已校勘、已刊行"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按典籍编号与状态过滤茶书典籍列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    extra = {k: v for k, v in request.query_params.items() if k not in ("keyword", "status", "page", "size") and v.strip()}
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size, extra=extra)
    return PageResult(items=items, total=total, page=page, size=size)



@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出茶书典籍清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "tea_book", "total": total, "items": items}


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条茶学典籍明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"茶学典籍 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条茶学典籍，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="茶学典籍已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条茶学典籍执行开始校勘、完成校勘、确认刊行；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)
