
import speech_recognition as sr
import pyautogui as ag

from playsound import playsound
def somBuy():
    buySound = 'D:\Projetos\VCTFT\sbuy.mp3'
    playsound(buySound)

def somXP():
    xpSound = 'D:\Projetos\VCTFT\sxp.mp3'
    playsound(xpSound)


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

heroi1 = '430, 789'

while txt != 'encerrar':
    try:
        if(txt=='posição'):
            mouse = ag.position()
            print(mouse)
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='comprar um'):
            ag.dragTo(557, 1003)
            print('Carta 1 comprada')
            somBuy()
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='comprar 2'):
            ag.dragTo(775,978)
            print('Carta 2 comprada')
            somBuy()
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='comprar 3'):
            ag.dragTo(989,989)
            print('Carta 3 comprada')
            somBuy()
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='comprar 4'):
            ag.dragTo(1202,989)
            print('Carta 4 comprada')
            somBuy()
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='comprar 5'):
            ag.dragTo(1407,989)
            print('Carta 5 comprada')
            somBuy()
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='comprar XP'):
            ag.dragTo(337,953)
            print('Xp comprada')
            somXP()
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='atualizar'):
            ag.dragTo(342,1028)
            print('Loja atualizada')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        #elif(txt=='herói um'):
        #    ag.dragTo(430,789)
        #    print('Loja atualizada')
        #    audio2 = ouvindo()
        #    txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt[0:5]=='herói'):
            if(txt[7:12]=='para' or txt[9:13]=='para'):
                print('movimento')
                if(txt[6]=='1' or txt[6:7]=='um'):
                    ag.dragTo(430,789)
            print(txt)
            print(txt[8:12])
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='herói 2'):
            ag.dragTo(550,789)
            print('Loja atualizada')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='herói 3'):
            ag.dragTo(773,789)
            print('Loja atualizada')
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
        elif(txt=='encerrar'):
            print('Tchau!')
            quit()
        else:
            print(txt)
            audio2 = ouvindo()
            txt = r.recognize_google(audio2, language='pt-BR')
            print('repita por favor, eu entendi ' +txt)


    except sr.UnknownValueError:
        print("Google Speech Recognition não te entendeu.")
    except sr.RequestError as e:
        print("Não pode requisitar respostas do serviço Google Speech Recognition; {0}".format(e))
