#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import rospy
from composiv_tryouts.msg import hit
from time import sleep
import rostest

class TalkerTest(unittest.TestCase):

    talker_ok = False

    def callback(self, data):
        self.talker_ok = True

    def test1(self):
        rospy.init_node("composiv_listener", anonymous=True)
        rospy.Subscriber("hit_topic", hit, self.callback)

        counter = 0
        while not rospy.is_shutdown() and counter < 5 and (not self.talker_ok):
            #eğet ros açık ve talker'dan mesaj 5 kere doğru alınırsa while döngüsünden çıkar
            sleep(1)
            counter = counter + 1

        self.assertTrue(self.talker_ok)

if __name__ == '__main__':

  rostest.unitrun("composiv_tryouts", "talker_test", TalkerTest)