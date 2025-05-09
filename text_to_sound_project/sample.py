from gtts import gTTS

tts = gTTS(text="안녕하세요", lang='ko')
tts.save("hello.mp3")
