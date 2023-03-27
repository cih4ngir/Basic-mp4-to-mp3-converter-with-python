# you have to install moviepy library with "!pip install moviepy".
from moviepy.editor import *

mp4_files = r'D:\basiconverter\mp4\1974.mp4'
mp3_files = r'D:\basiconverter\mp3\1974.mp3'

videoclip = VideoFileClip(mp4_files)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_files)
audioclip.close()
videoclip.close()
