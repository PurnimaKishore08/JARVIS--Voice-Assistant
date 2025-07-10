# 📦 Import necessary libraries
import streamlit as st                       # Web UI framework
import speech_recognition as sr              # For capturing speech
import pyttsx3                               # For converting text to speech
import os                                    # For accessing local files
import datetime                              # To get current time
import smtplib                               # For sending emails
import webbrowser                            # To open URLs in browser

# 🔊 Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)     # Use female voice

# 💬 Speak function to vocalize JARVIS response
def speak(text):
    st.info(f"JARVIS: {text}")                # Show response on UI
    engine.say(text)
    engine.runAndWait()

# 🎙️ Function to take voice command from mic
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.warning("🎤 Listening...")          # Status on UI
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')  # Convert speech to text
        st.success(f"🗣️ You said: {query}")    # Show user's input
        return query.lower()
    except Exception as e:
        st.error("❌ Sorry, I didn't catch that.")
        return "none"

# 📧 Send email using SMTP
def send_email(to, content):
    sender = "purnimakishore003@gmail.com"           # Your email
    password = "hybr ikut tavc vddj"            # Gmail App Password only!
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP setup
    server.starttls()                         # Start secure TLS connection
    server.login(sender, password)            # Login to email account
    server.sendmail(sender, to, content)      # Send the message
    server.quit()

# 🙋‍♂️ Greet user based on current time
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS. How can I help you today?")

# 🖥️ Streamlit Web Interface
st.set_page_config(page_title="JARVIS Assistant", page_icon="🤖")
st.title("🤖 JARVIS - Your Personal Voice Assistant")
st.markdown("This is a Python-based voice assistant with a simple web interface.")

# 🎯 When button is clicked, JARVIS starts listening
if st.button("🎙 Start Listening"):
    wish_user()
    query = take_command()

    # 🧠 Command Processing Block
    if 'open youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google.")

    elif 'open vs code' in query:
        try:
            os.startfile("C:\Users\Kishore\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            speak("Opening Visual Studio Code.")
        except Exception:
            speak("Couldn't find VS Code path.")

    elif 'open microsoft edge' in query:
        try:
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            speak("Opening Microsoft Edge.")
        except Exception:
            speak("Couldn't find Microsoft Edge path.")


    elif 'send email' in query:
        speak("What should I say?")
        content = take_command()
        to = "purnimakishore2003@gmail.com"             # Change to real recipient
        try:
            send_email(to, content)
            speak("Email has been sent.")
        except Exception as e:
            speak("Failed to send email.")
            st.error(str(e))

    elif 'exit' in query or 'Shut down' in query:
        speak("Shutting down JARVIS. Goodbye!")

    else:
        speak("I can only help with basic tasks like opening apps and sending email.")
