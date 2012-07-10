# -*- coding: utf-8 -*-
"""boleto2py
~~~~~~~~~~~~~
Ferramenta de criação de boletos bancários baseado no código fonte do pyboleto by Eduardo Cereto Carvalho
Para utilização com web2py.
Licensa: BSD
"""
import Image
import ImageDraw
import datetime

def modulo10(num):
    soma = 0
    peso = 2
    for i in range(len(num) - 1, -1, -1):
        parcial = int(num[i]) * peso
        if parcial > 9:
            s = "%d" % parcial
            parcial = int(s[0]) + int(s[1])
        soma += parcial
        if peso == 2:
            peso = 1
        else:
            peso = 2

    resto10 = soma % 10
    if resto10 == 0:
        modulo10 = 0
    else:
        modulo10 = 10 - resto10

    return modulo10

def modulo11(num, base=9, r=0):
    soma = 0
    fator = 2
    for i in range(len(num) -1, -1, -1):
        parcial10 = int(num[i]) * fator
        soma += parcial10
        if fator == base:
            fator = 1
        fator += 1
    if r == 0:
        soma = soma * 10
        digito = soma % 11
        if digito == 10:
            digito = 0
        return digito
    if r == 1:
        resto = soma % 11
        return resto

def formata_numero(numero, tamanho):
    return numero.zfill(tamanho)
    
def fator_vencimento(data_vcto):
    date_ref = datetime.date(2000, 7, 3)  # Fator = 1000
    data_vencimento = datetime.date(int(data_vcto[0:4]), int(data_vcto[5:7]), int(data_vcto[8:10]))
    delta = data_vencimento - date_ref
    fator = delta.days + 1000
    return fator

def getcodbarra(valor, posX=0, posY=0, height = 50):
    # padrão 2 por 5 intercalado ( utilizado em boletos bancários )
    padrao = ('00110', '10001', '01001', '11000', '00101',
              '10100', '01100', '00011', '10010', '01010')

    # criando imagem
    imagem = Image.new('RGB',(400,60),'white')
    draw = ImageDraw.Draw(imagem)

    # verificando se o conteudo para gerar barra é impar, se for,
    # adiciona 0 no inicial para fazer intercalação em seguida dos pares 

    if (len(valor) % 2) != 0:
        valor= '0' + valor

    # faz intercalação dos pares
    l=''
    for i in range(0,len(valor),2):
        p1=padrao[int(valor[i])]
        p2=padrao[int(valor[i+1])]
        for p in range(0,5):
            l+=p1[:1] + p2[:1]
            p1=p1[1:]
            p2=p2[1:]

    # gerando espaços e barras
    barra=True
    b=''

    # P = preto
    # B = banco

    for i in range(0,len(l)):
        if l[i] == '0':
            if barra:
                b+='P'
                barra=False
            else:
                b+='B'
                barra=True
        else:
            if barra:
                b+='PPP'
                barra=False
            else:
                b+='BBB'
                barra=True

    # concatena inicio e fim
    b='PBPB' + b + 'PPPBP'

    # P = preto
    # B = banco 

    # percorre toda a string b e onde for P pinta de preto, onde for B pinta de banco 

    for i in range(0,len(b)):
        if b[i] == 'P':
            draw.line((posX,posY,posX,posY + height),'black')
        else:
            draw.line((posX,posY,posX,posY + height),'white')
        posX+=1
    return imagem
