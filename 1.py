
import pyttsx3

print("Welcome to Robospeaker")

E = pyttsx3.init()

while True:
    X = input("What do you want me to say? (Type 'exit' to quit): ")
    if X.lower() == "exit":
        break
    E.say(X)
    E.runAndWait()
