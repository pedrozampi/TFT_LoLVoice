
import speech_recognition as sr
import pyautogui as ag


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga algo!")
    audio = r.listen(source)

txt = r.recognize_google(audio, language='pt-BR')

def ouvindo():
    with sr.Microphone() as source:
        print("Diga algo")
        audio = r.listen(source)
    txt = r.recognize_google(audio)
    return audio


while txt != 'encerrar':
    try:
        if(txt=='posição'):
            mouse = ag.position()
            print(mouse)
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='projétil'):
            ag.press('Q')
            print('Q')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='w'):
            ag.press('W')
            print('W')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='curar'):
            ag.press('E')
            print('E')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='r'):
            ag.click(957,1022)
            print('Ultou')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='exaustão'):
            ag.press('D')
            print('D')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='incendiar'):
            ag.press('F')
            print('F')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='loja'):
            ag.press('P')
            print('Loja')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='menu'):
            ag.press('Esc')
            print('EscQQ')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        else:
            print(txt)
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
            print('repita por favor, eu entendi ' +txt)


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
