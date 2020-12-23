import speech_recognition as sr

r=sr.Recognizer()
r1=sr.Microphone(device_index=3)

with r as source:
    print("listening")
    r.adjust_for_ambient_noise(source)
    audio =r.listen(source)
    r.recognize_google(audio)