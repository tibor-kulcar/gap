from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site = webdriver.Firefox()
site.get("http://localhost:8080")
assert "Example project" in site.title
elem = site.find_element_by_id("sub-title")
assert "Example project" in elem.text

site.close()

site = webdriver.Chrome(executable_path="./chromedriver")
site.get("http://localhost:8080")
assert "Example project" in site.title
elem = site.find_element_by_id("sub-title")
assert "Example project" in elem.text

site.close()