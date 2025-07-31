# Charlie Stock App - 開發輔助指令

.PHONY: help build up down logs clean restart migrate shell test

# 顯示幫助信息
help:
	@echo "Charlie Stock App - 可用指令:"
	@echo "  build     - 建置所有容器"
	@echo "  up        - 啟動所有服務"
	@echo "  down      - 停止所有服務"
	@echo "  logs      - 查看服務日誌"
	@echo "  clean     - 清理未使用的容器和映像"
	@echo "  restart   - 重啟所有服務"
	@echo "  migrate   - 執行資料庫遷移"
	@echo "  shell     - 進入後端容器的 shell"
	@echo "  test      - 執行測試"
	@echo "  init      - 初次設置專案"

# 建置所有容器
build:
	docker-compose build --no-cache

# 啟動所有服務
up:
	docker-compose up -d

# 停止所有服務
down:
	docker-compose down

# 查看服務日誌
logs:
	docker-compose logs -f

# 清理未使用的容器和映像
clean:
	docker system prune -f
	docker volume prune -f

# 重啟所有服務
restart: down up

# 執行資料庫遷移
migrate:
	docker-compose exec backend python manage.py migrate

# 進入後端容器的 shell
shell:
	docker-compose exec backend python manage.py shell

# 執行測試
test:
	docker-compose exec backend python manage.py test
	docker-compose exec frontend npm run test

# 初次設置專案
init:
	@echo "🚀 初始化 Charlie Stock App..."
	@echo "📋 複製環境變數檔案..."
	cp stock-backend/.env.example stock-backend/.env
	@echo "🔨 建置容器..."
	docker-compose build
	@echo "🚀 啟動服務..."
	docker-compose up -d
	@echo "⏳ 等待資料庫啟動..."
	sleep 10
	@echo "📊 執行資料庫遷移..."
	docker-compose exec backend python manage.py migrate
	@echo "👤 創建超級用戶 (可選)..."
	@echo "如需創建管理員用戶，請執行: make createsuperuser"
	@echo "✅ 設置完成！"
	@echo "🌐 前端: http://localhost:3000"
	@echo "🔧 後端: http://localhost:8000"
	@echo "📊 後端管理: http://localhost:8000/admin"

# 創建超級用戶
createsuperuser:
	docker-compose exec backend python manage.py createsuperuser

# 收集靜態文件
collectstatic:
	docker-compose exec backend python manage.py collectstatic --noinput

# 查看容器狀態
status:
	docker-compose ps

# 前端相關指令
frontend-install:
	docker-compose exec frontend npm install

frontend-build:
	docker-compose exec frontend npm run build

# 後端相關指令
backend-install:
	docker-compose exec backend pip install -r requirements.txt

backend-makemigrations:
	docker-compose exec backend python manage.py makemigrations
