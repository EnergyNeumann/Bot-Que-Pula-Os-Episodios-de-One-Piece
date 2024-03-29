#Bot para pular os episódios de one piece e os minutos iniciais
#Código de autoria do Richard Neumann - EnergyNeumann: https://github.com/EnergyNeumann
import pyautogui
import time

pyautogui.FAILSAFE = True #FailSafe, para que se caso algo der errado, basta vc arrastar o cursor do mouse para a quina da tela

contador = 0
# time.sleep(1080)

while contador < 10: #colocar quantos episódios deseja pular (basta alterar o número 10 pela quantidade de episódios que deseja assistir)
    try:
        x1, y1=pyautogui.center(pyautogui.locateOnScreen("onepiece.png", confidence=0.7)) 
        time.sleep(1)
        pyautogui.moveTo(x1,y1)
        print('Pulando o episódio...')
        pyautogui.moveTo(x1, y1)
        pyautogui.click(x=70, y=1017)
        time.sleep(3)
        pyautogui.click(x=260, y=1047)
        contador += 1
        time.sleep(1080)
    except:
        print(f'Ainda não é hora de pular... espere mais 5 segundos')
        time.sleep(5)