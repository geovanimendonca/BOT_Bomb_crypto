import cv2, mouse, time, pyautogui
import numpy as np

def main_auto_bomb():
    loop_back = 0
    loop_times = 0
    step = 0
    error_tratment = 0

    while (True):
        if step == 0: # Conectar a carteira - Erro implementado
            time.sleep(0.1)
            verify = verify_screen('conect_wallet')

            if verify[0] == 0:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                error_tratment = 0
                step = 1

            elif error_tratment >= 150:
                step = 8
                error_tratment = 0
                print('erro ao conectar a carteira')

            else:
                error_tratment +=1
                
        elif step == 1: # Assinar a carteira - Erro implementado -
            time.sleep(0.1)
            verify = verify_screen('asign_wallet')

            if verify[0] == 1:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                step = 2
                error_tratment = 0

            elif error_tratment >= 150:
                step = 8
                error_tratment = 0
                print('erro ao assinar a carteira')

            else:
                error_tratment += 1

        elif step == 2: # Entrar no mapa - Erro implementado -
            time.sleep(0.1)
            verify = verify_screen('treasure_hunt')

            if verify[0] == 2:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                step = 3
                error_tratment = 0

            elif error_tratment >= 150:
                step = 8
                error_tratment = 0
                print("erro ao iniciar treasure_hunt")

            else:
                error_tratment += 1
        
        elif step == 3: # Up button apenas - Erro implementado -
            time.sleep(0.1)
            verify = verify_screen('up_button')

            if verify[0] == 3:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                step = 4
                error_tratment = 0

            elif error_tratment >= 150:
                step = 8
                error_tratment = 0
                print("erro ao usar up_button")

            else:
                error_tratment += 1

        elif step == 4: # Heroes apenas - Erro implementado -
            time.sleep(0.1)
            verify = verify_screen('heroes')

            if verify[0] == 4:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                step = 5
                error_tratment = 0

            elif error_tratment >= 150:
                step = 8
                error_tratment = 0
                print("erro ao clicar em heroes")

            else:
                error_tratment += 1

        elif step == 5: # Colocar todos pra trabalhar menos lendario - Erro implementado -
            time.sleep(0.1)
            verify = verify_screen('work_all')

            if verify[0] == 5:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(2)
                mouse.click(button='left')
                mouse.move(50,50,absolute=False)
                time.sleep(7)

                for x in range(32):
                    mouse.wheel(delta=-200)
                    time.sleep(0.01)

                time.sleep(1.5)
                mouse.click(button='left')
                step = 6
                error_tratment = 0

            elif error_tratment >= 150:
                step = 8
                error_tratment = 0
                print("erro ao colocar todos para trabalhar")

            else:
                error_tratment += 1

        elif step == 6: # Fecha a tela de herois e clica na tela pra trabalhar - Erro implementado -
            time.sleep(0.1)
            verify = verify_screen('close_button')

            if verify[0] == 6:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                time.sleep(1)
                mouse.click(button='left')
                step = 7
                error_tratment = 0

            elif error_tratment >= 150:
                step = 8
                error_tratment = 0
                print("erro ao fechar a tela de herois")

            else:
                error_tratment += 1

        elif step == 7: # Volta e entra no mapa para evitar bugs - Erro implementado -
            verify = verify_screen('back_button')
            loop_back +=1
            time.sleep(1)

            if loop_back == 30 or loop_back == 60 or loop_back == 90 or loop_back == 120 or loop_back == 150:
                mouse.click(button='left')

            if verify[0] == 7 and loop_back >= 180:
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                time.sleep(1)
                verify = verify_screen('treasure_hunt')
                mouse.move((verify[1]+verify[2])/2,(verify[3]+verify[4])/2)
                time.sleep(1)
                mouse.click(button='left')
                time.sleep(1)
                loop_back = 0
                loop_times += 1
                error_tratment = 0

            elif loop_back >= 180:
                error_tratment += 1

            if loop_times >= 8:
                step = 8
                loop_times = 0
                error_tratment = 0

            if error_tratment >= 30:
                step = 8
                print("erro ao ir e voltar do mapa")
        
        elif step == 8: # Reinicia o game
            error_tratment = 0 # redundancia
            mouse.move(83,50)
            mouse.click('left')
            print('pagina recarregada')
            step = 0
                
def verify_screen(key):
    image = pyautogui.screenshot() # Take a printscreen
    image = np.array(image) # Transform in array
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = cv2.matchTemplate(image, templates[key], cv2.TM_CCOEFF_NORMED) # Match the tamplate with the screenshot
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result) # Get the contours
    (startX, startY) = maxLoc # Get the best contours
    endX = startX + templates[key].shape[1]
    endY = startY + templates[key].shape[0]
    verified = [-1,0,0,0,0]

    if key == 'conect_wallet' and maxVal > 0.9:
        verified = [0, startX, endX, startY, endY]
        
    elif key == 'asign_wallet' and maxVal > 0.9:
        verified = [1, startX, endX, startY, endY]

    elif key == 'treasure_hunt' and maxVal > 0.9:
        verified = [2, startX, endX, startY, endY]

    elif key == 'up_button' and maxVal > 0.7:
        verified = [3, startX, endX, startY, endY]

    elif key == 'heroes' and maxVal > 0.9:
        verified = [4, startX, endX, startY, endY]

    elif key == 'work_all' and maxVal > 0.9:
        verified = [5, startX, endX, startY, endY]

    elif key == 'close_button' and maxVal > 0.9:
        verified = [6, startX, endX, startY, endY]

    elif key == 'back_button' and maxVal > 0.9:
        verified = [7, startX, endX, startY, endY]

    elif key == 'ok_button' and maxVal > 0.9:
        verified = [8, startX, endX, startY, endY]

    return verified


templates = {'conect_wallet': cv2.imread("templates/conect_wallet.png"),
                    'asign_wallet' : cv2.imread("templates/assinar_wallet.png"),
                    'treasure_hunt': cv2.imread("templates/treasure_hunt.png"),
                    'back_button' : cv2.imread("templates/back_button.png"),
                    'close_button' : cv2.imread("templates/close_button.png"),
                    'heroes' : cv2.imread("templates/heroes.png"),
                    'rest_all' : cv2.imread("templates/rest_all.png"),
                    'work_all' : cv2.imread("templates/work_all.png"),
                    'up_button' : cv2.imread("templates/up_button.png"),
                    'ok_button' : cv2.imread("templates/ok.png") #(573, 497)          
     }

if __name__ == '__main__':
    main_auto_bomb()
