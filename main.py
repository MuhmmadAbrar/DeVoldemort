from setuptools import Command
import speech_recognition as sr
import pyttsx3 
import webbrowser
import random
import wikipedia
import googletrans
from time import localtime, strftime
import time
import os
   
r = sr.Recognizer() 
  
def SpeakText(command):
      
    # Initialize the engine
    print(command)
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
    
def wiki(s):
    print(wikipedia.summary(s,sentences=2))
              
while(True):    
      
    
    try:
          
        with sr.Microphone() as source2:
              
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Listening") 
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            message = MyText.lower()
            print(MyText)
            
        if 'goodbye' in message or ('power off') in message or ('stop') in message:                          
            rand ='Goodbye Sir. Powering off in 3.. 2.. 1.. 0'
            SpeakText(rand)
            break
            
        if 'tell me about' in message:
            se=message[14::]
            rand=str(wikipedia.summary(se,sentences=2))
            SpeakText(rand)

        elif ('hello') in message or ('hi') in message:
            rand ="Hello Sir. I'm Your Assistant . At Your Service Sir. "
            SpeakText(rand)

        elif ('thanks') in message or ('tanks') in message or ('thank you') in message:
            l1=['You are welcome','You are Extremely Welcome !','Always a pleasure ! ','You are welcome,I was literally made for this thing..!']
            rand =random.choice(l1)
            SpeakText(rand)

        elif ('jash') in message:
            rand ='Yes Sir . Waiting for your command!..'
            SpeakText(rand)


        elif  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand ="I'm fine! What can I do for you??"
            SpeakText(rand)

        elif  ('f***') in message or ('a******') in message:
            rand ='Be polite please'
            SpeakText(rand)

        elif ('your name') in message:
            rand ="I'm Jash. At your service dude!"
            SpeakText(rand)

        elif ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            rand ='We are connected'
            SpeakText(rand)


        elif ('.com') in message :                                                        #VersatileBrowsing
            rand = 'Opening' + message[5:]         
            
            SpeakText(rand)
            mess=message[5:-1]+'m'
            webbrowser.open('http://www.'+mess)
            print ('')
            

        elif ('google maps') in message:                                                  #Maps
            rand='Opening '+message[5: ]
            SpeakText(rand)
            webbrowser.open('http://www.googlemaps.com')

        if ('sleep mode') in message:
            rand = 'good night'
            SpeakText(rand)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        if ('time') in message:
            tim = strftime("%X", localtime())
            rand = tim
            SpeakText(rand)

        if ('joke') in message:
            ques=['What’s the best thing about Switzerland?','Hear about the new restaurant called Karma?']
            ans=['I don’t know, but the flag is a big plus.','There’s no menu: You get what you deserve.' ]
            k=random.randint(0,len(ques)-1)
            rand=ques[k]
            SpeakText(rand)
            time.sleep(1)
            rand=ans[k]
            SpeakText(rand)


        if ('system information') in message :
            rand='Your system information will be shown in a Command Window!'
            SpeakText(rand)
            os.system('cmd /k "systeminfo"')

        if ('games')in message or ('game') in message:
            rand="I can help you to play the following games.."
            SpeakText(rand)
            print('Ant, Bagels, Bounce, Cannon, Connect, Crypto, Fidget, Flappy, Guess, Life, Maze, Memory, Minesweeper, Pacman, Paint, Pong, Simonsays, Snake, Tictactoetiles, Tron')
            time.sleep(2)
            rand='Please enter your choice..'
            SpeakText(rand)
            choice=input(' ')
            chf=choice.lower()
            fin='python -m freegames.'+chf
            os.system(fin)

        if ('what can you do') in message:
            rand="Here's what I can do: "
            SpeakText(rand)
            print('1. Open URL. ')
            print('2. Navigation - Google maps.')
            print('3. Jokes.')
            print('4. Tell you about a person, place and many such things.')
            print('5. Check connection status.')
            print('6. Show system Information.')
            print('7. Play games.')
            print('8. Tell you the time.')
            time.sleep(3)
            
           
          
              
    except sr.RequestError as e:
        print("Oops.. pls check your internet connection and Try Again! ) {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
