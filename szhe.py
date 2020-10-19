url = "http://47.102.118.1:8089/api/problem?stuid=031804120"
# 发送get请求
r=requests.get(url)
user_dic = json.loads(r.text)
# swap=user_dic['step']
# uuid=user_dic['uuid']
data = user_dic['img']
image_data = base64.b64decode(data)
np_img=imageio.imread(image_data)
plt.imshow(np_img)
plt.show()
