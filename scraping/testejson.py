# -*- coding: utf-8 -*-
import json
import requests

def exibir(entrada):
    print json.dumps(entrada, sort_keys=True, indent=4, separators=(',', ': '))

data=json.loads("""
    {}"""
)
exibir(data)
temp=144
data={
    "identificador":"ident2",

    "titulo"  : "tit",
    "descri"  : "Olá Mundo!! ççç é",
    "cache"   : temp
}


exibir(data)
resposta=requests.post('http://127.0.0.1:8000/receber_dados/',data=data)