from typing import Text
import uiautomator2 as u2

#链接手机
device = u2.connect('MQS0219628044133')

#点击微信

# device(text='微信').click()
# print(device.device_info)
# print(device.app_current())

#apk_package = 'com.tencent.mm'

#启动微信，通过包名
# device.app_start('com.tencent.mm')
#关闭微信
# device.app_stop('com.tencent.mm')


# device(text='百度贴吧').click()

# device(text='搜索').click()

# com.baidu.tieba
# app = 'com.baidu.tieba'
# print(device.app_current())
# device.app_stop(app)
# device.app_clear(app)

# device(text='百度贴吧').click()
# device.screenshot('1.png')
# device.push(r'C:\\Users\\17502\\OneDrive\\Vscode_mypy\\uiautomator2\1.txt',r'/1.txt')
# device.screen_on()
# device.press('home')
device.press('power')