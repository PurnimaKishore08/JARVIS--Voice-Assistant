# JARVIS Assistant (Offline Only: Voice + Email + Commands)

import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import webbrowser
import os

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, Please say again.")
        return "none"

# Function to send email
def send_email(to, content):
    # Replace with your own email credentials
    your_email = "purnimakishore003@gmail.com"
    your_password = "rzfr ghvd kxdd fchb"
    
    # Setup SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS for security
    server.login(your_email, your_password)  # Login to email account
    server.sendmail(your_email, to, content)  # Send the email
    server.quit()
    

# Greeting function
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS. How can I help you today?")

if __name__ == "__main__":
    wish_user()
    while True:
        query = take_command()

        if query == "none":
            continue

        elif 'exit' in query or 'stop' in query:
            speak("Shutting down. Goodbye!")
            break

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open vs code' in query:
            os.startfile("C:\\Users\\Kishore\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Kishore\\Music'  # Adjust path
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

# Send an email
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()  # Take email content
                to = "vpal22962@gmail.com"  # Change to receiver email
                send_email(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
        else:
            speak("I can only help with voice commands, email, and launching apps right now.")
