from selenium import webdriver
PATH1 = 'C:/Users/kubaw/Desktop/drivery/chromedriver.exe'
PATH2 = 'C:/Users/kubaw/Desktop/drivery/geckodriver.exe'
PATH3 = 'C:/Users/kubaw/Desktop/drivery/msedgedriver.exe'

driver = webdriver.Chrome(PATH1)
driver.get('https://www.fantasynamegenerators.com/viking_names.php')

names = driver.find_element_by_css_selector("#placeholder")
contry = driver.find_element_by_css_selector("a.langFlag:nth-child(2)")
alien = driver.find_element_by_css_selector(".navmenu > li:nth-child(2) > ul:nth-child(2) > ol:nth-child(1) > li:nth-child(1) > a:nth-child(1)")


assert names != None

contry.click()
title = driver.title
assert title == 'Générateur de noms de Vikings. Des centaines de noms sont disponibles, vous trouverez forcément votre bonheur.'

driver.get('https://www.fantasynamegenerators.com/viking_names.php')
alien.click()
check = driver.find_element_by_css_selector('#submitArt > p:nth-child(1) > a:nth-child(1)')
assert check == 'Markus'


driver.close()

driver = webdriver.Firefox(PATH2)
driver.get('https://www.fantasynamegenerators.com/viking_names.php')

names = driver.find_element_by_css_selector("#placeholder")
contry = driver.find_element_by_css_selector("a.langFlag:nth-child(2)")
alien = driver.find_element_by_css_selector(".navmenu > li:nth-child(2) > ul:nth-child(2) > ol:nth-child(1) > li:nth-child(1) > a:nth-child(1)")

assert names != None
contry.click()
title = driver.title
assert title == 'Générateur de noms de Vikings. Des centaines de noms sont disponibles, vous trouverez forcément votre bonheur.'

driver.get('https://www.fantasynamegenerators.com/viking_names.php')
alien.click()
check = driver.find_element_by_css_selector('#submitArt > p:nth-child(1) > a:nth-child(1)')
assert check == 'Markus'

driver.close()

driver = webdriver.Edge(PATH3)
driver.get('https://www.fantasynamegenerators.com/viking_names.php')
names = driver.find_element_by_css_selector("#placeholder")
contry = driver.find_element_by_css_selector("a.langFlag:nth-child(2)")

assert names != None

contry.click()
title = driver.title
assert title == 'Générateur de noms de Vikings. Des centaines de noms sont disponibles, vous trouverez forcément votre bonheur.'

driver.get('https://www.fantasynamegenerators.com/viking_names.php')
alien.click()
check = driver.find_element_by_css_selector('#submitArt > p:nth-child(1) > a:nth-child(1)')
assert check == 'Markus'
driver.close()

driver = webdriver.Chrome(PATH1)
driver.get('https://gdansk.pja.edu.pl/pl/')

tytul = driver.title
infa = driver.find_element_by_css_selector("#sppb-addon-1615575049776 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
wawa = driver.find_element_by_css_selector("li.sp-has-child:nth-child(3) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)")


assert tytul == 'Start'

infa.click()
title = driver.title
assert title == 'Informatyka'

driver.get('https://gdansk.pja.edu.pl/pl/')
wawa.click()
title = driver.title
assert title == 'Strona Główna - Polsko-Japońska Akademia Technik Komputerowych'


driver.close()

driver = webdriver.Firefox(PATH2)
driver.get('https://gdansk.pja.edu.pl/pl/')

tytul = driver.title
infa = driver.find_element_by_css_selector("#sppb-addon-1615575049776 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
wawa = driver.find_element_by_css_selector("li.sp-has-child:nth-child(3) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)")


assert tytul == 'Start'

infa.click()
title = driver.title
assert title == 'Informatyka'

driver.get('https://gdansk.pja.edu.pl/pl/')
wawa.click()
title = driver.title
assert title == 'Strona Główna - Polsko-Japońska Akademia Technik Komputerowych'


driver.close()

driver = webdriver.Edge(PATH3)
driver.get('https://gdansk.pja.edu.pl/pl/')

tytul = driver.title
infa = driver.find_element_by_css_selector("#sppb-addon-1615575049776 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
wawa = driver.find_element_by_css_selector("li.sp-has-child:nth-child(3) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)")


assert tytul == 'Start'

infa.click()
title = driver.title
assert title == 'Informatyka'

driver.get('https://gdansk.pja.edu.pl/pl/')
wawa.click()
title = driver.title
assert title == 'Strona Główna - Polsko-Japońska Akademia Technik Komputerowych'


driver.close()


