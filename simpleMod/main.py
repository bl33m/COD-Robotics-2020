import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from sensor_msgs.msg import Joy

def callback(data):
    move_cmd = Twist()          ## create object of msg type twist 
    move_cmd.linear.x =  -1*data.axes[3]    ## assinge liner and anguler value
    move_cmd.angular.z = -4*data.axes[4]
    pos = data.axes[5]
    pubAngle.publish(pos)
    pubDrive.publish(move_cmd)

   

## main logic of the node 
def main():

    ## user rospy to create node nasa_control
    rospy.init_node('nasa_control')
    global pubDrive
    global pubAngle

    ## create publisher object the publishes to the /simple_model/diff_drive_controller/cmd_vel topic with msg type twist
    pubDrive = rospy.Publisher('/simple_model/diff_drive_controller/cmd_vel', Twist, queue_size = 100)
    pubAngle = rospy.Publisher('/simple_model/Rev5_position_controller/command', Float64, queue_size = 100)
    sub = rospy.Subscriber('joy', Joy, callback)  
    rate = rospy.Rate(100) # publishing rate in hz
    

    
    rospy.spin()


if __name__ =='__main__':
    main()
