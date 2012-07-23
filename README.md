boleto2py
=============

Módulo para geração de boletos no web2py, baseado no código do pyboleto

Licença
-------
O módulo esta licenciado sob a licença BSD


Estrutura do módulo
-------------------

boleto2py/

boleto2py/gerador.py

boleto2py/banrisul.py

gerador.py possui algumas funcionalidades comuns aos boletos, banrisul.py possui funcionalidades específicas
a este banco. Embora exista um padrão mínimo, cada banco tem suas particularidades.

Criando novos boletos
---------------------
Para criar um novo boleto, basta importar o arquivo gerador.py e criar os digitos verificadores, linha digitável, fator de vencimento e código de barra


Exemplo de uso
---------

```python
def imprime_boleto_banrisul():
    import boleto2py.banrisul as banrisul
    import boleto2py.gerador as gerador

    vcto = '2012-07-10'
    valor = '34.98'
    doc_num = '1'
    
    barras = banrisul.gera_cod_barras(valor.replace('.',''), doc_num, vcto)

    gera_linha = banrisul.gera_linha_digitavel(barras[0])
    cod_barra_boleto = gerador.getcodbarra(barras[0])
    tipo = 'gif'
    cod_barra_boleto.save('applications/boleto2py/static/barcode/%s.%s'%(barras[0],tipo), tipo)
    img_barras = '%s.%s'%(barras[0],tipo)
```

Bancos Homologados até o momento
--------------------------------
- Banrisul

Referências externas
--------------------

Além do pyboletos, utilizei as seguintes referências

http://informacaocomdiversao.blogspot.com/2009/01/entendendo-como-formada-linha-digitvel.html

https://github.com/klawdyo/PHP-Object-Boleto

http://thiagosm.wordpress.com/2008/06/07/codigo-de-barra-em-python/

pyboletos

