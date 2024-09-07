import speech_recognition as SpeechRecognition
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser


engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

recognizer = SpeechRecognition.Recognizer()

def cmd():
    with SpeechRecognition.Microphone() as src:
        print("How Can I Help You?")
        recognizer.adjust_for_ambient_noise(src, duration=0.5)
        print("Ask Me Anything")
        recordAudio = recognizer.listen(src)

    try:
        command = recognizer.recognize_google(recordAudio, language="en_US")
        command = command.lower()
        print("You Said:", command)
        
        if "chrome" in command:
            asis = "Opening Chrome..."
            engine.say(asis)
            engine.runAndWait()
            request = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            subprocess.Popen([request])

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            engine.say("The current time is " + time)
            engine.runAndWait()

        elif "youtube" in command:
            asis = "Opening YouTube..."
            engine.say(asis)
            engine.runAndWait()
            webbrowser.open_new_tab("https://www.youtube.com/")

        elif "play" in command:
            song = command.replace("play", "").strip()
            asis = f"Playing {song} on YouTube"
            engine.say(asis)
            engine.runAndWait()
            pywhatkit.playonyt(song)

        elif "linkedin" in command:
            asis = "Opening LinkedIn..."
            engine.say(asis)
            engine.runAndWait()
            webbrowser.open_new_tab("https://www.linkedin.com/")

        elif "github" in command:
            asis = "Opening GitHub..."
            engine.say(asis)
            engine.runAndWait()
            webbrowser.open_new_tab("https://github.com/")

        elif "amazon" in command:
            asis = "Opening Amazon..."
            engine.say(asis)
            engine.runAndWait()
            webbrowser.open_new_tab("https://www.amazon.com/")

        elif "search" in command:
            search_query = command.replace("search", "").strip()
            asis = f"Searching for {search_query} on Google"
            engine.say(asis)
            engine.runAndWait()
            pywhatkit.search(search_query)

        elif "news" in command:
            asis = "Opening the latest news..."
            engine.say(asis)
            engine.runAndWait()
            webbrowser.open_new_tab("https://news.google.com/")

        elif "weather" in command:
            asis = "Opening the weather forecast..."
            engine.say(asis)
            engine.runAndWait()
            webbrowser.open_new_tab("https://www.weather.com/")

        elif "exit" in command or "stop" in command or "bye" in command:
            asis = "Goodbye!"
            engine.say(asis)
            engine.runAndWait()
            exit()

        else:
            engine.say("Sorry, I didn't understand the command.")
            engine.runAndWait()

    except SpeechRecognition.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except SpeechRecognition.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

while True:
    cmd()
