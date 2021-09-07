from gtts import gTTS
from playsound import playsound

language = 'de'
tts = gTTS(text=input('Was soll der text sein?: '),
           lang=language,
           slow=False)
tts.save("tts.mp3")
playsound("tts.mp3")

input("Press any key to terminate the program")