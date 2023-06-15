#-----------------------------------------------------
# ASISTENTE VIRTUAL POR VOZ
# Facundo Majda - IPF
# 2023 - FORMOSA, ARGENTINA
#stormbreaker
#-----------------------------------------------------




#module text to speech here.
import pyttsx3
engine = pyttsx3.init()
engine.say("Hola usuario, soy un modelo de reconocimiento de voz a tiempo real, por favor habla e intentaré responder")
engine.runAndWait()


#use google speech recognition to this project
#most accesible tool of this type. Free public api 
 
import speech_recognition as sr

r=sr.speech()

with sr.Microphone() as source:
    print("Hola, soy un modelo de reconocimiento de voz a tiempo real, por favor habla e intentaré responder")
    audio = r.listen(source)
    try: 
        text = r.recognize_google(audio, language="es") 
        print(text) 
    except: 
     print("Usuario, no te he entendido, por favor vuelve a hablar")







class SpeechModule:
   def __init__(self, voice= 0, volume=1, rate=125):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
                
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice].id)
        
        
def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()



class VoiceRecognitionModule:
    def __init__(self) -> None:
        pass

