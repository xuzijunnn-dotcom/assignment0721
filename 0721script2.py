import os
import random
import time
import pygame
pygame.mixer.init()
clip_folder = "/Users/xuzijun/Desktop/Working/new_audio_files"
clip_files = os.listdir(clip_folder)
random.shuffle(clip_files)

for audio in clip_files:
    fullpath = os.path.join(clip_folder, audio)
    print (f"playing: {audio}")
    pygame.mixer.music.load(fullpath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)
    print("finished, 5 sec pausing")
    time.sleep(5)
print ("bingo!")
