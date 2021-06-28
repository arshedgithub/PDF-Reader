import pyttsx3

name = input("Enter your Name : ")

friend = pyttsx3.init()
friend.say(f"Hi {name}, i'm david")
friend.runAndWait()

while True:
    speach = "Type something : "

    friend.say(speach)
    friend.runAndWait()

    c = input(speach)
    friend.say(c)
    friend.runAndWait()

    if input("Do you want to Quit ? Y/N \n") == 'y' or 'Y':
        friend.say("good bye, see you later")
        friend.runAndWait()
        break
