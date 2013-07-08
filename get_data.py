# warning: this took 4.5 hrs to go form AL to WY

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
#from IPython import embed

driver = webdriver.Firefox()

def get_data(url):
	driver.get(url)
	time.sleep(5)
	elements = driver.find_elements_by_css_selector('.hospitals_score')
	grade = driver.find_element_by_css_selector('.d-col1').get_attribute('data-grade')
	lat = driver.find_element_by_css_selector('.d-col1').get_attribute('data-lat')
	lon = driver.find_element_by_css_selector('.d-col1').get_attribute('data-lon')
	address = driver.find_element_by_css_selector('.d-add').text
	txt_list = []
	txt_list.extend([grade, address, lat, lon])
	for element in elements:
	    txt_list.append(element.text)
	return txt_list

def open_state_file(file):
	all_data = []
	s = open(file + '.csv')
	url_list = csv.reader(s)
	for line in url_list:
		data_result = get_data(line[1])
		line = line + data_result
		all_data.append(line)
	return all_data

f = open('state_abrv.txt')
state_list = f.read().split() 

for s in state_list:
	with open(s + "_data.csv", "wb") as f:
		writer = csv.writer(f, delimiter = ",")
		writer.writerows(open_state_file(s))

driver.close()
