# Coleta de dados de consumo de tinta
 Este projeto tem como finalidade coletar dados de consumo de tinta ao longo do tempo
 
 ---

 ## Softwares utilizados
 * Para este projeto estaremos utilizando o software de RIP da MIMAKI RasterLinkPro5 IP
 * Utilizaremos a linguagem python para coleta de dados
 * Tesseract-OCR é nesserário para leitura dos dados dentro da Screenshot
 ### Biblicotecas 
 * [PyAutoGUI](https://pyautogui.readthedocs.io/)
 * [PyGetWindow](https://pygetwindow.readthedocs.io/en/latest/)
 * [PyTesseract](https://pypi.org/project/pytesseract/)
 * [OpenCV](https://opencv24-python-tutorials.readthedocs.io/en/latest/)
 * [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)

---

## Utilização
O script algoritmo.py utiliza funções para fazer toda a captura de uma screenshot dentro da janela do RIP.
A primeira coisa que será necessário fazer é a instalação do Tesseract-OCR para seja possível a leitura desta screenshot e será necessário fornecer o caminho do Tesseract-OCR ao script na linha de código 9 `pyt.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'`.

O script será executado e é necessário que a janela do RIP esteja no monitor principal, caso utilize dois monitores. Caso a janela de RIP não esteja aberta, o script exibirá uma mensagem de erro informando que a mesma não está aberta e o script será interrompido.

Os dados serão gravados em um novo arquivo de nome especificado na linha 95 do script dados.py `wb.save('Consumo.xlsx')`. Um backup será feito pelo script para evitar que o arquivo excel anterior seja gravado errado. Da mesma forma, o script solicitará que sejam conferidos os dados antes da gravação. Caso os dados não estejam corretos o script será interrompido e deve ser executado novamento após os devidos ajustes.
### Possíveis problemas
* A janela de RIP sofre alterações de tamanho com a função `ripwin()`, podendo ocorrer que a janela de tinta seja aberta de forma inadequada, sendo necessário que o usuário corrija o tamanho do espaço onde as informações são mantidas.
