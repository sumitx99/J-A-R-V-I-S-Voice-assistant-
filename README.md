# J-A-R-V-I-S (Voice Assistant) 🤖

J-A-R-V-I-S is a simple voice assistant application that allows you to interact with an AI-powered backend and perform a range of tasks via voice commands. Built using Python, the assistant listens to your commands, processes them, and responds with appropriate feedback. This project includes features like text-to-speech, speech recognition, and AI-powered responses. 🗣️💬

---

## Features 🌟

- **Speech Recognition** 🎙️: Convert spoken words into text using the Google Speech Recognition API.
- **AI Response** 🤖: Powered by Google Gemini AI API for generating intelligent responses.
- **Text-to-Speech** 🗣️🔊: Use pyttsx3 to convert text responses back to speech.
- **Conversation Interface** 🖥️: The GUI allows for easy interaction, displaying the conversation with the assistant.

---

## Requirements 📝

Before running the program, ensure you have Python 3.x installed along with the following libraries:

- `google-generativeai`: For generating AI responses.
- `pyttsx3`: For text-to-speech functionality.
- `speech_recognition`: For speech-to-text conversion.
- `tkinter`: For creating the GUI interface.
- `pillow`: For handling images (if using custom background images).

You can install the dependencies using pip:

```bash
pip install google-generativeai, pyttsx3, SpeechRecognition, pillow, tkinter
 ```
 
## Setup Instructions ⚙️
1. Add API Key 🔑

```bash
api_data = "YOUR_API_KEY"
 ```
2. Run the Program 🚀
- Run the main.py script to start the application:
```bash
python main.py
 ```
The Tkinter GUI will open, and you can start interacting with the assistant using voice commands. Click the Start conversation button to begin, and the assistant will listen for commands and generate responses.


## How It Works 🔍
- Listening for Commands 👂: The assistant listens to your voice through a microphone. If it detects speech, it converts it to text using the Google Speech Recognition API.
- Generating Response 🤔: The text is sent to the Gemini AI API, which processes the input and generates an appropriate response.
- Text-to-Speech 🗣️: The generated response is read out loud using the pyttsx3 library.
- Conversation Window 💬: A Tkinter window displays the ongoing conversation with the assistant.

## Troubleshooting 🛠️
- API Key Error: Ensure your API key is correctly placed in the apikey.py file and that it has the necessary permissions to access the Gemini API.
- Speech Recognition Issues: Make sure the microphone is connected and accessible. Check your internet connection if the speech recognition service fails.
- GUI Display: If the Tkinter window doesn’t display correctly, ensure you have the necessary GUI libraries installed.



## License 📜

This project is open-source and available under the MIT License. See the [license](https://github.com/sumitx99/J-A-R-V-I-S-Voice-assistant-/blob/main/LICENSE) file for more details.

## Contributing 🤝
Feel free to contribute by creating issues or submitting pull requests. Make sure to follow the guidelines for contributing.




