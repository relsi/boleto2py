# coding: utf8
# tente algo como
def index(): return dict(message="hello from cobranca.py")

def imprime_boleto():
    import boleto2py.banrisul as banrisul
    import boleto2py.gerador as gerador

    barras = banrisul.gera_cod_barras('550000', '22832563', '2000-07-04')
    gera_linha = banrisul.gera_linha_digitavel(barras)
    cod_barra_boleto = gerador.getcodbarra(barras)
    tipo = 'gif'
    cod_barra_boleto.save('applications/boleto2py/static/barcode/%s.%s'%(barras,tipo), tipo)
    img_barras = '%s.%s'%(barras,tipo)
    return dict(barras=barras, gera_linha=gera_linha, img_barras=img_barras)
