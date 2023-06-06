import pyautogui as ag
import pygetwindow as gw
import pytesseract as pyt
import cv2

print(input('Coloque a janela do RIP no monitor principal e pressione qualquer tecla'))

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
        rasterlinkwindow.resizeTo(800, 800)
        
            
    else: #Mensagem de erro caso o RIP não esteja aberto
        ag.alert(text='Abra o programa de RIP', title='ERRO!', button='OK')
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
        img = ag.screenshot('ss.png',region=(544,202, 221, 169),)
        
        
def reading(): #Leitura de dados da imagem
    capture()
    img = cv2.imread('ss.png')
    def capmagenta(): #Captura de dados de magenta
        x, y, width, height = 182, 5, 35, 14 #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        extract_text = pyt.image_to_string(gray_roi)
        return extract_text
    magenta = capmagenta()
    
    def capcyan(): #Captura de dados de cyan
        x, y, width, height = 182, 26, 35, 14 #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        extract_text = pyt.image_to_string(gray_roi)
        return extract_text
    cyan = capcyan()
    
    def capamarelo(): #Captura de dados de amarelo
        x, y, width, height = 182, 47, 35, 14 #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        extract_text = pyt.image_to_string(gray_roi)
        return extract_text
    amarelo = capamarelo()
    
    def cappreto(): #Captura de dados de preto
        x, y, width, height = 182, 68, 35, 14 #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        extract_text = pyt.image_to_string(gray_roi)
        return extract_text
    preto = cappreto()
    
    def capbranco1(): #Captura de dados de branco1
        x, y, width, height = 182, 131, 35, 14 #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        extract_text = pyt.image_to_string(gray_roi)
        return extract_text
    branco1 = capbranco1()
    
    def capbranco2(): #Captura de dados de branco2
        x, y, width, height = 182, 152, 35, 14 #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        extract_text = pyt.image_to_string(gray_roi)
        return extract_text
    branco2 = capbranco2()
    
    print(magenta, cyan, amarelo, preto, branco1, branco2)

reading()