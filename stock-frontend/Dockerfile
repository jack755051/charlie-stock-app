# 使用官方 Node.js 18 運行時作為基礎映像
FROM node:18-alpine

# 設置工作目錄
WORKDIR /app

# 安裝 pnpm (Nuxt 推薦的包管理器)
RUN npm install -g pnpm

# 複製 package.json 和 pnpm-lock.yaml (如果存在)
COPY package*.json ./
COPY pnpm-lock.yaml* ./

# 安裝依賴
RUN pnpm install

# 複製專案文件
COPY . .

# 創建非 root 用戶
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nuxtjs -u 1001 && \
    chown -R nuxtjs:nodejs /app
USER nuxtjs

# 暴露端口
EXPOSE 3000

# 設置環境變數
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

# 健康檢查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000 || exit 1

# 啟動命令
CMD ["pnpm", "dev"]
