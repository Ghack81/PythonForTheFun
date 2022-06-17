import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK...")
    audio = r.listen(source)
print(r.recognize_google (audio))

# Verify import speech_recognition