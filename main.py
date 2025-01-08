import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from tkinter import PhotoImage, scrolledtext
import threading
from apikey import api_data
import time
import PIL
import google.generativeai as genai
print(dir(genai))
# Check available models
# Check and print available models





GENAI_API_KEY = api_data

print("API Key:", GENAI_API_KEY)
genai.configure(api_key=GENAI_API_KEY)


genai.configure(api_key=GENAI_API_KEY)

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen_to_command(): 
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        conversation_area.insert(tk.END,"Listening...\n\n")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source,timeout=5, phrase_time_limit=10)
            query = recognizer.recognize_google(audio,language = 'en-in').lower()
            conversation_area.insert(tk.END,f"You: {query}\n")
            return query
        except sr.UnknownValueError:
            conversation_area.insert(tk.END,"Jarvis: Sorry, I didn't catch that. Please try again.\n")
            speak("sorry, I didn't catch that plz repeat")
            return "none"
        except sr.RequestError:
            conversation_area.insert(tk.END,"Jarvis: Sorry, I'm having trouble understanding you. Please check your connection")
            speak("sorry, I'm having trouble understanding you. Please check your connection")
            return "none"
        except Exception as e:
            conversation_area.insert(tk.END,f"Jarvis: Error: {e}\n")
            speak("Sorry I encountered an error.")
            return "none"
        
def generate_response(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query, generation_config = genai.GenerationConfig(
            max_output_tokens=75,
            temperature = 0.1,))
        print("\n")
        return response.text
    except Exception as e:
        return f"sorry, I encountered an error: {e}"

    
stop_conversation = False  

def handel_conversation():
    global stop_conversation
    while not stop_conversation:
        query = listen_to_command()
        if query == "none":
            continue
        
        if "bye" in query or "goodbye" in query:
            conversation_area.insert(tk.END, "Jarvis: Goodbye! have a great day!\n")
            speak("Goodbye! Have a great day!")
            break
        
        response = generate_response(query)
        conversation_area.insert(tk.END, f"Jarvis: {response}\n")
        speak(response)

def start_conversation():
    global stop_conversation
    stop_conversation = False
    conversation_thread = threading.Thread(target=handel_conversation)
    conversation_thread.daemon  = True
    conversation_thread.start()
    conversation_area.insert(tk.END,"Hi i am Jarvis How can i Help you?\n\n")
    conversation_area.see(tk.END)
    speak("Hi, i am Jarvis How can i help you")

def end_converstaion():
    global stop_conversation
    stop_conversation = True
    conversation_area.insert(tk.END,"jarvis: Conversation Ended manually. Goodbye!\n")
    speak("converstaion ended manually good bye!") 
    root.quit()
       
root = tk.Tk()
root.title("J-A-R-V-I-S")

#image = PhotoImage(file="C:\\Users\\sumit\\Downloads\\pngwing.com (1).png")

# Create a label to hold the image
#image_label = tk.Label(root, image=image)
#image_label.pack(padx=5, pady=5)
from tkinter import PhotoImage

# For a GIF background, use the PhotoImage class
background_photo = PhotoImage(file="C:\\Users\\sumit\\Downloads\\QNBH.gif")

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

conversation_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 50, height= 20,font ={"Arial",12})
conversation_area.pack(padx= 10, pady=10) 

start_button = tk.Button(root, text="Start conversation",font={"Arial",12},command=start_conversation)
start_button.pack(pady=5)

end_button = tk.Button(root, text="End conversation", font={"Arial",12},command=end_converstaion)
end_button.pack(pady=5)

root.mainloop()