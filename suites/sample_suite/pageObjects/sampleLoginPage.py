import logging
import global_var
#import parse_xml
import re
import time
#
from CommonUtil import CommonUtil
from sampleValue import sampleValue
from sampleLoginLocator import sampleLoginLocator

class sampleLoginPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.logger = global_var.logger
        self.commonUtilHdl = CommonUtil(self.driver)
        self.page_url = 'http://www.stealmylogin.com/demo.html'
        self.driver.get(self.page_url)
        
        
    def verify_dummy_login(self):
        result = True
        
        
        #Step - 1 Enter Login UserName
        if not self.commonUtilHdl.send_value(sampleLoginLocator.sample_page_login_username_field_xpath,sampleValue.sample_password_value):
            self.logger.error("Not able to send User Name Value. Please check!!")
            result = False
            
        else:
            self.logger.info("Entering Username Successful")
            print('Done')
            #self.commonUtilHdl.captureScreenshot('after_clicking_card_view_button')
        
        #Step - 2 Enter Login Password
        if not self.commonUtilHdl.send_value(sampleLoginLocator.sample_page_login_password_field_xpath,sampleValue.sample_password_value):
            self.logger.error("Not able to send Password Value. Please check!!")
            result = False
            
        else:
            self.logger.info("Entering Password Successful")
            #self.commonUtilHdl.captureScreenshot('after_clicking_card_view_button')
        
        #Step - 3 Click on Login Button
        if not self.commonUtilHdl.click_element(sampleLoginLocator.sample_page_login_button_xpath):
            self.logger.error("Not able to Click on Login Button. Please check!!")
            result = False
            
        else:
            self.logger.info("Clicking on Login Button Successful!!")
            #self.commonUtilHdl.captureScreenshot('after_clicking_card_view_button')
        
        
        #Step - 4  Button
        time.sleep(10)
        if not sampleValue.expected_url in self.commonUtilHdl.get_current_url(): 
            self.logger.error("Current URL and Expected URL does'nt match. Please check!!")
            result = False
            
        else:
            self.logger.info("Current URL and Expected URL Matching.!!")
            #self.commonUtilHdl.captureScreenshot('after_clicking_card_view_button')
        
        
        
        return result
        
        
