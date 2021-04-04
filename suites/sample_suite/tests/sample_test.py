import global_var
import unittest
import create_test_report
from selenium import webdriver

from sampleLoginPage import sampleLoginPage
#
#
#
#
class SampleTest(unittest.TestCase):    
    
    @classmethod
    def setUpClass(cls):
        
        
        global_var.create_test_report = create_test_report.createTestReport()
        global_var.create_test_report.create_test_report_header()
        global_var.create_test_report.create_test_report_table()
    @classmethod
    def tearDownClass(cls):
        # Suite Deconfig
        #cls.commonLibHdl.suite_deconfig()
        pass
        
    def setUp(self):
        self.logger = global_var.logger
        self.testresult = {}
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.sampleLoginPageHdl = sampleLoginPage(self.driver)
        
        
        
        
    def tearDown(self):
        self.driver.quit()
        global_var.create_test_report.write_to_test_report(self.testresult)
        
    def test_b(self):
        
        self.testresult['name'] = 'Test_B'
        self.testresult['summary'] = 'Login to Dummy Login Page and see if it reaches Example.com '
        
        if not self.sampleLoginPageHdl.verify_dummy_login():
            self.logger.error("Not able to verify Sample Login. Please check!!")
            self.testresult['result'] = 'FAIL'
            self.testresult['comment'] = ''
            self.assertTrue(False)
        
        else:
            self.logger.info("==> Verify Sample Login :- Passed. <==")
            self.testresult['result'] = 'PASS'
            self.testresult['comment'] = ''
            self.assertTrue(True)
        
    def test_a(self):
        self.testresult['name'] = 'Test_A'
        self.testresult['summary'] = 'Sample Passing test'
        self.testresult['result'] = 'FAIL'
        self.testresult['comment'] = 'Here,,This Can contain Error Logs'
        
        self.assertTrue(False)
