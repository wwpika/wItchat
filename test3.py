#coding=utf8
import requests

apiUrl='http://www.tuling123.com/openapi/api'
data={
	'key':'8edce3ce905a4c1dbb965e6b35c3834d',
	'info':'hello kk',
	'userid':'wechat-robot',
}

r=requests.post(apiUrl,data=data).json()

print(r)