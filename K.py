import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit 
##import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180 )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("welcome back,  i am k 2point o. how may i help u")       

def music():
    speak("sure sir ,tell me the name of the song!")
    musicName = takeCommand()
    if 'Besabriyaan' in musicName:
        os.startfile('D:\GENZ songs\Besabriyaan')
    else:
        pywhatkit.playonyt(musicName)
        speak("playing")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



 
    
if __name__ == "__main__":
#working function
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'youtube search' in query:
            speak("ok sir this what i found")
            query=query.replace("k","")
            query=query.replace("youtube search","")
            web="https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            speak("done sir!")
        
        elif 'spotify search' in query:
            speak("ok sir this what i found")
            query=query.replace("k","")
            query=query.replace("spotify search","")
            web="https://open.spotify.com/search/" + query
            webbrowser.open(web)
            speak("done sir!")    
        
        elif 'open spotify' in query:
            speak("opening spotify ")
            webbrowser.open("https://open.spotify.com/playlist/3aWdiWXe6jDcL14uCEqqdW")

        elif 'search' in query:
            speak("this is what i found")
            query=query.replace("k","")
            query=query.replace("search","")
            query=query.replace("for","")
            pywhatkit.search(query)
            speak("done sir")
            

        elif 'open stack overflow' in query:
            speak("opening stackoverflow ")
            webbrowser.open("https://stackoverflow.com/")   
        
        elif 'open github' in query:
            speak("opening Hub ")
            webbrowser.open("https://github.com/") 
        
        elif 'open insta' in query:
            speak("opening instaa ")
            webbrowser.open("https://www.instagram.com/")       

        elif 'open calculator' in query:
            speak("opening calc ")
            webbrowser.open("http://calculator.com/")
        elif 'who are you' in query:
            myself=('my name is k ,a virtual assistant specially made for k to reduce his burden')
            speak(myself)    
        
        elif 'play slow songs' in query:
            speak("playing lofi songs ")
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play volume 1' in query:
            speak("playing Genzy songs ")
            music_dir = 'D:\GENZ songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))    
                

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'date' in query:
            date = datetime.datetime.now()  
            speak(f"Sir, todays date is {date}") 
            print({date})   

        elif 'open code' in query:
            speak("opening your console")
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
 
        
        elif 'what the hell are you doing'in query:
            sorry=('sorry sir i dont whats going on')
            speak(sorry)        
        
        elif 'open powerpoint' in query:
           speak("opening powerpoint") 
           codePath=("https://www.office.com/launch/powerpoint")
           os.startfile(codePath)
           
        elif 'music'in query:
            music()
               
        elif 'wikipedia'in query:
            speak("searching wikipedia...")
            query=query.replace("k","")
            query=query.replace("wikipedia","")
            wiki =wikipedia.summary(query)   
           
           
#chatbot module 
        
        #want to add voice chatbot feature  
    

     
