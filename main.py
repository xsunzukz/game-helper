import time
from pynput import keyboard
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load your music file
music_file = 'calm down.mp3'
pygame.mixer.music.load(music_file)

# Setting
threshold = 200  # Number of key presses per minute to trigger music
time_frame = 60  # Time frame in seconds to count key presses
cooldown_time = 30  # Cooldown time in seconds

key_press_count = 0
start_time = time.time()
last_played_time = 0

def on_press(key):
    global key_press_count, start_time, last_played_time
    
    current_time = time.time()
    elapsed_time = current_time - start_time
    time_since_last_play = current_time - last_played_time

    if elapsed_time > time_frame:
        key_press_count = 0
        start_time = current_time

    key_press_count += 1

    if key_press_count > threshold and time_since_last_play > cooldown_time:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            last_played_time = current_time

def on_release(key):
    # Stop listener if needed
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
