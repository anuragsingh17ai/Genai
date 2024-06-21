import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
print("Let's speak!!")

with sr.Microphone() as source:
    # clear background noise
    r.adjust_for_ambient_noise(source, duration=0.3)
    
    print("Speak now")
    # capture the audio
    audio = r.listen(source)
    
    text = r.recognize_google(audio)
    print("Speaker:", text)
