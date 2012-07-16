# -*- coding: utf-8 -*-
import gerador

#dados fornecidos no manual, alterar para os dados do cedente
banco = "041"
ag_cedente = "1102"
cod_cedente = "9000150"
moeda = "9"
especie = "R$"
carteira = "2"


def gera_linha_digitavel(cod_barra):

        num_d1 = "%4s%1s%1s%3s" % (cod_barra[0:4],cod_barra[19:20],cod_barra[20:21],cod_barra[21:24])
        ver_d1 = gerador.modulo10(num_d1)

        num_d2 = "%1s%7s%2s" % (cod_barra[24:25],cod_barra[25:32],cod_barra[32:34])
        ver_d2 = gerador.modulo10(num_d2)

        num_d3 = "%6s%2s%2s" % (cod_barra[34:40],cod_barra[40:42],cod_barra[42:44])
        ver_d3 = gerador.modulo10(num_d3)
        
        campo_1 = "%4s%1s%1s%1s%3s%1s%2s" % (cod_barra[0:4],cod_barra[19:20],'.',cod_barra[20:21],cod_barra[21:24],ver_d1,'  ')
        campo_2 = "%1s%4s%1s%3s%2s%1s%2s" % (cod_barra[24:25],cod_barra[25:29],'.',cod_barra[29:32],cod_barra[32:34],ver_d2,'  ') 
        campo_3 = "%5s%1s%1s%2s%2s%1s%2s" % (cod_barra[34:39],'.',cod_barra[39:40],cod_barra[40:42],cod_barra[42:44],ver_d3,'  ')
        dac = "%1s%2s" % (cod_barra[4:5],'  ')
        fat_vcto = "%4s" % (cod_barra[5:9])
        valor = "%10s" % (cod_barra[9:19])

        linha_digitavel = campo_1+campo_2+campo_3+dac+fat_vcto+valor

        return linha_digitavel 

def gera_cod_barras(valor, nosso_numero, data_vencimento):
    nosso_numero = gerador.formata_numero(nosso_numero, 8)

    def calc_nc(num):
        digito_1 = gerador.modulo10(num)
        digito_2 = gerador.modulo11(str(num)+str(digito_1), 7, 1)
        if digito_2 == 1:
            digito_1 += 1
            digito_2 = gerador.modulo11(str(num)+str(digito_1), 7, 1)
            digito_2 = 11 - digito_2
        else:
            digito_2 = 11 - digito_2
        return [digito_1, digito_2]

    duplo_digito = calc_nc(nosso_numero)
    nc_1 = duplo_digito[0]
    nc_2 = duplo_digito[1]

    ofator_vencimento = gerador.fator_vencimento(data_vencimento)

    digitos_calc_geral = "%1s%1s%4s%7s%8s%2s" %('2','1',ag_cedente,cod_cedente,nosso_numero,'40')
    
    def calc_nc_g(posicoes):
        digito_1 = gerador.modulo10(posicoes)
        digito_2 = gerador.modulo11(str(posicoes)+str(digito_1), 7, 1)
        if digito_2 == 1:
            digito_1 += 1
            digito_2 = gerador.modulo11(str(posicoes)+str(digito_1), 7, 1)
            digito_2 = 11 - digito_2
        elif digito_2 == 0:
            digito_2 = digito_2
        else:
            digito_2 = 11 - digito_2
        return [digito_1, digito_2]

    digito_nc = calc_nc_g(digitos_calc_geral)

    calc_dac = "%3s%1s%4s%10s%1s%1s%4s%7s%8s%2s%1s%1s" % (
        banco, 
        moeda, 
        ofator_vencimento, 
        gerador.formata_numero(valor, 10), 
        '2', 
        '1', 
        ag_cedente, 
        cod_cedente, 
        nosso_numero, 
        '40', 
        digito_nc[0],
        digito_nc[1]
    )

    resto_dac = gerador.modulo11(calc_dac, 9, 1)
    if resto_dac in [0, 1, 10]:
        num_dac = 1
    else:
        num_dac = 11 - resto_dac

    cod_barra = "%3s%1s%1s%4s%10s%1s%1s%4s%7s%8s%2s%1s%1s" % (
        banco,
        moeda,
        num_dac,
        ofator_vencimento,
        gerador.formata_numero(valor, 10),
        '2',
        '1',
        ag_cedente,
        cod_cedente,
        nosso_numero,
        '40',
        digito_nc[0],
        digito_nc[1]
    )
    return cod_barra
