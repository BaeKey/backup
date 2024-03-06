#!/bin/bash
SSH_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo $SSH_KEY > ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
sed -i 's/^\(PasswordAuthentication \).*/\1no/' /etc/ssh/sshd_config
echo "SSH公钥配置完成，root用户密码登录已被禁用。"

echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p
echo "BBR配置完成。"

echo "更新软件包列表并安装最新云内核"
apt update
apt autoremove --purge qemu-guest-agent -y
apt install linux-image-cloud-amd64 -y
