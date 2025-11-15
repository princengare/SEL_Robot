#!/usr/bin/env python3
import sys
import rospy
from std_msgs.msg import String
from qt_robot_interface.srv import *

class Talker:
    
    def __init__(self, speechConfig, speechSay, emotionShow, talkText, gesturePlay, recognize):
        self.speechConfig = speechConfig
        self.speechSay = speechSay
        self.emotionShow = emotionShow
        self.talkText = talkText
        self.gesturePlay = gesturePlay
        self.recognize = recognize
        
    '''
       set which voice to use 
    '''
    def set_speaker(self, speaker):
        pass
    
    '''
        adjust volume of speaker
    '''
    def set_volume(self, volume):
        pass
    
    '''
        display an emotion
    '''
    def set_emotion(self, emotion):
        self.emotionShow(emotion)
    
    '''
        do an action
    '''
    def set_action(self, action):
        self.gesturePlay(action)
    
    '''
        say a phrase
    '''
    def speak(self, phrase):
        self.talkText(phrase)
    
    '''
        concurrent actions/emotions/speech
    '''
    def simultaneous(self):
        pass
    
    '''
        based on pickle file and past input, pick next phrase to say
    '''
    def get_next_phrase(self, pkl, input):
        pass

    '''
        wait for a response from the user and return result
    '''
    def get_response(self, options):
        resp = self.recognize('en-US', options, 0)
        return resp