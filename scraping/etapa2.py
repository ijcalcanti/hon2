# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import json
import requests

def exibir(entrada):
    print json.dumps(entrada, sort_keys=True, indent=4, separators=(',', ': '))


options = Options()
options.add_argument("--headless")

lista=[
    "http://www.vivalocal.com/acompanhante-erotico/recreio/paty-greluda-uma-hora-em-meu-local-r--100-reais-no-recreio-/178905894"]

print("Criando navegador\n\n")

firefox = webdriver.Firefox(executable_path=r'E:\Programas\geckodriver.exe',firefox_options=options)

for i in lista:
    print("Acessando a página")
    firefox.get(i)
    print("Procurando elementos")
    cache=firefox.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[1]/table/tbody/tr[10]/td/div[2]/div[2]')
    cache=cache.text

    try:
        telefone=firefox.find_element_by_xpath('//*[@id="contact_phone_bottom_wrapper"]')
    except:
        cache='-'
    if(cache=='-'):
        print("Cache nao informado, seguindo em frente")

    else:
        cache=cache.replace("R$","")
        cache=float(cache)


        #Gerar telefone codificavel

        telefone=telefone.get_attribute('data-phone-number')
        print(telefone)
        telefone=telefone.replace("-","")
        telefone=int(telefone)

        #Calcula ultima atualizacao
        data_atualizacao=firefox.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[5]/span[2]')
        data_atualizacao=data_atualizacao.text
        data_atualizacao=data_atualizacao.split(" ")
        data_atualizacao=data_atualizacao[2]
        #data_atualizacao=datetime.strptime(data_atualizacao,'%d/%m/%Y')

        #Descriçao
        descricao=firefox.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[1]/div[7]/div[2]')
        descricao=descricao.text

        #Idade
        idade=firefox.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[1]/table/tbody/tr[3]/td[2]').text
        idade=idade.split(' ')
        idade=idade[0]
        idade=int(idade)

        #Cidade
        cidade=firefox.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[1]/table/tbody/tr[1]/td[2]/div').text
        cidade=cidade.split('\n')
        cidade=cidade[0]
        cidade=cidade.split(" - ")
        estado=cidade[1]
        cidade=cidade[0]

        #Local-Atendimento - ELEMENTO MULTIPLO
        local_atend=firefox.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div[1]/table/tbody/tr[6]/td[2]').text
        try:
            local_atend=local_atend.split(', ')
        except:
            pass

    data={
        "telefone":telefone,
        "descricao" : descricao,
        "cache"     : cache,
        "estado"    : estado,
        "cidade"    : cidade,
        "idade"     : idade,
        "atualizado": data_atualizacao,
        "local"     : local_atend
    }
    exibir(data)
    resposta=requests.post('http://127.0.0.1:8000/receber_dados/',data=data,)







firefox.quit()