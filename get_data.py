from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from IPython import embed

driver = webdriver.Firefox()

def get_data(url):
  driver.get(url)
	time.sleep(5)
	elements = driver.find_elements_by_css_selector('.hospitals_score')
	txt_list = []
	for element in elements:
	    txt_list.append(element.text)
	#txt_list = [txt_list]
	#print txt_list
	return txt_list

f = open('state_abrv.txt')
state_list = f.read().split() 

def open_state_file(file):
	all_data = []
	s = open(file + '.csv')
	url_list = csv.reader(s)
	for line in url_list:
		data_result = get_data(line[1])
		#line.append(data_result)
		line = line + data_result
		#embed()
		all_data.append(line)
		#embed()
	return all_data

#for s in state_list:
with open("AK_data.csv", "wb") as f:
	writer = csv.writer(f, delimiter = ",")
	writer.writerows(open_state_file('AK'))

driver.close()
