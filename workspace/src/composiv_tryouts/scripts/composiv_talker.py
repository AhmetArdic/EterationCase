#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from composiv_tryouts.msg import hit
import random # hasar değeri üretmek için

def talker():

    pub = rospy.Publisher("hit_topic", hit, queue_size=10)
    #bu şekilde "hit_topic" isminde bir topic oluşturduk ve pub ismindeki objeye atadık

    rospy.init_node("composiv_talker", anonymous=True)
    #"composiv_talker" isminde bir düğüm tanımladık

    rate = rospy.Rate(1)
    #çalışma hızı 1 Hz

    max_health = 100 #vurulan kişinin ilk canı

    while(not rospy.is_shutdown()): 
        #bu şekilde ros sistemi çökmediği sürece while içerisine girebilecek
        
        hit_obj = hit()
        hit_obj.shooter = "Ahmet"
        hit_obj.hitted = "Alp"
        hit_obj.last_damage = random.randint(0, 100)
        hit_obj.hitted_health = max_health - hit_obj.last_damage
        #burada verileri yerleştirdik

        rospy.loginfo(hit_obj) 
        #verileri terminale yazdırmak için kullanacağız

        pub.publish(hit_obj)
        #yayınımızı tanımladık

        rate.sleep()
        #çalışma hızını yuakarıda belittiğimiz değerde tutmak için kullanılır

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
