from gtts import gTTS
import os

# Function to convert text to speech and save as an audio file
def text_to_speech(text, filename):
    try:
        tts = gTTS(text)
        tts.save(filename)
        print(f"Text converted to speech and saved as '{filename}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Input text
input_text = "Hello, this is a text-to-speech converter example."

# Output audio file name
output_file = "output.mp3"

# Convert the text to speech and save it as an audio file
text_to_speech(input_text, output_file)

# Play the generated audio (optional)
os.system(f"mpg123 {output_file}")  # You may need to install mpg123 for this to work 
