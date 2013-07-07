from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Firefox()
driver.get("http://www.hospitalsafetyscore.org/hospital-details?location_id=ad6bb4a3")

headers = driver.find_elements_by_css_selector('.table-headers')
head_list = []
for h in headers[0:6]:
  txt_list.append(h.text)
return txt_list # list of column headers

sky = driver.find_elements_by_css_selector('.sky-blue td')
sky_list = []
for s in sky:
	sky_list.append(s.text)

sky_list[0:78:7] 	# list of all measures; state file column headers
sky_list[6:78:7] 	# list of all dates

s_list = []
for i in range(7):
	s_list.append(sky_list[i:78:7])

s_list 				    # list of lists
s_list[0] 			  # list of all measures; state file column headers
s_list[6] 			  # list of dates
