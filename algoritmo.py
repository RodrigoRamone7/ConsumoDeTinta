import pyautogui
import pygetwindow as gw

def ripwin():
    window_true = None
    janelas = []
    janelas += gw.getAllTitles() #Array with all active windows
    
    tittle = 'RasterLinkPro5IP' #Título a ser encontrado
    for valid in janelas: #Valida se o raster link está aberta
        if tittle in valid:
            window_true = valid
            window_index = janelas.index(window_true)
            break
    if window_true:
        rasterlinkwindow = gw.getWindowsWithTitle(window_true)[0]
        
            
    else:
        pyautogui.alert(text='Abra o programa de RIP', title='ERRO!', button='OK')
        

ripwin()