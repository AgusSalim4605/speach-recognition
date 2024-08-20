import pyttsx3 as tts
import speech_recognition as sr

engine = tts.init()

# mengatur kecepatan suara
rate = engine.getProperty('rate')                 
engine.setProperty('rate', 180)     # mengatur kecepatan berbicara

# mengganti suara
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female o for male

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("hello, i am your virtual assistant")

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.energy_threshold = 10000
    recognizer.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    print(text)