# 茶道修习传承管理平台

面向中华茶道修习的茶样鉴藏、茶席布置、点茶研习、茶具养护与雅集筹办的一体化传承管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 茶样鉴藏 | `tea_leaf` | 茶样 | 茶样编号、茶样名称、茶叶品类 |
| 茶人档案 | `tea_master` | 茶道师 | 茶人编号、姓名、师承流派 |
| 门生修习 | `disciple` | 门生 | 门生编号、姓名、师从茶人 |
| 茶具养护 | `tea_set` | 茶具 | 茶具编号、茶具名称、器型类别 |
| 茶席布置 | `tea_mat` | 茶席 | 茶席编号、茶席主题、主泡茶具 |
| 点茶研习 | `dian_cha` | 点茶记录 | 记录编号、研习茶样、研习日期 |
| 用水品鉴 | `tea_water` | 用水记录 | 记录编号、水源名称、水源类型 |
| 香道搭配 | `tea_incense` | 香品 | 香品编号、香品名称、香品类别 |
| 茶会雅集 | `tea_ceremony` | 茶会 | 茶会编号、茶会主题、主持茶人 |
| 茶诗茶画 | `tea_poetry` | 文艺作品 | 作品编号、作品名称、作品类别 |
| 茶书典籍 | `tea_book` | 茶学典籍 | 典籍编号、典籍名称、作者朝代 |
| 茶区探访 | `tea_region` | 茶区记录 | 记录编号、茶区名称、所在省份 |
| 制茶工坊 | `tea_workshop` | 制茶批次 | 批次编号、鲜叶来源、制茶品类 |
| 斗茶赛会 | `tea_contest` | 斗茶赛事 | 赛事编号、赛事名称、赛事等级 |
| 茶礼往来 | `tea_exchange` | 往来记录 | 记录编号、往来对象、茶礼内容 |
| 影像记录 | `tea_media` | 茶事影像 | 影像编号、拍摄主题、拍摄日期 |
| 传承基金 | `tea_fund` | 基金项目 | 项目编号、资助方向、资助金额 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
