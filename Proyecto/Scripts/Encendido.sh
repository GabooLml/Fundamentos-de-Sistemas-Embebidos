#! /bin/bash

TOKEN="5750664400:AAGFA9MkVc9INtQlifD270DsjrpWul1-gQk"
ID="5755555473"
MENSAJE="HERMES se ha puesto en línea"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"

