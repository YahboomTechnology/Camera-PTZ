import wiringpi
import time

OUTPUT = 1
PIN_TO_PWM = 1                                #定义PIN_TO_PWM为1脚
wiringpi.wiringPiSetup()                        #设置GPIO编号为wPi方式
wiringpi.pinMode(PIN_TO_PWM,OUTPUT)             #设置PIN_TO_PWM为OUTPUT输出模式
wiringpi.softPwmCreate(PIN_TO_PWM,0,100)        #设置PWM输出引脚为PIN_TO_PWM,PWM范围是0-100
while 1:
        wiringpi.softPwmWrite(PIN_TO_PWM,0)
        time.sleep(1)
        wiringpi.softPwmWrite(PIN_TO_PWM,50)
        time.sleep(1)
        wiringpi.softPwmWrite(PIN_TO_PWM,0)
