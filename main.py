#coding=utf8
import requests
import itchat

KEY='8edce3ce905a4c1dbb965e6b35c3834d'

#向图灵机器人发送消息，得到机器人的回答
def get_response(msg):
	apiUrl='http://www.tuling123.com/openapi/api'
	data={
		'key':KEY,
		'info':msg,
		'userid':'wechat-robot',
	}
	try:
		r=requests.post(apiUrl,data=data).json()
		#字典的get方法在字典没有'text'值的时候回返回None而不会抛出异常
		return r.get('text')
	except:
		return

#装饰器，实现微信消息的获取
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
	#获取的消息保存在msg['Text']中
	defaultReply='I received: '+msg['Text']
	reply=get_response(msg['Text'])
	return reply or defaultReply

#热启动，不用每次登录都要扫码了(第一次除外)
itchat.auto_login(hotReload=True)
itchat.run()