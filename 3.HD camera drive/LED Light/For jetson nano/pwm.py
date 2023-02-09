import Jetson.GPIO as GPIO
import time
import rospy
from multiprocessing import Process, Queue
from geometry_msgs.msg import Point,Twist


class PWM():
    def __init__(self, channel, frequency, level=1):
        self.channel = channel
        self.frequency = frequency
        if level == 1:
            self.HIGH = GPIO.HIGH
            self.LOW = GPIO.LOW
        elif level == 0:
            self.HIGH = GPIO.LOW
            self.LOW = GPIO.HIGH
        else:
            raise ValueError("ERROR: level's err")

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.channel, GPIO.OUT, initial=self.LOW)
        
        self.if_pwm = True
        self.if_change = False

    def ros_pwm(self):
        rospy.init_node("pwm")
        a = rospy.Subscriber("/pwm",Point,self.Change)

        f = 50.0
        c = 0.5
        t = 1/f
        t_h = t*c
        t_l = t*(1-c)
        print(t, t_h, t_l)


        while True:
            if self.if_change:
                f = self.frequency
                c = self.cycle
                t = 1/f
                t_h = t*c
                t_l = t*(1-c)
            if self.if_pwm:
                GPIO.output(self.channel, self.HIGH)
                time.sleep(t_h)
                GPIO.output(self.channel, self.LOW)
                time.sleep(t_l)
                print('f and c: ', f, '  ',c)
            if rospy.is_shutdown():
                exit()
        rospy.spin()


    def Change(self, data):
        if int(data.x) == 0:
            self.if_pwm = False
        else:
            self.if_pwm = True
        print("Change\n", data)
        self.frequency = data.y
        self.cycle = data.z
        self.if_change = True            

if __name__=="__main__":
    a = PWM(33,50)
    a.ros_pwm()

