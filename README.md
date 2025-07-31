# Charlie Stock App

這是一個全端應用程式專案，結合了 Nuxt.js（前端）與 Django（後端），用於顯示與管理股票相關資訊。

---

## 📁 專案結構

charlie-stock-app/
├── stock-frontend/        # Nuxt.js 專案
├── stock-backend/         # Django 專案
├── docker-compose.yml     # Docker 組態
├── .gitignore
└── README.md

---

## 🐳 使用 Docker 開發

### 一鍵啟動

```bash
docker-compose up --build

前端預設位置
-   Nuxt app: http://localhost:3000

後端預設位置
-   Django app: http://localhost:8000

---

## 🛠️ 環境建置

### 前端（Nuxt 3）

```bash
cd stock-frontend
npm install      # 或 yarn install
npm run dev      # 開發模式運行