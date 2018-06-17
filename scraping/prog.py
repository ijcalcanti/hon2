# -*- coding: utf-8 -*-

from selenium import webdriver

# Criar instância do navegador
firefox = webdriver.Firefox(executable_path=r'E:\Programas\geckodriver.exe')

pagina=firefox.get('htt38577063')
texto=firefox.find_element_by_class_name('shortdescription').text

link=firefox.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/div[1]/div[6]/div/div[3]/div[1]/div[8]/img").get_attribute('src')
print(link)


firefox.quit()
