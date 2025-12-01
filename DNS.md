# DNS

## 端口-53 协议-udp 地区-CN

114
```
114.114.114.114
```

四川移动
```
183.221.253.100
```

四川联通
```
119.6.6.6
```

四川电信
```
218.6.200.139
```

四川电信
```
61.139.2.69
```

阿里
```
223.5.5.5
```

腾讯
```
119.29.29.29
```

## 端口-853 协议-tls 地区-Global

Cloudflare
```
1dot1dot1dot1.cloudflare-dns.com
```

OpenDNS
```
sandbox.opendns.com
```

Yandex
```
common.dot.dns.yandex.net
```

中国台湾 Quad101
```
dns.twnic.tw
```

DNS.SB
```
dot.sb
```

日本IIJ
```
public.dns.iij.jp
```

Quad9 无过滤服务
```
dns10.quad9.net
```

AdGuard无过滤服务
```
unfiltered.adguard-dns.com
```

日本Blahdns
```
dot-jp.blahdns.com
```

新加坡Blahdns
```
dot-sg.blahdns.com
```

Google
```
dns.google
```

AdGuard无过滤服务
```
unfiltered.adguard-dns.com
```

AdGuard无过滤服务
```
unfiltered.adguard-dns.com
```

Bebas 无过滤服务
```
unfiltered.dns.bebasid.com
```

CFIEC
```
dns.cfiec.net
```

ControlD 无过滤服务
```
p0.freedns.controld.com
```

Mulvad 无过滤服务
```
doh.mullvad.net
```

NextDNS
```
anycast.dns.nextdns.io
```

RethinkDNS 无过滤服务
```
max.rethinkdns.com
```

CIRA Shield DNS 无过滤服务
```
private.canadianshield.cira.ca
```

# WARP-clash订阅

[https://tofree.zeabur.app/](https://tofree.zeabur.app/)
```
https://subs.zeabur.app/clash
```

[https://neko-warp.nloli.xyz/](https://neko-warp.nloli.xyz/)
```
https://neko-warp.nloli.xyz/neko_warp.yaml
```

# 列表

AdBlock DNS Filters

[https://github.com/217heidai/adblockfilters](https://github.com/217heidai/adblockfilters)

```
https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt
```
china-list

[https://github.com/Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)

```
https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/china-list.txt
```

# Termux优选对端IP

```
curl -sSL https://gitlab.com/rwkgyg/CFwarp/raw/main/point/endip.sh -o endip.sh && chmod +x endip.sh && ./endip.sh
```

# 计划任务更新ipset

```
0 16 * * * curl -s https://gaoyifan.github.io/china-operator-ip/cmcc.txt | tee /dev/stderr | cat - <(curl -s https://gaoyifan.github.io/china-operator-ip/cmcc6.txt) > /etc/mwan3helper/cmcc.txt
0 17 * * * curl -s https://gaoyifan.github.io/china-operator-ip/unicom.txt | tee /dev/stderr | cat - <(curl -s https://gaoyifan.github.io/china-operator-ip/unicom6.txt) > /etc/mwan3helper/unicom_cnc.txt
0 18 * * * curl -s https://ispip.clang.cn/chinatelecom.txt | tee /dev/stderr | cat - <(curl -s https://ispip.clang.cn/chinatelecom_ipv6.txt) > /etc/mwan3helper/chinatelecom.txt
0 19 * * * curl -s https://cdn.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/gfw.txt > /etc/mwan3helper/gfw.txt
```
