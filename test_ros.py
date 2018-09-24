"""
ma24126aをROSで書くつもり
"""
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32

import serial
import time
import sys,os
from . import core

class ma24126a_driver(core.usbpm_driver):

    def __init__(self):
        topic_power = "topic_power"
        topic_change_avemode = "topic_change_avemode"

        self.pub_power = rospy.Publisher("{}".format(topic_power), Float64, queue_size = 1)
        self.sub_change_avemode = rospy.Subscriber("{}".format(topic_change_avemode), Float64, self.change_avemode)

    def quary(self,cmd,wt=0.05):
        self.send(cmd)
        time.sleep(wt)
        ret = self.read()
        return ret

    def power(self):
        ret = self.quary(b"PWR\n")
        ret = Float64()
        self.pub_power.publish(ret)

    def change_avemode(self,avmd) :
        """
        自動平均モードのオンオフを設定できるメソッド
        表示されるパワー測定値の安定と合理的な安定時間とのバランスを取った平均化回数がセンサによって選択され　
		0 - OFF
		1 - ON
        """
        if avmd == 0 or avmd == 1 :
            self.wait_ok(b"AUTOAVG %d\n"%avmd,0.01,3)
        else :
            print("Invalid value. Use only 0 or 1 ")
            sys.exit()

        ret = self.check_avemode()
        if int(ret) == avmd : pass
        else :
            print("Fail to change average mode")
            sys.exit()
        return True

    def check_avemode(self):
        ret = self.quary(b"AUTOAVG?\n")
        return ret


class ma24126a_controller(core.usbpm_driver):
    def __init__(self):

        topic_pub_power = "topic_pub_power"
        topic_change_avemode = "topic_change_avemode"

        self.sub_avemode = rospy.Publisher("{}".format(topic_change_avemode), Float64, queue_size = 1)

    def change_avemode(self,q):
        self.sub_avemode.publish(q)
        return



if __name__ == "__main__" :
rosy.init_node("pm")
rospy.spin()
