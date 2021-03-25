from gtts import gTTS
from playsound import playsound
ibge = gTTS("python é uma linguagem de alto nivel.",lang='pt')
ibge.save('ibge.mp3')
playsound(ibge.mp3)
