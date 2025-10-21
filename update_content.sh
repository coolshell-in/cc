#!/bin/bash

# Exit if any command fails
set -e

# 网络诊断函数
network_diagnostic() {
    echo "===== 网络诊断 ====="
    echo "1. 测试 GitHub 连接性..."
    ping -c 3 github.com
    echo "2. 测试 HTTPS 连接..."
    curl -s -o /dev/null -w "HTTPS 状态码: %{http_code}\n" https://github.com
    echo "3. 当前时间: $(date)"
    echo "===================="
}

# 获取当前分支名
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')

# 设置提交信息
COMMIT_MSG="内容更新 [$TIMESTAMP]"

# 检查是否存在子模块
if [ -f ".gitmodules" ]; then
    echo "检测到子模块配置，重置子模块..."
    git submodule foreach --recursive git reset --hard
    git submodule update --init --recursive
fi

# 添加内容变更（排除主题目录）
echo "添加内容变更..."
git add -f -- . ':!themes/*' ':!public/*' ':!resources/*'

# 检查是否有需要提交的变更
if [ -n "$(git status --porcelain --ignore-submodules=all)" ]; then
    echo "检测到内容变更，提交更新..."
    git commit -m "$COMMIT_MSG"
    
    # 网络诊断
    network_diagnostic
    
    echo "推送到远程仓库 $CURRENT_BRANCH 分支..."
    
    # 切换到 HTTPS 协议
    echo "切换到 HTTPS 协议进行推送..."
    git remote set-url origin https://github.com/cooshell-in/cc.git
    
    # 增加 Git 缓冲区大小
    git config http.postBuffer 524288000  # 500MB
    
    # 使用更健壮的重试机制（移除了 timeout）
    max_retries=5
    retry_count=0
    push_success=false
    
    while [ $retry_count -lt $max_retries ] && [ "$push_success" = false ]; do
        # 直接执行推送（无 timeout）
        if git push --progress origin "$CURRENT_BRANCH"; then
            push_success=true
        else
            retry_count=$((retry_count + 1))
            echo "推送失败 (尝试 $retry_count/$max_retries)，30秒后重试..."
            
            # 网络诊断
            network_diagnostic
            
            sleep 30
        fi
    done
    
    if [ "$push_success" = false ]; then
        echo "错误: 推送失败，已达到最大重试次数"
        echo "尝试手动推送: git push origin $CURRENT_BRANCH"
        exit 1
    else
        echo "推送成功！"
        exit 0
    fi
else
    echo "没有检测到内容变更"
    exit 0
fi