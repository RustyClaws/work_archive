import subprocess
curl_cmd = "curl 'https://www.fmz.com/ws_botvs_v1?compress=zlib&platform=web&zone=USD&version=1747022640722&uuid=927a610a-023f-489a-957a-0ea97af4697a&nonce=1747044020175&sign=f62259a992e2865b63a2e39e9f3e66e5165e99508f88f5401cae139eee209f37' \
  -H 'accept: */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -b 'session_token=017f25cbebb015428f3b98c576dc82d0; web_client=normal' \
  -H 'origin: https://www.fmz.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.fmz.com/robot/597675' \
  -H 'sec-ch-ua: \"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"Linux\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0' \
  --data-raw '{\"method\":[\"GetRobotLogs\"],\"params\":[{\"robotId\":597675,\"logMinId\":0,\"logMaxId\":0,\"logOffset\":0,\"logLimit\":20,\"profitMinId\":0,\"profitMaxId\":0,\"profitOffset\":0,\"profitLimit\":1000,\"chartMinId\":0,\"chartMaxId\":0,\"chartOffset\":0,\"chartLimit\":1000,\"chartUpdateBaseId\":0,\"chartUpdateDate\":0,\"summaryLimit\":1048576}],\"lang\":\"zh_CN\",\"token\":\"\",\"path\":\"/robot/597675\",\"cache\":0,\"callbackId\":\"5\",\"version\":3.7}'"

output = subprocess.check_output(curl_cmd, shell=True)
output = output.decode('utf-8')
# print(output)
with open('sub.txt','w') as f:
  f.write(output)

print("the data has saved!")
