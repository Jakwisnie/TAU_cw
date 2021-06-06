from selenium import webdriver
PATH1 = 'C:/Users/kubaw/Desktop/drivery/chromedriver.exe'

driver = webdriver.Chrome(PATH1)
driver.get('https://gdansk.pja.edu.pl/pl/')

infa = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/section[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/a")
strefaK = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/section[2]/div/div/div/div[2]/div/div[5]/div/div/div[2]/div/div/div[4]/div/div/div[13]/div/div/div[10]/div/div/p[1]/span/span/strong/a")
przyd = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/section[2]/div/div/div/div[2]/div/div[4]/div/div/div/div[2]/div/div/div/div/ul/li[9]/a")
tyt = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/section[2]/div/div/div/div[2]/div/div[6]/div/div/div[2]/div/div/div[4]/div/div/div[8]/div/div/div[9]/div/h3[2]")

infa.click()
strefaK.click()
przyd.click()



assert tyt == "PRZYDATNE INFORMACJE"

driver.close()


driver = webdriver.Chrome(PATH1)
driver.get('https://www.pja.edu.pl/')

infaa = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/ul/li[1]/a")
opl = driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/div[1]/div/div[2]/ul/div/li[7]/a")
cena = driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/div[2]/div[3]/div[2]/div/ul/li[1]")
infaa.click()
opl.click()

assert cena == "Studia inżynierskie stacjonarne polskojęzyczne (dzienne) - 1380 zł"


driver.close()

