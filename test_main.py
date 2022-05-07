# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMain():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_main(self):
    self.driver.get("https://jakuborlinskiupm.github.io/EvaluationOfInteractiveSystems//EvaluationOfInteractiveSystems/")
    self.vars["null"] = self.driver.execute_script("let randInt = Math.floor(Math.random() * 100); let buttonAlt = document.querySelector(\'.button-alt\'); if (buttonAlt.parentNode.children[0].classList.contains(\'button-alt\')) { 	if (randInt > 90) { 		buttonAlt.click(); 	} } else { 	if (randInt > 70) { 		buttonAlt.click(); 	} }")
  
