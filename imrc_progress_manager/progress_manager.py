import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Empty

from imrc_messages.msg import ConpanelBuzzerControl
from imrc_messages.srv import ProgressInfo
from imrc_messages.msg import MissBallInfo
from imrc_messages.srv import ResetMissBall

class ProgressManager(Node):
    def __init__(self):
        super().__init__('progress_manager')
        self.conpanel_miss_ball_sub = self.create_subscription(String, 'conpanel_miss_ball', self.conpanel_miss_ball_callback, 10)
        self.progress_info_srv = self.create_service(ProgressInfo, 'progress', self.progress_info_callback)

        self.miss_ball_pub = self.create_publisher(MissBallInfo, 'miss_ball', 10)
        self.miss_ball_tim = self.create_timer(1.0, self.publish_miss_ball)

        self.conpanel_bz_pub = self.create_publisher(ConpanelBuzzerControl, 'conpanel_bz', 10)

        self.miss_ball_reset_srv = self.create_service(ResetMissBall, "reset_miss_ball", self.miss_ball_reset_callback)
        
        self.logger = self.get_logger()

        # 0: Red, 1: Blue, 2: Yellow
        self.ball_color = 0
        self.isOK = False
        self.miss = [0, 0, 0]

        self.logger.info("Progress Manager node initialized.")
    
    def publish_miss_ball(self):
        mbi = MissBallInfo()
        mbi.miss_red = self.miss[0]
        mbi.miss_blue = self.miss[1]
        mbi.miss_yellow = self.miss[2]

        self.miss_ball_pub.publish(mbi)
    
    def miss_ball_reset_callback(self, request, response):
        self.logger.info(f"Reset miss ball count. Color is: {0}", request.color)
        if(request.color == "RED"):
            self.miss[0] = 0
        elif(request.color == "BLUE"):
            self.miss[1] = 0
        elif(request.color == "YELLOW"):
            self.miss[2] = 0
        else:
            self.miss[0] = 0
            self.miss[1] = 0
            self.miss[2] = 0

        return response

    def conpanel_bz_feedback(self, num):
        self.logger.info("Publish buzzer signal \"{0}\"".format(num))
        bz = ConpanelBuzzerControl()
        bz.count = num
        bz.isloop = False
        self.conpanel_bz_pub.publish(bz)

    def progress_info_callback(self, request, response):
        response.miss_red = self.miss[0]
        response.miss_blue = self.miss[1]
        response.miss_yellow = self.miss[2]

        return response

    def conpanel_miss_ball_callback(self, msg):
        data = msg.data

        self.logger.info("Received conpanel_miss_ball \"{0}\"".format(data))

        if(data == "Red"):
            self.ball_color = 0
        elif(data == "Blue"):
            self.ball_color = 1
        elif(data == "Yellow"):
            self.ball_color = 2
        
        if(data == "OK"):
            if(self.isOK == False):
                self.isOK = True
                # conpanelにfeedbackする
                self.conpanel_bz_feedback(self.miss[self.ball_color])
            else:
                self.isOK = False
        elif(data == "NG"):
            self.miss[self.ball_color] = 0
            self.isOK = False
        else:
            self.miss[self.ball_color] += 1

def main():
    rclpy.init()
    ledController = ProgressManager()
    rclpy.spin(ledController)
    rclpy.shutdown()

