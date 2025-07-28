#!/bin/bash

# Exit if any command fails
set -e

# 获取当前分支名
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# 检查是否存在子模块
if [ -f ".gitmodules" ]; then
    echo "检测到子模块配置，重置子模块..."
    # 重置所有子模块的更改
    git submodule foreach --recursive git reset --hard
    
    echo "更新子模块..."
    # 确保子模块是最新版本
    git submodule update --init --recursive
fi

# 添加所有更改（排除子模块目录）
echo "添加内容变更..."
git add -- . ':!themes/*' ':!public/*' ':!resources/*'

# 检查是否有需要提交的变更
if [ -n "$(git status --porcelain --ignore-submodules=all)" ]; then
    echo "检测到内容变更，提交更新..."
    TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')
    git commit -m "内容更新 [$TIMESTAMP]"
    
    echo "推送到远程仓库 $CURRENT_BRANCH 分支..."
    # 使用重试机制推送
    max_retries=5
    retry_count=0
    
    while [ $retry_count -lt $max_retries ]; do
        if git push origin "$CURRENT_BRANCH"; then
            echo "推送成功！"
            exit 0
        else
            retry_count=$((retry_count + 1))
            echo "推送失败 (尝试 $retry_count/$max_retries)，10秒后重试..."
            sleep 10
        fi
    done
    
    echo "错误: 推送失败，已达到最大重试次数"
    exit 1
else
    echo "没有检测到内容变更"
    exit 0
fi