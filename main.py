from gpiozero import Buzzer
from time import sleep

makerobo_Buzzer = 17  # 有源蜂鸣器管脚定义

# GPIO设置函数
def makerobo_setup():
    global bz
    bz = Buzzer(pin=makerobo_Buzzer, active_high=False)  # 设置管脚，及改为低电平开启蜂鸣器
    bz.off()

# 打开蜂鸣器
def makerobo_buzzer_on():
    bz.on()  # 蜂鸣器为低电平触发，所以使能蜂鸣器让其发声

# 关闭蜂鸣器
def makerobo_buzzer_off():
    bz.off()  # 蜂鸣器设置为高电平，关闭蜂鸣器

# 控制蜂鸣器鸣叫
def makerobo_beep(x):
    makerobo_buzzer_on()  # 打开蜂鸣器控制
    sleep(x)  # 延时时间
    makerobo_buzzer_off()  # 关闭蜂鸣器控制
    sleep(x)  # 延时时间

# 循环函数
def loop():
    while True:
        makerobo_beep(0.5)  # 控制蜂鸣器鸣叫，延时时间为500ms

# 清理函数
def destroy():
    bz.close()  # 关闭蜂鸣器并释放资源

# 程序入口
if __name__ == '__main__':
    makerobo_setup()  # 设置GPIO管脚
    try:
        loop()  # 调用循环函数
    except KeyboardInterrupt:  # 当按下Ctrl+C时，将执行destroy()子程序。
        destroy()  # 释放资源
