---
date: 2026-09-06
linktitle: "Ubuntu"

title: "Ubuntu 学习指南：从入门到进阶"
weight: 13
cascade:
    type: docs
    no_list: true
---

> 适用于 Ubuntu 22.04 / 24.04 / 26.04 及衍生版本

---

## 一、学习路线总览

| 阶段 | 目标 | 建议时长 |
|------|------|----------|
| 入门 | 熟悉桌面环境和基本操作 | 1-2 天 |
| 命令行 | 掌握常用终端命令 | 1-2 周 |
| 系统管理 | 服务、用户、磁盘、网络管理 | 2-4 周 |
| 开发环境 | 搭建开发工具链，编写 Shell 脚本 | 持续实践 |

---

## 二、阶段一：入门 — 熟悉桌面环境

- 学会用 **Activities（活动）** 搜索应用、管理窗口
- 熟悉 **文件管理器 (Nautilus)** 的基本操作
- 了解 **Settings** 里的网络、显示、电源等设置
- 学会通过 **App Center / Snap** 安装软件

### 常用快捷键

| 快捷键 | 功能 |
|--------|------|
| `Super` | 打开活动概览 |
| `Super + A` | 显示应用程序列表 |
| `Super + L` | 锁屏 |
| `Super + D` | 显示桌面 |
| `Alt + Tab` | 切换窗口 |
| `Ctrl + Alt + T` | 打开终端 |
| `Super + 方向键` | 窗口贴靠（左/右/最大化） |
| `Print Screen` | 截图 |

---

## 三、阶段二：命令行 — 核心能力

### 3.1 文件与目录操作

```bash
ls              # 列出目录内容
ls -la          # 列出详细信息（含隐藏文件）
cd /path/to/dir # 切换目录
cd ~            # 回到主目录
cd ..           # 回到上级目录
pwd             # 显示当前路径
cp src dest     # 复制文件
cp -r src dest  # 复制目录
mv src dest     # 移动/重命名
rm file         # 删除文件
rm -rf dir      # 强制递归删除目录（慎用！）
mkdir dir       # 创建目录
mkdir -p a/b/c  # 递归创建多级目录
touch file      # 创建空文件 / 更新时间戳
find /path -name "*.txt"  # 按名称查找文件
tree            # 以树形结构显示目录
```

### 3.2 文件权限

```bash
chmod 755 file  # 设置权限（rwxr-xr-x）
chmod +x script.sh  # 添加执行权限
chown user:group file  # 修改所有者
```

**权限数字对照表：**

| 数字 | 权限 | 说明 |
|------|------|------|
| 7 | rwx | 读+写+执行 |
| 6 | rw- | 读+写 |
| 5 | r-x | 读+执行 |
| 4 | r-- | 只读 |
| 3 | -wx | 写+执行 |
| 2 | -w- | 只写 |
| 1 | --x | 只执行 |
| 0 | --- | 无权限 |

### 3.3 系统信息

```bash
uname -a        # 系统和内核信息
lsb_release -a  # Ubuntu 版本信息
df -h           # 磁盘使用情况
du -sh ~/path   # 目录大小
free -h         # 内存使用情况
top             # 实时进程监控（按 q 退出）
htop            # 增强版进程监控（需安装）
ps aux          # 列出所有进程
uptime          # 系统运行时间和负载
```

### 3.4 软件管理

```bash
# APT 包管理（Debian/Ubuntu 原生）
sudo apt update              # 更新软件源索引
sudo apt upgrade             # 升级所有已安装软件
sudo apt install package     # 安装软件
sudo apt remove package      # 卸载软件
sudo apt autoremove          # 清理无用依赖
apt search keyword           # 搜索软件包
apt show package             # 查看软件包详情

# Snap 包管理
sudo snap install app        # 安装 Snap 应用
sudo snap remove app         # 卸载 Snap 应用
snap list                    # 列出已安装的 Snap
snap refresh                 # 更新所有 Snap

# Flatpak（需先安装）
flatpak install app          # 安装 Flatpak 应用
flatpak list                 # 列出已安装应用
```

### 3.5 网络相关

```bash
ip addr             # 查看 IP 地址
ip link             # 查看网络接口
ping google.com     # 测试网络连通性
curl -O url         # 下载文件
wget url            # 下载文件
ssh user@host       # SSH 远程连接
scp file user@host:/path  # 通过 SSH 复制文件到远程
```

### 3.6 文本处理

```bash
cat file            # 显示文件内容
less file           # 分页浏览（按 q 退出）
head -n 20 file     # 查看前 20 行
tail -f logfile     # 实时追踪日志
grep "pattern" file # 搜索匹配行
grep -r "text" dir/ # 递归搜索目录
sed 's/old/new/g' file  # 文本替换
awk '{print $1}' file   # 按列提取
wc -l file          # 统计行数
sort file           # 排序
uniq                # 去重
```

### 3.7 管道与重定向

```bash
# 管道：将前一个命令的输出传给下一个
cat file | grep "error" | wc -l

# 重定向
command > file      # 输出写入文件（覆盖）
command >> file     # 输出追加到文件
command 2>&1        # 合并标准错误到标准输出
command < file      # 从文件读取输入
```

