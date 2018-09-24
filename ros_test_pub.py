"""
ROS　publish
"""

import rospy

rospy.init_node("pub")
#pub起動のおまじない

topic_name = "test"
from std_msgs.msg import Float64
msg = Float64()
msg.data = 1000000
#topicの名前、メッセージ型をきめる

pub = rospy.Publisher(topic_name, Float64, queue_size=1)

pub.publish(msg)
#pubishする
