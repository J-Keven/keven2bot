
# keven2bot
Este repositório contém um simples bot criado para o Telegram. nesse codigo foi inserido comportamentos simples ao bot, apenas reponde a alguns comando como "/oi", "/cafe",  "/pipoca" e o bot responde com gifs de acordo com cada comando.
O codigo foi desenvolvido acompanhando o pyjamas conf 2019, onde o [helioloureiro](https://github.com/helioloureiro "helioloureiro") foi o palestrante que demonstrou algumas formas de se utilizar a linguagem python para criar interaçõe para bots no Telegram.

## Requisitos
De início é necessário criar um bot no telegram e obter a key de acesso a esse bot para inserir novos comportamentos a ele. Para isso siga o passo a passo abaixo:
- Abra seu Telegram e busque por: **@BotFather**;
- No chat do **@BotFather** digite: **/newbot**;
- Insira um **nome** para o seu bot
> Lembrando que o nome escolhido para o bot tem que terminar com "bot", ex: keven2bot.
- Insira um **username**
-  Feito isso voce recebera um token que servira para que você possa acesar a API.
- Também sera necessário  que voce tenha a API instalada na sua maquina, para isso execute o comando abaixo:

	    pip3 install pyTelegrambotAPI

## observação
O token que está no codigo [keven2bot.py](https://github.com/J-Keven/keven2bot/blob/master/keven2bot.py "keven2bot.py") já está desativado, entao para que o código funcione é necessario obter um token válido, e ai voce pode substituir pelo que a variável **KEY** está armazenando.