---

## 四、阶段三：系统管理

### 4.1 Systemd 服务管理

```bash
systemctl status service    # 查看服务状态
systemctl start service     # 启动服务
systemctl stop service      # 停止服务
systemctl restart service   # 重启服务
systemctl enable service    # 开机自启
systemctl disable service   # 取消开机自启
systemctl list-units --type=service  # 列出所有服务

journalctl -u service       # 查看服务日志
journalctl -f               # 实时追踪系统日志
journalctl --since "1 hour ago"  # 查看最近 1 小时日志
```

### 4.2 用户与权限管理

```bash
sudo useradd -m username       # 创建用户（含主目录）
sudo passwd username           # 设置密码
sudo usermod -aG sudo username # 添加到 sudo 组
sudo userdel -r username       # 删除用户及其主目录
sudo su - username             # 切换到其他用户

# sudo 权限管理
sudo visudo                    # 编辑 sudoers 文件
```

### 4.3 磁盘分区与挂载

```bash
lsblk                 # 查看块设备
sudo fdisk -l         # 查看磁盘分区表
sudo fdisk /dev/sdb   # 对新磁盘分区
sudo mkfs.ext4 /dev/sdb1  # 格式化分区
sudo mount /dev/sdb1 /mnt   # 挂载分区
sudo umount /mnt          # 卸载

# 开机自动挂载：编辑 /etc/fstab
# /dev/sdb1  /mnt/data  ext4  defaults  0  2
```

### 4.4 防火墙 (UFW)

```bash
sudo ufw status           # 查看防火墙状态
sudo ufw enable           # 启用防火墙
sudo ufw allow 22         # 允许 SSH
sudo ufw allow 80         # 允许 HTTP
sudo ufw allow 443        # 允许 HTTPS
sudo ufw deny 3306        # 拒绝 MySQL 端口
sudo ufw delete allow 80  # 删除规则
sudo ufw reset            # 重置所有规则
```

### 4.5 定时任务

```bash
# Cron 定时任务
crontab -e                # 编辑当前用户的定时任务
crontab -l                # 列出定时任务

# 格式：分 时 日 月 星期 命令
# 示例：每天凌晨 3 点备份
0 3 * * * /home/user/backup.sh

# Systemd Timer（更现代的替代方案）
# 创建 /etc/systemd/system/backup.timer 和 backup.service
```

---

## 五、阶段四：开发环境搭建

### 5.1 Git

```bash
sudo apt install git
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
git clone https://github.com/user/repo.git
git status / add / commit / push / pull
```

### 5.2 Docker

```bash
# 安装
sudo apt install docker.io
sudo usermod -aG docker $USER  # 免 sudo 运行（需重新登录）

# 使用
docker pull ubuntu
docker run -it ubuntu bash
docker ps / stop / rm
docker images / rmi
```

### 5.3 Node.js (通过 NVM)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use 20
```

### 5.4 Python 虚拟环境

```bash
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install package
deactivate
```

### 5.5 Shell 脚本基础

```bash
#!/bin/bash
# 示例脚本：hello.sh

NAME="World"
echo "Hello, $NAME!"

# 条件判断
if [ -f "/etc/os-release" ]; then
    echo "系统信息文件存在"
fi

# 循环
for file in *.txt; do
    echo "处理文件: $file"
done

# 函数
greet() {
    echo "你好, $1!"
}
greet "Ubuntu"
```

---

## 六、推荐在线资源

| 资源 | 链接 | 说明 |
|------|------|------|
| Ubuntu 官方教程 | https://ubuntu.com/tutorials | 官方出品，覆盖安装、服务器、开发等场景 |
| Ubuntu 中文文档 | https://people.ubuntu.com/~happyaron/udc-cn/ | 中文翻译的系统课程，适合入门 |
| Ubuntu Server 文档 | https://ubuntu.com/server/docs | 偏服务器运维，适合进阶学习 |
| Ubuntu Manpage 手册 | https://manpages.ubuntu.com/ | 所有命令的在线手册，随查随用 |
| 滚雪球学 Ubuntu 全方位指南 | https://m.blog.csdn.net/weixin_43970743/article/details/143305691 | 中文系列教程，从基础到高级 |
| 从零到精通 Linux 入门指南 | https://blog.csdn.net/2402_84764726/article/details/158978706 | 万字深度教程，适合系统学习 |
| Linux 命令大全 | https://manpages.ubuntu.com/ | 当字典查，遇到不会的命令就翻手册 |

---

## 七、学习建议

1. **以用代学**：最好的学习方式就是每天在终端里操作，遇到问题先尝试用命令行解决
2. **每天 15 分钟**：坚持每天在终端练习，1-2 周就能形成肌肉记忆
3. **善用 man 手册**：遇到不认识的命令，先 `man command` 查看手册
4. **搭建实战项目**：比如搭一个 Web 服务器、配置 Docker 容器、写自动化脚本
5. **加入社区**：Ubuntu 中文论坛、Stack Overflow、Ask Ubuntu 都是好去处

---

*文档生成时间：2026-09-06*
*适用系统：Ubuntu 22.04 / 24.04 / 26.04 LTS*
