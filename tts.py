from aip import AipSpeech
import time
import pygame
# import os
# import mp3play

# def speaker(path):
#     clip = mp3play.load(path)
#     clip.play()
#     clip.stop()

APP_ID = '15220687'
API_KEY = 'HZffI2RvXSp7H29n6bXo98YW'
SECRET_KEY = 'Dqg1iIt04WBWPSGpmSerPQu0xC6t7rqy'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('空调已经打开，温度合适吗？', 'zh', 1, {
    'vol': 5,
})

if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)

pygame.mixer.init()
track = pygame.mixer.music.load('audio.mp3')
clock = pygame.time.Clock()
pygame.mixer.music.play()
time.sleep(4)
pygame.mixer.music.stop()

# p = vlc.MediaPlayer("audio.mp3")
# p.play()
# os.system('audio.mp3')

# speaker('audio.mp3')