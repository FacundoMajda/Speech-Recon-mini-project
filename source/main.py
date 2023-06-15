#-----------------------------------------------------
# ASISTENTE VIRTUAL POR VOZ
# IPF
# 2023 - FORMOSA, ARGENTINA
#-----------------------------------------------------

#use google speech recognition to this project
#most accesible tool of this type. Free public api 




import pyttsx3
import time
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()


#Speech Module
class SpeechModule:
    def __init__(self, voice=0, volume=1, rate=120):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice].id)
        
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


#Voice recognition module
class VoiceRecognitionModule:
    def __init__(self, key=None):
        #aqui va la key de la API de google speech recognition
        self.key = key
        self.r = sr.Recognizer()
    
    def recognize(self):
        with sr.Microphone() as source:
            print("Di algo ahora! :")
        audio = self.r.listen(source)
        try: 
            text = self.r.recognize_google(audio,key=self, language="es") 
            return text 
        except: 
              return None

speech= SpeechModule()
text= VoiceRecognitionModule()


while True:
    text = recognition.recognize()
    if text:
        chatbot_text = chatbot.talk(text)
        speech.talk(chatbot_text)
    else:
        speech.talk("No te he entendido")
    time.sleep(1)