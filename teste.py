from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
#Passo 1: abrindo o site
driver.get('https://buger-eats.vercel.app/')

#Passo 2: validar botão Cadastre-se para fazer entregas
driver.find_element('xpath', '//*[@id="page-home"]/div/main/a').click()
#Passo 3 : validar que o campo nome completo seja obrigatório o preenchimento
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[1]/div[1]/input').send_keys("Usuario")
#Passo 4: validar que o campo CPF seja um CPF válido
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[1]/div[2]/input').send_keys("23149321026")
#Passo 5: validar que o campo E-mail seja obrigatório o preenchimento
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[2]/div[1]/input').send_keys("aleena6707@uorak.com")
#Passo 6: validar que o campo whatsapp aceite somente 12 números
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[1]/div[2]/div[2]/input').send_keys("11 91111-1111")
#Passo 7: validar botão BUSCAR CEP com CEP válido
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[1]/div[1]/input').send_keys("69900-901")
#Passo 8: validar que o campo número seja obrigatório o preenchimento
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[3]/div[1]/input').send_keys("10")
#Passo 9: validar botão CEP
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[2]/div[1]/div[2]/input').click()
#Passo 10: validar que o Método de entrega só permite selecionar uma categoria
driver.find_element('xpath', '//*[@id="page-deliver"]/form/fieldset[3]/ul/li[2]').click()
#Passo 11: validar que o upload da Foto seja obrigatório foto da CNH
driver.find_element('xpath', '//*[@id="page-deliver"]/form/div/p').click()
#Passo 12: validar que o botão Cadastre-se para fazer entrega finalize o cadastro
driver.find_element('xpath','//*[@id="page-deliver"]/form/button').click()
#Passo 13: validar botão fechar do modal informativo 
driver.find_element('xpath', '/html/body/div[2]/div/div[6]/button[1]').click()
