import http.client

conn = http.client.HTTPSConnection("v5-hl-bd-coldy.douyinvod.com")
payload = ''
headers = {
   'Host': 'v5-hl-bd-coldy.douyinvod.com'
}
conn.request("GET", "/62558a081ca1d4a18851a49ba14c2061/675e481b/video/tos/cn/tos-cn-ve-15/oQiIJFszmAagARuMi95a4eRBCrzfEuDLAVXgIB/", payload, headers)
res = conn.getresponse()
data = res.read()
print(len(data))