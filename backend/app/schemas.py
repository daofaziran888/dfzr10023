"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class TeaLeafEntry(BaseModel):
    """茶样明细结构。"""

    field_0: str | None = None  # 茶样编号
    field_1: str | None = None  # 茶样名称
    field_2: str | None = None  # 茶叶品类
    field_3: str | None = None  # 产地来源
    field_4: str | None = None  # 采摘年份
    field_5: str | None = None  # 制作工艺
    field_6: str | None = None  # 冲泡参数
    field_7: str | None = None  # 鉴藏状态

class TeaMasterEntry(BaseModel):
    """茶道师明细结构。"""

    field_0: str | None = None  # 茶人编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 师承流派
    field_3: str | None = None  # 修习年限
    field_4: str | None = None  # 擅长茶类
    field_5: str | None = None  # 授业资质
    field_6: str | None = None  # 联系方式
    field_7: str | None = None  # 在册状态

class DiscipleEntry(BaseModel):
    """门生明细结构。"""

    field_0: str | None = None  # 门生编号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 师从茶人
    field_3: str | None = None  # 入门日期
    field_4: str | None = None  # 修习阶段
    field_5: str | None = None  # 考核成绩
    field_6: str | None = None  # 出师日期
    field_7: str | None = None  # 门生状态

class TeaSetEntry(BaseModel):
    """茶具明细结构。"""

    field_0: str | None = None  # 茶具编号
    field_1: str | None = None  # 茶具名称
    field_2: str | None = None  # 器型类别
    field_3: str | None = None  # 材质工艺
    field_4: str | None = None  # 制器匠人
    field_5: str | None = None  # 入藏日期
    field_6: str | None = None  # 养护周期
    field_7: str | None = None  # 茶具状态

class TeaMatEntry(BaseModel):
    """茶席明细结构。"""

    field_0: str | None = None  # 茶席编号
    field_1: str | None = None  # 茶席主题
    field_2: str | None = None  # 主泡茶具
    field_3: str | None = None  # 辅助器物
    field_4: str | None = None  # 插花搭配
    field_5: str | None = None  # 香道搭配
    field_6: str | None = None  # 布置人员
    field_7: str | None = None  # 茶席状态

class DianChaEntry(BaseModel):
    """点茶记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 研习茶样
    field_2: str | None = None  # 研习日期
    field_3: str | None = None  # 水温控制
    field_4: str | None = None  # 击拂手法
    field_5: str | None = None  # 沫饽品质
    field_6: str | None = None  # 指导茶人
    field_7: str | None = None  # 研习状态

class TeaWaterEntry(BaseModel):
    """用水记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 水源名称
    field_2: str | None = None  # 水源类型
    field_3: str | None = None  # 取水日期
    field_4: str | None = None  # 水质等级
    field_5: str | None = None  # 适用茶类
    field_6: str | None = None  # 品鉴人员
    field_7: str | None = None  # 品鉴状态

class TeaIncenseEntry(BaseModel):
    """香品明细结构。"""

    field_0: str | None = None  # 香品编号
    field_1: str | None = None  # 香品名称
    field_2: str | None = None  # 香品类别
    field_3: str | None = None  # 原料配方
    field_4: str | None = None  # 制香匠人
    field_5: str | None = None  # 适用茶席
    field_6: str | None = None  # 燃香时长
    field_7: str | None = None  # 香品状态

class TeaCeremonyEntry(BaseModel):
    """茶会明细结构。"""

    field_0: str | None = None  # 茶会编号
    field_1: str | None = None  # 茶会主题
    field_2: str | None = None  # 主持茶人
    field_3: str | None = None  # 举办地点
    field_4: str | None = None  # 开始日期
    field_5: str | None = None  # 参与人数
    field_6: str | None = None  # 所用茶样
    field_7: str | None = None  # 茶会状态

class TeaPoetryEntry(BaseModel):
    """文艺作品明细结构。"""

    field_0: str | None = None  # 作品编号
    field_1: str | None = None  # 作品名称
    field_2: str | None = None  # 作品类别
    field_3: str | None = None  # 创作人
    field_4: str | None = None  # 创作日期
    field_5: str | None = None  # 所用茶样
    field_6: str | None = None  # 作品内容
    field_7: str | None = None  # 作品状态

class TeaBookEntry(BaseModel):
    """茶学典籍明细结构。"""

    field_0: str | None = None  # 典籍编号
    field_1: str | None = None  # 典籍名称
    field_2: str | None = None  # 作者朝代
    field_3: str | None = None  # 版本类型
    field_4: str | None = None  # 典藏地点
    field_5: str | None = None  # 录入日期
    field_6: str | None = None  # 校勘人员
    field_7: str | None = None  # 典籍状态

class TeaRegionEntry(BaseModel):
    """茶区记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 茶区名称
    field_2: str | None = None  # 所在省份
    field_3: str | None = None  # 主要茶类
    field_4: str | None = None  # 探访日期
    field_5: str | None = None  # 探访人员
    field_6: str | None = None  # 风土记录
    field_7: str | None = None  # 探访状态

class TeaWorkshopEntry(BaseModel):
    """制茶批次明细结构。"""

    field_0: str | None = None  # 批次编号
    field_1: str | None = None  # 鲜叶来源
    field_2: str | None = None  # 制茶品类
    field_3: str | None = None  # 制茶师傅
    field_4: str | None = None  # 开始日期
    field_5: str | None = None  # 完成日期
    field_6: str | None = None  # 成品数量
    field_7: str | None = None  # 批次状态

class TeaContestEntry(BaseModel):
    """斗茶赛事明细结构。"""

    field_0: str | None = None  # 赛事编号
    field_1: str | None = None  # 赛事名称
    field_2: str | None = None  # 赛事等级
    field_3: str | None = None  # 参赛茶样
    field_4: str | None = None  # 评审委员
    field_5: str | None = None  # 举办日期
    field_6: str | None = None  # 获奖结果
    field_7: str | None = None  # 赛事状态

class TeaExchangeEntry(BaseModel):
    """往来记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 往来对象
    field_2: str | None = None  # 茶礼内容
    field_3: str | None = None  # 往来方向
    field_4: str | None = None  # 往来日期
    field_5: str | None = None  # 经手人员
    field_6: str | None = None  # 回礼记录
    field_7: str | None = None  # 往来状态

class TeaMediaEntry(BaseModel):
    """茶事影像明细结构。"""

    field_0: str | None = None  # 影像编号
    field_1: str | None = None  # 拍摄主题
    field_2: str | None = None  # 拍摄日期
    field_3: str | None = None  # 拍摄地点
    field_4: str | None = None  # 影像类型
    field_5: str | None = None  # 拍摄人员
    field_6: str | None = None  # 存储位置
    field_7: str | None = None  # 影像状态

class TeaFundEntry(BaseModel):
    """基金项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 资助方向
    field_2: str | None = None  # 资助金额
    field_3: str | None = None  # 申请人
    field_4: str | None = None  # 审批人
    field_5: str | None = None  # 资助周期
    field_6: str | None = None  # 成果汇报
    field_7: str | None = None  # 项目状态
