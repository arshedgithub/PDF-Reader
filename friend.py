import pyttsx3

name = input("Enter your Name : ")

friend = pyttsx3.init()
friend.say(f"Hi {name}, i'm david")
friend.runAndWait()

while True:
    friend.say("Type something")
    friend.runAndWait()

    c = input("Type something : ")
    friend.say(c)
    friend.runAndWait()

    if input("Do you want to Quit ? Y/N ") == 'y':
        friend.say("good bye, see you later")
        friend.runAndWait()
        break
