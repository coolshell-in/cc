#!/bin/bash

# Exit if any command fails
set -e

# Get the current branch name
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Add all changes
git add .

# Check if there are changes to commit
if [ -n "$(git status --porcelain)" ]; then
  echo "检测到内容变更，提交更新..."
  git commit -m "Update content"
  
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