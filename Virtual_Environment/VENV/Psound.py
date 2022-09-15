import vlc
import time

sound_file= vlc.MediaPlayer("/home/user/Downloads/mixkit-flock-of-wild-geese-20.wav")
sound_file.play()
time.sleep(10)
