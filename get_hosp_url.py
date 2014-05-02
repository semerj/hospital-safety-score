#!/usr/bin/Python

from selenium import webdriver
import time
import csv

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
	with open('data/' + state + '.csv', 'wb') as f:
		wtr = csv.writer(f, delimiter=',')
		wtr.writerows(hosp_list)

states = [
	"AL","AK","AZ","AR","CA","CO","CT","DC","DE","FL","GA","HI","ID","IL","IN","IA","KS",
	"KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
	"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
	]

driver = webdriver.PhantomJS()
driver.get("http://www.hospitalsafetyscore.org/")
driver.find_element_by_id('TermsCheckbox').click()
driver.find_element_by_id('search_hosp_btn').click()

for state in states:
	search(state)

driver.close()
