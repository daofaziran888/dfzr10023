"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import tea_leaf as router_tea_leaf
from app.routers import tea_master as router_tea_master
from app.routers import disciple as router_disciple
from app.routers import tea_set as router_tea_set
from app.routers import tea_mat as router_tea_mat
from app.routers import dian_cha as router_dian_cha
from app.routers import tea_water as router_tea_water
from app.routers import tea_incense as router_tea_incense
from app.routers import tea_ceremony as router_tea_ceremony
from app.routers import tea_poetry as router_tea_poetry
from app.routers import tea_book as router_tea_book
from app.routers import tea_region as router_tea_region
from app.routers import tea_workshop as router_tea_workshop
from app.routers import tea_contest as router_tea_contest
from app.routers import tea_exchange as router_tea_exchange
from app.routers import tea_media as router_tea_media
from app.routers import tea_fund as router_tea_fund

ROUTERS = [router_tea_leaf, router_tea_master, router_disciple, router_tea_set, router_tea_mat, router_dian_cha, router_tea_water, router_tea_incense, router_tea_ceremony, router_tea_poetry, router_tea_book, router_tea_region, router_tea_workshop, router_tea_contest, router_tea_exchange, router_tea_media, router_tea_fund]
