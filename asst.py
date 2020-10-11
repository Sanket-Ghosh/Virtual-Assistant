import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',200)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.1)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir!')
    elif hour>=12 and hour<=18:
        speak('Good Afternoon Sir!')
    else:
        speak('Good Evening Sir!')

    speak('I am Bozo at your service! Please tell me, How may I help you?')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")

    except Exception as e:
        #print(e)
        speak('Say that again please!!')
        return "None"
    return query

#def sendEmail(to,content):





if __name__ == '__main__':
    
    wishme()
    while True:
            query =takecommand().lower()

            #logic for tasks
            if 'wikipedia' in query:
                speak('Searching Wikipedia')
                query = query.replace('wikipedia',"")
                results = wikipedia.summary(query, sentences=2)
                speak('Accoeding to Wikipedia')
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open facebook' in query:
                webbrowser.open("facebook.com")

            elif 'play music' in query:
                music_dir = "D:\\Music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif 'the time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir! the time is {strtime}")

            elif 'send email to sanket' in query:
                try:
                    speak('what should I say?')
                    content = takecommand()
                    to = "sanketghosh033@gmail.com"
                    sendEmail(to, content)
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir! Unable to send the email")

            elif 'quit' in query:
                exit()
