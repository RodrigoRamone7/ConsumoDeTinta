import pyautogui as ag
import pygetwindow as gw
import pytesseract as pyt
import cv2
from dados import gravarDados

print(input(f'COLETA DE DADOS DE CONSUMO DE TINTA \n Por favor siga as seguintes instruções: \n 1 - Verifique se a maquina está ligada \n 2 - Certifique-se de que a maquina não está imprimindo nada \n Para continuar pressiona ENTER'))

pyt.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

def ripwin(): #Valida se a janela está aberta
    window_true = None
    janelas = []
    janelas += gw.getAllTitles()
    
    tittle = 'RasterLinkPro5IP' #Título a ser encontrado
    
    for valid in janelas: #Valida se o raster link está aberta
        if tittle in valid:
            window_true = valid
            break
    if window_true: # Se a janela estiver aberta vai abrir e redimencionar
        rasterlinkwindow = gw.getWindowsWithTitle(window_true)[0]
        rasterlinkwindow.minimize()
        rasterlinkwindow.maximize()
        rasterlinkwindow.moveTo(0,0)
        rasterlinkwindow.resizeTo(800, 800)
        
            
    else: #Mensagem de erro caso o RIP não esteja aberto
        ag.alert(text='Abra o programa de RIP e aguarde sua inicialização', title='ERRO!', button='OK')
        alertwindow = gw.getActiveWindow()
        alertwindow.activate()
        moveto()
        return False
    
    return True

def moveto(): #Sequencia de ações para encontrar níveis de tinta
    if ripwin() == True: # A janela do RIP deve estar no monitor principal
        ag.moveTo(170,115)
        ag.click()
        ag.moveTo(580,150)
        ag.click()
        ag.moveTo(700,420)
        ag.click()
        return True
        
def capture(): #Captura Screenshot dos níveis de tinta
    if moveto() == True:
        img = ag.screenshot('ss.png',region=(544,211, 230, 169),)
        
        
def reading(): #Leitura de dados da imagem
    capture()
    img = cv2.imread('ss.png')
    def capPoncentagem(x,y,width,height): #Captura de dados de porcentagem
        x, y, width, height = x, y, width, height #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        (h, w) = roi.shape[:2]
        roire = cv2.resize(roi, (w*3,h*3))
        gray_roi = cv2.cvtColor(roire, cv2.COLOR_BGR2GRAY)
        ret,thr_roi = cv2.threshold(gray_roi,127,255,cv2.THRESH_BINARY)
        extract_text = pyt.image_to_string(thr_roi)
        # Substituir caracteres incorretos por números correspondentes
        corrected_text = ""
        for char in extract_text:
            if char == 'G':
                corrected_text += '9'
            else:
                corrected_text += char
        corrected_text = extract_text.replace("276%\n", "26%\n")
        return corrected_text
    magenta = capPoncentagem(190,4,35,14)
    cyan = capPoncentagem(190,25,35,14)
    amarelo = capPoncentagem(190,46,35,14)
    preto = capPoncentagem(190,67,35,14)
    branco1 = capPoncentagem(190,130,35,14)
    branco2 = capPoncentagem(190,151,35,14)
    
    def conferencia():
        conf = input()
        if conf == "Y" or conf == "y":
            gravarDados(magenta, cyan, amarelo, preto, branco1, branco2)
        else:
            reading()
    
    print('Confira os dados recebidos e digite Y para correto e N para incorreto:')
    print(magenta, cyan, amarelo, preto, branco1, branco2)
    conferencia()
    
    
    

reading()