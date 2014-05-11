from selenium import webdriver
import time
import csv


def search(state):
    hosp_list = []
    base_url = (
      "http://www.hospitalsafetyscore.org/"
      "search-result?zip_code=&hospital=&city=&state_prov="
      )
    url = base_url + state + "&agree=agree"
    driver.get(url)
    time.sleep(3)
    chunks = driver.find_elements_by_css_selector('div.right-con')
    for hospital in chunks:
        get_name = hospital.find_element_by_css_selector('h1')
        get_name_text = name.text
        get_url = hospital.find_element_by_css_selector('h3 a')
        get_url_att = get_url.get_attribute('href')
        hosp_list.append([get_name_text, get_url_att])
    with open('url_data/' + state + '.csv', 'wb') as f:
        wtr = csv.writer(f, delimiter=',')
        wtr.writerows(hosp_list)

states = ["AL", "AK", "AZ", "AR", "CA", "CO",
          "CT", "DC", "DE", "FL", "GA", "HI",
          "ID", "IL", "IN", "IA", "KS", "KY",
          "LA", "ME", "MD", "MA", "MI", "MN",
          "MS", "MO", "MT", "NE", "NV", "NH",
          "NJ", "NM", "NY", "NC", "ND", "OH",
          "OK", "OR", "PA", "RI", "SC", "SD",
          "TN", "TX", "UT", "VT", "VA", "WA",
          "WV", "WI", "WY"]

driver = webdriver.PhantomJS()
driver.get("http://www.hospitalsafetyscore.org/")
driver.find_element_by_id('TermsCheckbox').click()
driver.find_element_by_id('search_hosp_btn').click()

for state in states:
    search(state)

driver.close()
