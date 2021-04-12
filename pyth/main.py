from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("black")
search.send_keys(Keys.RETURN)

driver.quit()
PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("white")
search.send_keys(Keys.RETURN)

driver.quit()

PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("blue")
search.send_keys(Keys.RETURN)

driver.quit()
PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("green")
search.send_keys(Keys.RETURN)

driver.quit()

PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("White")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[W]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Black")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[B]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Green")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[G]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Blue")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[U]")
print(driver.title)


driver.quit()

PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Blue")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[U]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("black")
search.send_keys(Keys.RETURN)

driver.quit()
PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("white")
search.send_keys(Keys.RETURN)

driver.quit()

PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("blue")
search.send_keys(Keys.RETURN)

driver.quit()
PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("green")
search.send_keys(Keys.RETURN)

driver.quit()

PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("White")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[W]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Black")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[B]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/geckodriver.exe"
driver = webdriver.firefox(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Green")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[G]")
print(driver.title)


driver.quit()




PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Blue")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[U]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)
driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("black")
search.send_keys(Keys.RETURN)

driver.quit()
PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("white")
search.send_keys(Keys.RETURN)

driver.quit()

PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("blue")
search.send_keys(Keys.RETURN)

driver.quit()
PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)

driver.get("https://gatherer.wizards.com/Pages/Default.aspx")
print(driver.title)

search = driver.find_element_by_name("ctl00_ctl00_MainContent_Content_SearchControls_CardSearchBoxParent_CardSearchBox")
search.send_keys("green")
search.send_keys(Keys.RETURN)

driver.quit()

PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("White")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[W]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Black")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[B]")
print(driver.title)


driver.quit()
PATH = "C:/Users/kubaw/Downloads/msedgedriver.exe"
driver = webdriver.edge(PATH)

driver.get("https://gatherer.wizards.com/Pages/Advanced.aspx")
print(driver.title)

search = driver.find_element_by_id("autoCompleteSourceBoxcolorAddText2_InnerTextBox")
search.send_keys("Green")
search.send_keys(Keys.RETURN)
search_but = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAddText_itemsRepeater_ctl00_itemValue")
search_but.click()
search_but2 = driver.find_element_by_id("ctl00_ctl00_MainContent_Content_colorAdd")
search_but2.click()
driver.get("https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&color=+[G]")
print(driver.title)


driver.quit()