import werobot

robot = werobot.WeRoBot(token='non')
robot.config["APP_ID"] = "wx9742a414146d815a"
robot.config["APP_SECRET"] = "628c6b7f77c9f0ad356174ddd6ad2c64"
robot.config['ENCODING_AES_KEY'] = 'zDSkLBNeNTNd5uku0JfeOJkT5H34GirtH8sMeJ97BvY'
@robot.text
def hello(message):
    if message.content == "小黄歌":
        return u'链接: https://pan.baidu.com/s/1eR6rUiI 密码: n4b8'
    elif message.content == "追剧":
        return u'http://www.myei.cc/show/25824.html?from=timeline\n 将链接拷贝至手机浏览器直接播放即可\nmagnet:?xt=urn:btih:3a6d76a16e86e411ef2df070b8cf817b74ea840f&dn=人民的名义（送审样片）.全集.\n联盟MP4-www.lmp4.cn\n也可将本链接在百度网盘中离线下载、观看\n小编缓存了47集以后的部分，链接如下\n链接: https://pan.baidu.com/s/1bp1ozHP 密码: vv2k'
    elif message.content =="B站下载":
        return u'链接: https://pan.baidu.com/s/1dFL3cdz 密码: fc8m'
    else:
        return u'我们的聊天机器人正在部署中，有什么问题和建议可以告诉我们'
# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()