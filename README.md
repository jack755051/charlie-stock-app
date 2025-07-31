# 📈 Charlie Stock App

> 一個基於 Django + Nuxt.js 的現代化股票分析應用程式

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Node.js](https://img.shields.io/badge/node.js-18-green.svg)
![Django](https://img.shields.io/badge/django-5.2.4-darkgreen.svg)
![Nuxt.js](https://img.shields.io/badge/nuxt.js-4.0.1-00C58E.svg)

## 🎯 專案簡介

Charlie Stock App 是一個全棧的股票分析應用程式，提供即時股票數據追蹤、技術分析圖表、投資組合管理等功能。

### ✨ 主要功能

- 📊 **即時股票數據** - 即時價格、成交量等關鍵指標
- 📈 **技術分析** - K線圖、移動平均線、技術指標
- 💼 **投資組合管理** - 追蹤個人投資表現
- �� **股票搜尋** - 快速搜尋和篩選股票
- 📱 **響應式設計** - 支援桌面和行動裝置
- 🔐 **用戶認證** - 安全的用戶註冊和登入

## 🏗️ 技術架構

### 後端 (Django)
- **Framework**: Django 5.2.4 + Django REST Framework
- **資料庫**: PostgreSQL 15
- **快取**: Redis 7
- **認證**: JWT + Django Allauth
- **API 文件**: DRF Spectacular (Swagger/OpenAPI)
- **數據處理**: Pandas + NumPy

### 前端 (Nuxt.js)
- **Framework**: Nuxt.js 4.0.1 (Vue 3)
- **UI 框架**: Nuxt UI
- **語言**: TypeScript
- **構建工具**: Vite
- **狀態管理**: Pinia (內建)

### DevOps
- **容器化**: Docker + Docker Compose
- **開發工具**: ESLint, TypeScript
- **版本控制**: Git

## 🚀 快速開始

### 前置需求

- [Docker](https://www.docker.com/get-started) 20.10+
- [Docker Compose](https://docs.docker.com/compose/install/) 2.0+
- [Make](https://www.gnu.org/software/make/) (可選，用於簡化指令)

### 一鍵啟動

1. **克隆專案**
   ```bash
   git clone https://github.com/jack755051/charlie-stock-app.git
   cd charlie-stock-app
   ```

2. **初始化專案**
   ```bash
   make init
   ```
   
   或手動執行：
   ```bash
   # 複製環境變數檔案
   cp stock-backend/.env.example stock-backend/.env
   
   # 建置並啟動服務
   docker-compose up -d
   
   # 執行資料庫遷移
   docker-compose exec backend python manage.py migrate
   
   # 創建超級用戶 (可選)
   docker-compose exec backend python manage.py createsuperuser
   ```

3. **訪問應用**
   - 🌐 **前端應用**: http://localhost:3000
   - 🔧 **後端 API**: http://localhost:8000
   - 📊 **管理後台**: http://localhost:8000/admin
   - 📚 **API 文件**: http://localhost:8000/api/schema/swagger-ui/

## 🛠️ 開發指令

### 基本操作
```bash
# 啟動所有服務
make up

# 停止所有服務
make down

# 重啟服務
make restart

# 查看服務狀態
make status

# 查看日誌
make logs
```

### 資料庫操作
```bash
# 執行遷移
make migrate

# 創建遷移文件
make backend-makemigrations

# 創建超級用戶
make createsuperuser
```

### 開發工具
```bash
# 進入後端 shell
make shell

# 執行測試
make test

# 清理 Docker 資源
make clean
```

## 📁 專案結構

```
charlie-stock-app/
├── 📁 stock-backend/           # Django 後端
│   ├── 📄 Dockerfile           # 後端容器配置
│   ├── 📄 requirements.txt     # Python 依賴
│   ├── 📄 .env.example         # 環境變數範例
│   ├── 📄 manage.py            # Django 管理工具
│   └── 📁 backend/             # Django 主應用
│       ├── 📄 settings.py      # Django 設定
│       ├── 📄 urls.py          # URL 路由
│       └── 📄 wsgi.py          # WSGI 入口
├── 📁 stock-frontend/          # Nuxt.js 前端
│   ├── 📄 Dockerfile           # 前端容器配置
│   ├── 📄 package.json         # Node.js 依賴
│   ├── 📄 nuxt.config.ts       # Nuxt 配置
│   ├── 📁 app/                 # 應用主目錄
│   │   └── 📄 app.vue          # 根組件
│   └── 📁 public/              # 靜態資源
├── 📄 docker-compose.yml       # Docker 服務編排
├── 📄 Makefile                 # 開發指令集
├── 📄 .gitignore              # Git 忽略文件
└── 📄 README.md               # 專案說明文件
```

## 🔧 環境配置

### 後端環境變數 (.env)

```bash
# Django 設定
DEBUG=1
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# 資料庫設定
DATABASE_URL=postgresql://stock_user:stock_password@db:5432/stock_app_db

# Redis 設定
REDIS_URL=redis://redis:6379/0

# CORS 設定
CORS_ALLOWED_ORIGINS=http://localhost:3000

# 股票 API 設定
STOCK_API_KEY=your-stock-api-key
STOCK_API_URL=https://api.example.com/v1/
```

### 前端環境變數

前端環境變數透過 `nuxt.config.ts` 配置，主要包括：
- `NUXT_PUBLIC_API_BASE_URL`: 後端 API 基礎 URL

## 🐳 Docker 服務

| 服務名稱 | 端口 | 說明 |
|---------|------|------|
| `frontend` | 3000 | Nuxt.js 前端應用 |
| `backend` | 8000 | Django 後端 API |
| `db` | 5432 | PostgreSQL 資料庫 |
| `redis` | 6379 | Redis 快取服務 |

## 🧪 測試

### 後端測試
```bash
# 執行所有測試
docker-compose exec backend python manage.py test

# 執行特定應用測試
docker-compose exec backend python manage.py test stocks

# 產生測試覆蓋率報告
docker-compose exec backend coverage run --source='.' manage.py test
docker-compose exec backend coverage html
```

### 前端測試
```bash
# 執行單元測試
docker-compose exec frontend npm run test

# 執行 E2E 測試
docker-compose exec frontend npm run test:e2e
```

## 📚 API 文件

應用啟動後，可透過以下方式訪問 API 文件：

- **Swagger UI**: http://localhost:8000/api/schema/swagger-ui/
- **ReDoc**: http://localhost:8000/api/schema/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/

## 🔒 安全考量

- 使用 JWT 進行 API 認證
- CORS 設定限制前端訪問
- Docker 容器使用非 root 用戶
- 敏感資訊透過環境變數管理
- 生產環境需要設定 `DEBUG=False`

## 🚀 部署

### 生產環境部署

1. **設定生產環境變數**
   ```bash
   DEBUG=0
   SECRET_KEY=your-production-secret-key
   ALLOWED_HOSTS=yourdomain.com
   DATABASE_URL=your-production-database-url
   ```

2. **使用生產配置**
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
   ```

3. **收集靜態文件**
   ```bash
   make collectstatic
   ```

## 🤝 貢獻指南

1. Fork 此專案
2. 創建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

## 📝 授權條款

此專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 文件

## 📞 聯絡資訊

- **開發者**: Charlie
- **GitHub**: [@jack755051](https://github.com/jack755051)
- **專案連結**: [https://github.com/jack755051/charlie-stock-app](https://github.com/jack755051/charlie-stock-app)

## 🙏 致謝

感謝所有為此專案貢獻的開發者和開源社群。

---

⭐ 如果這個專案對你有幫助，請給它一個星星！
