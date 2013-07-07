from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Firefox()

def search(state):
  hosp_list = []
	url = "http://www.hospitalsafetyscore.org/search-result?zip_code=&hospital=&city=&state_prov=" + state + "&agree=agree"
	driver.get(url)
	time.sleep(3)
	all_hospital_element_chunks = driver.find_elements_by_css_selector('div.right-con')
	for hospital in all_hospital_element_chunks:
		name = hospital.find_element_by_css_selector('h1').text
		url = hospital.find_element_by_css_selector('h3 a').get_attribute('href')
		hosp_list.append([name, url])
	with open(state + '.csv', 'wb') as f:
		wtr = csv.writer(f, delimiter = ',')
		wtr.writerows(hosp_list)

f = open('state_abrv.txt', 'r')
state_list = f.read().split()   #state_list = ['AL', 'CA']

for s in state_list:
	search(s)

driver.close()
"""
# Gets the first hospital's HTML on a state page
hospital_1 = driver.find_elements_by_css_selector('div.right-con')[0]
# Extracts the hospital name
hospital_1.find_element_by_css_selector('h1').text
# Extracts the hospital URL
hospital_1.find_element_by_css_selector('h3 a').get_attribute('href')
"""
