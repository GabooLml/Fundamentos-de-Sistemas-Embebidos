#! /bin/bash

#Token del bot de Telegram
TOKEN="5750664400:AAGFA9MkVc9INtQlifD270DsjrpWul1-gQk"

#ID del chat al que se mandarán las alertas
ID="5755555473"

#Mensaje que se va a mandar al chat
MENSAJE="HERMES se ha puesto en línea"

#URL de la API por la cual se harán llegar las alertas
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

#Comando que concatena las variables en una URL para realizar la petición
curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"

