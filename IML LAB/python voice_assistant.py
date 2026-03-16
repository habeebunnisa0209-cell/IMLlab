import whisper
import pyaudio
import wave
import os
import pyautogui
import pyttsx3

# -------------------- INITIALIZATION --------------------

# Load Whisper model (use "small" or "medium" for higher accuracy)
model = whisper.load_model("base")

engine = pyttsx3.init()
engine.setProperty("rate", 170)

# -------------------- TEXT TO SPEECH --------------------

def speak(text):
    engine.say(text)
    engine.runAndWait()

# -------------------- AUDIO RECORDING --------------------

def record_audio(filename="input.wav", duration=5):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 16000

    audio = pyaudio.PyAudio()
    stream = audio.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("🎙️ Listening...")
    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b"".join(frames))

# -------------------- SPEECH TO TEXT --------------------

def recognize_command():
    filename = "input.wav"
    record_audio(filename)
    result = model.transcribe(filename)
    command = result["text"].lower().strip()
    print("🧠 Recognized:", command)

    os.remove(filename)  # delete after use
    return command

# -------------------- COMMAND EXECUTION --------------------

def execute_command(command):

    if "open chrome" in command:
        speak("Opening Google Chrome")
        os.system("start chrome")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "close window" in command:
        speak("Closing the current window")
        pyautogui.hotkey("alt", "f4")

    elif "increase volume" in command:
        speak("Increasing volume")
        pyautogui.press("volumeup")

    elif "decrease volume" in command:
        speak("Decreasing volume")
        pyautogui.press("volumedown")

    elif "mute volume" in command:
        speak("Muting volume")
        pyautogui.press("volumemute")

    elif "shutdown system" in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 5")

    elif "restart system" in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 5")

    elif "exit" in command or "stop assistant" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Sorry, I did not understand that command")

# -------------------- MAIN LOOP --------------------

def main():
    speak("Voice assistant started. Please say a command.")

    while True:
        try:
            command = recognize_command()
            execute_command(command)
        except Exception as e:
            print("Error:", e)
            speak("An error occurred. Please try again.")

# -------------------- START --------------------

if __name__ == "__main__":
    main()
