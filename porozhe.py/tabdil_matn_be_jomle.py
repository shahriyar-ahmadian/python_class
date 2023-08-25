import pyttsx3
engine = pyttsx3.init()
engine.say("this is  a your jommele")
""" RATE"""
rate = engine.getProperty('rate') 
(rate) 
engine.setProperty('rate',125) 
"""VOLUME"""
volume = engine.getProperty('volume') 
(volume) 
engine.setProperty('volume',1.0)  

"""VOICE"""

voices = engine.getProperty('voices') 

engine.setProperty('voice', voices[1].id) 
 

engine.say(input('enter ajomle:'))
engine.runAndWait()
engine.stop()
"""Saving Voice to a file"""

engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()