
curl 
'https://www.fmz.com/ws_botvs_v1?compress=zlib&platform=web&zone=USD&version=1747022640722&uuid=7e6ab50b-1848-408f-9bf7-1441263cca53&nonce=1747031066923&sign=2bbd57d4fa07a3bdbdd70c84ef37a54510a024a19bf4cc29dba71927de16d03d' -
-compressed -X POST 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0' 
-H 'Accept: */*' 
-H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' 
-H 'Accept-Encoding: gzip, deflate, br, zstd' 
-H 'Referer: https://www.fmz.com/robot/597675' 
-H 'Content-Type: application/json' 
-H 'Origin: https://www.fmz.com' 
-H 'DNT: 1' 
-H 'Sec-GPC: 1' 
-H 'Connection: keep-alive' 
-H 'Cookie: session_token=4df74564bdf0ce7a9762a443781a53ee; web_client=normal' 
-H 'Sec-Fetch-Dest: empty' 
-H 'Sec-Fetch-Mode: cors' 
-H 'Sec-Fetch-Site: same-origin' 
-H 'Priority: u=4' 
-H 'Pragma: no-cache' 
-H 'Cache-Control: no-cache' 
-H 'TE: trailers' --data-raw '{"method":["GetRobotLogs"],"params":[{"robotId":597675,"logMinId":0,"logMaxId":0,"logOffset":0,"logLimit":20,"profitMinId":0,"profitMaxId":0,"profitOffset":0,"profitLimit":1000,"chartMinId":0,"chartMaxId":0,"chartOffset":0,"chartLimit":1000,"chartUpdateBaseId":0,"chartUpdateDate":0,"summaryLimit":1048576}],"lang":"zh_CN","token":"","path":"/robot/597675","cache":0,"callbackId":"5","version":3.7}'


$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.Cookies.Add((New-Object System.Net.Cookie("session_token", "4df74564bdf0ce7a9762a443781a53ee", "/", "www.fmz.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("web_client", "normal", "/", "www.fmz.com")))
Invoke-WebRequest -UseBasicParsing -Uri "https://www.fmz.com/ws_botvs_v1?compress=zlib&platform=web&zone=USD&version=1747022640722&uuid=7e6ab50b-1848-408f-9bf7-1441263cca53&nonce=1747031066923&sign=2bbd57d4fa07a3bdbdd70c84ef37a54510a024a19bf4cc29dba71927de16d03d" `
-Method POST `
-WebSession $session `
-UserAgent "Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0" `
-Headers @{
"Accept" = "*/*"
  "Accept-Language" = "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
  "Accept-Encoding" = "gzip, deflate, br, zstd"
  "Referer" = "https://www.fmz.com/robot/597675"
  "Origin" = "https://www.fmz.com"
  "DNT" = "1"
  "Sec-GPC" = "1"
  "Sec-Fetch-Dest" = "empty"
  "Sec-Fetch-Mode" = "cors"
  "Sec-Fetch-Site" = "same-origin"
  "Priority" = "u=4"
  "Pragma" = "no-cache"
  "Cache-Control" = "no-cache"
  "TE" = "trailers"
} `
-ContentType "application/json" `
-Body "{`"method`":[`"GetRobotLogs`"],`"params`":[{`"robotId`":597675,`"logMinId`":0,`"logMaxId`":0,`"logOffset`":0,`"logLimit`":20,`"profitMinId`":0,`"profitMaxId`":0,`"profitOffset`":0,`"profitLimit`":1000,`"chartMinId`":0,`"chartMaxId`":0,`"chartOffset`":0,`"chartLimit`":1000,`"chartUpdateBaseId`":0,`"chartUpdateDate`":0,`"summaryLimit`":1048576}],`"lang`":`"zh_CN`",`"token`":`"`",`"path`":`"/robot/597675`",`"cache`":0,`"callbackId`":`"5`",`"version`":3.7}"

await fetch("https://www.fmz.com/ws_botvs_v1?compress=zlib&platform=web&zone=USD&version=1747022640722&uuid=7e6ab50b-1848-408f-9bf7-1441263cca53&nonce=1747031066923&sign=2bbd57d4fa07a3bdbdd70c84ef37a54510a024a19bf4cc29dba71927de16d03d", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/json",
        "Sec-GPC": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=4",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    },
    "referrer": "https://www.fmz.com/robot/597675",
    "body": "{\"method\":[\"GetRobotLogs\"],\"params\":[{\"robotId\":597675,\"logMinId\":0,\"logMaxId\":0,\"logOffset\":0,\"logLimit\":20,\"profitMinId\":0,\"profitMaxId\":0,\"profitOffset\":0,\"profitLimit\":1000,\"chartMinId\":0,\"chartMaxId\":0,\"chartOffset\":0,\"chartLimit\":1000,\"chartUpdateBaseId\":0,\"chartUpdateDate\":0,\"summaryLimit\":1048576}],\"lang\":\"zh_CN\",\"token\":\"\",\"path\":\"/robot/597675\",\"cache\":0,\"callbackId\":\"5\",\"version\":3.7}",
    "method": "POST",
    "mode": "cors"
});