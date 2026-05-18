import edge_tts
import asyncio
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

VOICE = "en-US-ChristopherNeural" # A friendly, professional, and very realistic male voice

async def _generate_audio(text, output_file="response.mp3"):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

def speak(text):
    print(f"Jarvis: {text}")
    try:
        # Run the async edge-tts generation synchronously
        asyncio.run(_generate_audio(text))
        
        # Play the audio using pygame
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
        
        # Wait until the audio is finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(f"Error speaking: {e}")
    finally:
        # Clean up the file if possible
        pygame.mixer.music.unload()
        if os.path.exists("response.mp3"):
            try:
                os.remove("response.mp3")
            except:
                pass

if __name__ == "__main__":
    speak("Hello sir, I am Jarvis. How can I help you today?")
