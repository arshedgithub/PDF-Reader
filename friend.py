import pyttsx3

name = input("Enter your Name : ")

friend = pyttsx3.init()
friend.say(f"Hi {name}, i'm david, How can I help you?")
friend.runAndWait()

options = "Enter 1 for read pdf : "
friend.say(options)
friend.runAndWait()
input(options)

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
