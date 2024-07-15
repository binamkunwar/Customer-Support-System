import os
import speech_recognition as sr

def handle_user_input(input_data, is_audio=False):
    if is_audio:
        audio_file_path = "./audio.m4a"
        print(f"Looking for audio file at: {audio_file_path}")
        if not os.path.exists(audio_file_path):
            print(f"File does not exist: {audio_file_path}")
            return
        try:
            text = recognize_speech_from_audio(audio_file_path)
            return text
        except ValueError as e:
            print(f"Error: {e}")
            return "Audio file could not be processed."
    # ... rest of the function ...

def recognize_speech_from_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    return text

if __name__ == "__main__":
    audio_input = "./audio.m4a"
    print(handle_user_input(audio_input, is_audio=True))
