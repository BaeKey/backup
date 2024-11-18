#!/bin/bash
SSH_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo $SSH_KEY > ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
sed -i 's/^#\?\(PasswordAuthentication \).*/\1no/' /etc/ssh/sshd_config
sed -i 's/^#\?\(Port \).*/\121112/' /etc/ssh/sshd_config
echo "SSH公钥配置完成，root用户密码登录已被禁用。"

echo "net.core.default_qdisc= fq " >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control= bbr " >> /etc/sysctl.conf
echo "net.ipv4.tcp_window_scaling = 2" >> /etc/sysctl.conf
echo "net.ipv4.tcp_rmem = 4096 16384 11050000" >> /etc/sysctl.conf
echo "net.ipv4.tcp_wmem = 4096 87380 11050000" >> /etc/sysctl.conf
echo "net.ipv4.tcp_pacing_ca_ratio = 110" >> /etc/sysctl.conf
echo "net.core.rmem_max = 33554432" >> /etc/sysctl.conf
echo "net.core.wmem_max = 33554432" >> /etc/sysctl.conf

sysctl -p
echo "BBR配置完成,TCP网络协议配置完成"

echo "更新软件包列表并安装最新云内核"
apt update
apt autoremove --purge qemu-guest-agent -y
apt install linux-image-cloud-amd64 -y

echo "禁用内存超售模块"
echo "blacklist virtio_balloon" | tee /etc/modprobe.d/blacklist.conf && update-initramfs -u
