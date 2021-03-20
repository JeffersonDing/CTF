#!/bin/bash
curl 'http://mercury.picoctf.net:42214/contribute.php' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Origin: http://mercury.picoctf.net:42214' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Referer: http://mercury.picoctf.net:42214/index.php' \
  -H 'Accept-Language: en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5' \
  -H 'Cookie: PHPSESSID=47d33bsi3t5a2aufogq9pulvj1' \
  --data-raw 'captcha=49&moneys=hello' \
  --compressed \
  --insecure