"""斗茶赛会接口：维护斗茶赛事，覆盖发布赛事、开始评审、公布结果等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.tea_contest import TeaContestService

router = APIRouter(prefix="/api/tea_contest", tags=["斗茶赛会"])

service = TeaContestService()

LIST_FIELDS = ["赛事编号", "赛事名称", "赛事等级", "参赛茶样", "评审委员", "举办日期", "获奖结果", "赛事状态"]
STATUSES = ["待举办", "报名中", "评审中", "已揭晓"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按赛事编号检索"),
    status: str | None = Query(default=None, description="待举办、报名中、评审中、已揭晓"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按赛事编号与状态过滤斗茶赛会列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条斗茶赛事明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"斗茶赛事 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条斗茶赛事，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="斗茶赛事已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条斗茶赛事执行发布赛事、开始评审、公布结果；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出斗茶赛会清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "tea_contest", "total": total, "items": items}
