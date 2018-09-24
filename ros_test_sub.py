"""
ROS subscriber
"""
import rospy

rospy.init_node("sub")
#sub起動のおまじない

topic_name = "test"　
from stg_msgs.msg import Float64
def test_method(q):
    print(q)
#topinの名前、メッセージ型、callback関数を決める

sub = rospy.Subscriber(topic_name, Float64, test_method)

rospy.spin()
#sub始動のおまじない
