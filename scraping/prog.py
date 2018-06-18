# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--headless")

lista_paginas=[
    'http://search.vivalocal.com/acompanhante-erotico/manaus?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Manaus+AM&searchGeoId=13&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/belem-para?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Belem+PA&searchGeoId=59&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/porto-velho?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Porto+Velho+RO&searchGeoId=127&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/maceio?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Maceio+AL&searchGeoId=7&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1'
    'http://search.vivalocal.com/acompanhante-erotico/salvador?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Salvador+BA&searchGeoId=21&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/fortaleza?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Fortaleza+CE&searchGeoId=32&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1'
    'http://search.vivalocal.com/acompanhante-erotico/sao-luis?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Sao+Luis+MA&searchGeoId=40&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/joao-pessoa?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Joao+Pessoa+PB&searchGeoId=62&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/recife?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Recife+PE&searchGeoId=70&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/teresina?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Teresina+PI&searchGeoId=73&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/natal?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Natal+RN&searchGeoId=115&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/aracaju?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Aracaju+SE&searchGeoId=193&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/goiania?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Goiania+GO&searchGeoId=37&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/cuiaba?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Cuiaba+MT&searchGeoId=43&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/campo-grande-mato-grosso-do-sul?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Campo+Grande+MS&searchGeoId=46&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/brasilia?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Brasilia+DF&searchGeoId=27&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/vitoria?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Vitoria+ES&searchGeoId=31&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/belo-horizonte?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Belo+Horizonte+MG&searchGeoId=53&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/sao-paulo-capital?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Sao+Paulo+SP&searchGeoId=164&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/rio-de-janeiro-capital?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Rio+de+Janeiro+RJ&searchGeoId=76&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/curitiba?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Curitiba+PR&searchGeoId=66&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/porto-alegre-rg-do-sul?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Porto+Alegre+RS&searchGeoId=117&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1',
    'http://search.vivalocal.com/acompanhante-erotico/florianopolis-sc?lb=new&search=1&start_field=1&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&keywords=&cat_1=133&geosearch_text=Florianopolis+SC&searchGeoId=134&sp_personals_age%5Bstart%5D=&sp_personals_age%5Bend%5D=&sp_common_designation=&sp_common_second_type=&sp_common_tags_2%5Bstart%5D=&sp_common_tags_2%5Bend%5D=&sp_text_0=&image_total=1'
]

lista_links=[]

# Criar instância do navegador
print("Criando navegador\n\n")
firefox = webdriver.Firefox(executable_path=r'E:\Programas\geckodriver.exe',firefox_options=options)

for cidade in lista_paginas:
    print("Acessando a pagina \n")
    print(cidade)
    pagina=firefox.get(cidade)
    try:
        firefox.find_element_by_xpath('/html/body/div[9]/div[3]/button[1]').click()
    except:
        pass
    loop1=1
    while(loop1):

#        print("Indo até o final da página")
#        for j in range(1,100):
#            #print(j)
#            firefox.execute_script("window.scroll(0,130*"+str(j)+");")



        print("Extraindo links")
        #Extraindo links para as paginas
        #temp_elementos=firefox.find_elements_by_xpath('/html/body/div[4]/div/div[4]/ul/li[*]/div/a')
        temp_elementos=firefox.find_elements_by_xpath("//a[@class='clad__wrapper']")

        for j in temp_elementos:
            print(j.get_attribute('href'))
            lista_links.append(j.get_attribute('href'))

        try:
            botaoprox=firefox.find_element_by_xpath("//*[contains(text(), 'Próximo')]")
            #print(botaoprox.get_attribute('href'))
            if (botaoprox.get_attribute('href')==None):
                loop1=0
                print('Fim de pesquisa')
            else:
                print("Indo para a próxima pagina")
                botaoprox.click()
        except:
            print("Fim de pesquisa. Pagina unica")
            loop1=0
            pass



print(lista_links)

#caminho=firefox.find_elements_by_xpath("/html/body/div[4]/div/div[3]/ul/li[*]")
#for i in caminho:
#    print(i.find_element_by_xpath('//div/a/div[1]/div/img').get_attribute('src'))



firefox.quit()
