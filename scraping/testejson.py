# -*- coding: utf-8 -*-
import json

def exibir(entrada):
    print json.dumps(entrada, sort_keys=True, indent=4, separators=(',', ': '))

data=json.loads("""
    {}"""
)
exibir(data)
temp=144
data['segundo']={

      "telefone" : [
        {
            "numero": "111",
            "desde": "15/22/2011"
        }
      ],

      "titulo"  : "tit",
      "descri"  : "Olá Mundo!! ççç é",
      "cache"   : temp
  }

print('\n')
exibir(data)
data['segundo']['telefone'].append(
    {
        "numero": "2222",
          "desde": "15/22/2011"
    }
)

exibir(data)
exibir(data['segundo']['telefone'])