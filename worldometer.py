from selenium import webdriver

driver=webdriver.Firefox()

driver.get('https://www.worldometers.info/coronavirus/country/india/')

rise = driver.find_elements_by_class_name("news_li")

num_days = len(rise)
print(len(rise))
print
for i in range(num_days):
    print(rise[i].text) 