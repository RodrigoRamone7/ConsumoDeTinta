import pyautogui as ag
import pygetwindow as gw
import pytesseract as pyt
import cv2
from dados import gravarDados

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
    def capPoncentagem(x,y,width,height): #Captura de dados de porcentagem
        x, y, width, height = x, y, width, height #Coordenadas e tamanho do dado a ser capturado
        roi = img[y:y+height, x:x+width]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        extract_text = pyt.image_to_string(gray_roi)
        return extract_text
    magenta = capPoncentagem(182,5,35,14)
    cyan = capPoncentagem(182,26,35,14)
    amarelo = capPoncentagem(182,47,35,14)
    preto = capPoncentagem(182,68,35,14)
    branco1 = capPoncentagem(182,131,35,14)
    branco2 = capPoncentagem(182,152,35,14)
    
    def limparcaractere(limp):
        l = limp
        limpar = "\n"
        for letra in l:
            if letra in limpar:
                l = l.replace(letra,'')
        return l
    
    magenta = limparcaractere(magenta)
    cyan = limparcaractere(cyan)
    amarelo = limparcaractere(amarelo)
    preto = limparcaractere(preto)
    branco1 = limparcaractere(branco1)
    branco2 = limparcaractere(branco2)
    
    gravarDados(magenta, cyan, amarelo, preto, branco1, branco2)

reading()