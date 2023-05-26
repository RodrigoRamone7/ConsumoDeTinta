import pyautogui as ag
import pygetwindow as gw

print(input('Coloque a janela do RIP no monitor principal e pressione qualquer tecla'))

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
        
capture()