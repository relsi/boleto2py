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


Como usar
---------
Instale o pacote web2py.app.boleto2py.w2p e verifique o controller cobranca

Referências externas
--------------------

Além do pyboletos, utilizei as seguintes referências

http://informacaocomdiversao.blogspot.com/2009/01/entendendo-como-formada-linha-digitvel.html
https://github.com/klawdyo/PHP-Object-Boleto

