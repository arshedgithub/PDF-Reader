import pyttsx3
import functions


name = input("Enter your Name : ")

speaker = pyttsx3.init()
speaker.say(f"Hi {name}, i'm alpha the computer, Enter the file name to read")
speaker.runAndWait()


while True:
    file_name = input("Enter the File Name : ")
    functions.getFile(file_name)

    if input("Do you want to Quit ? Y/N \n") == 'y' or 'Y':
        speaker.say("good bye, see you later")
        speaker.runAndWait()
        break
