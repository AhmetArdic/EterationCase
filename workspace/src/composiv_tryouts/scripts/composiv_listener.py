#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from composiv_tryouts.msg import hit

def callback(data):
    rospy.loginfo("%s -> %d damage -> %s (%d health)", data.shooter, data.last_damage, data.hitted, data.hitted_health)
    #veriler geldiğinde onları terminale yazdırmak için bu fonksiyonu ve loginfo'yu yazdık

def listener():

    rospy.init_node("composiv_listener", anonymous=True) 
    #"composiv_listener" isminde bir düğüm tanımladık

    rospy.Subscriber("hit_topic", hit, callback)
    #abone olmak için topic ismi, msg dosya ismi ve yazdigimiz fonksiyon callback olarak verilir

    rospy.spin()

if __name__ == '__main__':

  listener()