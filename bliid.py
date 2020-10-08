import requests
import json
BV = input("请输入BV号: ")
r = requests.get("https://api.bilibili.com/x/web-interface/view?bvid="+str(BV))
r.encoding = 'utf-8'
arr = json.loads(r.text)
avid=arr['data']['aid']
print("AV号为:"+str(avid))
getcid="https://www.bilibili.com/widget/getPageList?aid="+str(avid)
r = requests.get(getcid)
r.encoding = 'utf-8'
arr = json.loads(r.text)
cid=arr[0]["cid"]
print("Cid为:"+str(cid))
