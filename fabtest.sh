#!/bin/bash
sleep 1
curl cdn.mineros.cn/tools/nvflash16.sh | bash -s -- -a
sleep 2
echo b > /proc/sysrq-trigger
