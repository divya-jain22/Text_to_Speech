# Here in this code file , the text to speech is being implemented using GTTS module
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can generate spoken audio from written text.
# To play the converted audio
import os

# The text that you want to convert to audio
text = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# demo 
myobj.save("demo.mp3")

# Playing the converted file
os.system("mpg321 demo.mp3")
