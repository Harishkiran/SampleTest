import datetime
import logging
import os, sys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#
#
import global_var
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select


class CommonUtil(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = global_var.logger
        self.waitobj = WebDriverWait(self.driver, 25)
        
    def click_element(self, xpath, wtime=10):
        try:
            self.logger.info("==> Action:- [Click on Element] %s "%(xpath))
            if not self.check_element_exists_by_xpath(xpath,wtime):
                self.logger.error("==> !!ALERT!! --click_element-- xpath '%s' is DOES NOT exist. Please check!!" %xpath)
                return False
            if not self.waitobj.until(EC.element_to_be_clickable((By.XPATH, xpath))):
                self.logger.info("==> !!ALERT!! --click_element-- Element '%s' is not clickable. Please check!!" %xpath)
                return False
            self.logger.info("\t<< --click_element-- '%s' is Clickable. >>"%xpath)
            if self.driver.find_element_by_xpath(xpath).click() is None:
                self.logger.info("\t<< --click_element-- '%s' is Successful. >>"%xpath)
                return True
            else:
                self.logger.error("\t<< --click_element-- '%s' is Failed!! >>"%xpath)
                return False
        except Exception as ex:
            self.logger.error("==> !!ALERT!! --click_element-- Exception Occured. Exception Message is shown below :\n\t%s" %ex)
            return False
        

    def send_value(self, xpath, value):
        try:
            self.logger.info("==> Action:- [Enter text in Element] %s, %s "%(xpath,value))
            if not self.is_element_clickable(xpath):
                return False
            if self.driver.find_element_by_xpath(xpath).send_keys(value) is None:
                self.logger.info( "\t<< --send_value-- Send text '%s' to Element '%s' is Successful. >>"%(value,xpath))
                return True
            else:
                self.logger.error("\t<< --send_value-- Send text '%s' to Element '%s' is Failed!!. >>"%(value,xpath))
                return False
        except Exception as ex:
            self.logger.error("==> !!ALERT!! --send_value-- Exception Occured. Exception Message is shown below :\n\t%s" %ex)
            return False

    def clear_and_send_value(self,xpath,value):
        try:
            self.logger.info( "==> Action:- [Clear & Enter text in Element] %s, %s"%(xpath,value))
            if not self.is_element_clickable(xpath):
                return False
            if not self.driver.find_element_by_xpath(xpath).clear() is None:
                self.logger.info( "\t<< --clear_and_send_value-- Clear input in Element '%s' is Successful. >>"%(xpath))
                return False
            if self.driver.find_element_by_xpath(xpath).send_keys(value) is None:
                self.logger.info( "\t<< --clear_and_send_value-- Send text '%s' to Element '%s' is Successful. >>"%(value,xpath))
                return True
            else:
                self.logger.error("\t<< --clear_and_send_value-- Send text '%s' to Element '%s' is Failed!!. >>"%(value,xpath))
                return False
        except Exception as ex:
            self.logger.error("==> !!ALERT!! --clear_and_send_value-- Exception Occured. Exception Message is shown below :\n\t%s" %ex)
            return False


    def check_element_exists_by_xpath(self,xpath,wtime=10):
        try:
            self.driver.implicitly_wait(wtime)
            if len(self.driver.find_elements_by_xpath(xpath)) > 0:
                self.logger.info( "\t<< --check_element_exists_by_xpath-- The element %s exist >>" %xpath)
                self.driver.implicitly_wait(15)
                return True
            else:
                self.logger.error( "==> !!ALERT-FIX!! --check_element_exists_by_xpath-- The element %s does not exist. Please check!!" %xpath)
                self.driver.implicitly_wait(15)
                return False
        except NoSuchElementException:
            self.logger.error( "==> !!ALERT-FIX!! --check_element_exists_by_xpath-- NoSuchElementException Exception Occured for element %s. Please check!!" %xpath)
            self.driver.implicitly_wait(15)
            return False
            
            
    def get_current_url(self):
        # Get the element text value
        textValue = self.driver.current_url
        if not textValue:
            self.logger.error("Current URL does not have value. Please check")
            return False
        return textValue
        
    def is_element_clickable(self, xpath):
        try:
            
            if not self.waitobj.until(EC.presence_of_element_located((By.XPATH, xpath))):
                self.logger.error( "==> !!ALERT!! --is_element_clickable-- xpath '%s' is not located. Please check!!" %xpath)
                return False
            
            if not self.waitobj.until(EC.element_to_be_clickable((By.XPATH, xpath))):
                self.logger.error( "==> !!ALERT!! --is_element_clickable-- Element '%s' is not clickable. Please check!!" %xpath)
                return False
            
            return True
        except Exception as ex:
            self.logger.error( "==> !!ALERT!! --is_element_clickable-- Exception Occured. Exception Message is shown below :\n\t%s" %ex)
            return False


