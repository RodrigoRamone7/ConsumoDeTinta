import openpyxl as xl
from openpyxl.styles import numbers
from datetime import datetime

def gravarDados(m,c,a,b,wh1,wh2):
    def data_hora():
        # Obter a data e hora atuais
        data_hora_atual = datetime.now()

        # Formatando a data e hora no formato desejado
        formato = "%d/%m/%Y %H:%M"
        data_hora_formatada = data_hora_atual.strftime(formato)
        return data_hora_formatada

    # Carregar o arquivo da planilha existente
    wb = xl.load_workbook('Consumo.xlsx')
    wb.save('Backup.xlsx')

    # Escolhe active sheet
    ws = wb.active

    # Encontrar a próxima célula vazia na coluna A
    next_row = ws.max_row + 1

    magenta = m
    cyan = c
    amarelo = a
    preto = b
    branco1 = wh1
    branco2 = wh2
    
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

    # Dados que você deseja adicionar
    dados = [data_hora(),
            magenta, f"=D{next_row} * 600 / 100 *100",
            cyan, f"=B{next_row} * 600 / 100 *100",
            amarelo, f"=F{next_row} * 600 / 100 *100",
            preto, f"=H{next_row} * 600 / 100 *100",
            branco1, f"=J{next_row} * 600 / 100 *100",
            branco2, f"=L{next_row} * 600 / 100 *100",
            f'=C{next_row}+E{next_row}+G{next_row}+I{next_row}+K{next_row}+M{next_row}']

    # adiciona os dados na próxima linha vazia sem sequencia
    for i, dado in enumerate(dados, start=1):
        coluna = ws.cell(row=next_row, column=i)
        coluna.value = dado
        


    def format_colum_percent(coluna): #Formata a coluna em porcentagem para valores de string terminados em %
        format_num = numbers.FORMAT_PERCENTAGE
        col = coluna
        for celula in ws[col]:
            celula.number_format = format_num
            valor_format = celula.value
            if isinstance(valor_format, str) and valor_format.endswith('%'):
                valor_num = float(valor_format.strip('%')) / 100
                celula.value = valor_num

    format_colum_percent("B")
    format_colum_percent("D")
    format_colum_percent("F")
    format_colum_percent("H")
    format_colum_percent("J")
    format_colum_percent("L")

    def format_colum_ml(coluna):
        col = ws[coluna]
        format_num = ws['C2'].number_format
        for celula in col:
            celula.number_format = format_num
            
    format_colum_ml("C")
    format_colum_ml("E")
    format_colum_ml("G")
    format_colum_ml("I")
    format_colum_ml("K")
    format_colum_ml("M")
    format_colum_ml("N")

    wb.save('Consumo.xlsx')

