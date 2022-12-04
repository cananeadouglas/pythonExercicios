from selenium import webdriver
webdriver.Chrome
from selenium.webdriver.common.keys import Keys
import time
import urllib


navegador = webdriver.Chrome()
navegador.get("www.google.com.br/")

