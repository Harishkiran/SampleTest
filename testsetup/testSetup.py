import sys
import paths
import os
import global_var
import datetime
import logging
import unittest
from suites_def import DefineSuite
  
suite = 'sample_suite'

class TestSetup():
    def __init__(self):
        
        global_var.init_global_var()
        self.SetupLogPath()
        self.log_file = self.log_path + "/" + global_var.log_file
        self.logger = logging.getLogger('Test')
        self.logger.setLevel(logging.DEBUG)
        self.addLogHandler(self.log_file, 'Test', logging.DEBUG)
        global_var.logger = self.logger
        self.runSubSuite(suite)
        
    def SetupLogPath(self):
        self.log_path = global_var.log_path
        if (not os.path.isdir(self.log_path)):
            self.makeLogPath(self.log_path)
        
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.datetime.now().strftime('%H-%M-%S')
        
        self.log_path += '/'+str(current_date)
        if (not os.path.isdir(self.log_path)):
            self.makeLogPath(self.log_path)
            
        self.log_path += '/'+current_time
        if (not os.path.isdir(self.log_path)):
            self.makeLogPath(self.log_path)
            
        global_var.log_path = self.log_path
        global_var.result_path = self.log_path
        
    def makeLogPath(self,path):
        try:
            os.makedirs(path)
            os.chmod(path, 0777)
            print("Created log path %s" %path)
        except Exception as ex:
            print("ERROR::An exception occurred in makeLogPath" + str(ex))
            exit(0)
        
    def addLogHandler(self, logFile,logger_name='Test',loglevel=logging.DEBUG):
        try:
            hdlr = logging.FileHandler(logFile)
            
            formatter = logging.Formatter('%(asctime)s %(levelname)s (%(threadName)-10s) %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
            hdlr.setFormatter(formatter)
            hdlr.setLevel(loglevel)
            self.logger.addHandler(hdlr)
            return hdlr
        except Exception as ex:
            print("ERROR::An exception occurred while adding log handlers" +str(ex))
            exit(0)
            
            
    def runSubSuite(self,suite):
        try:
            
            global_var.suite_name = suite
            test_suite = unittest.TestSuite()
            suite_attr = DefineSuite().get_suite_attributes(suite)
            module = __import__(suite_attr['module'])
            class_name = suite_attr['class']
            suite_class = getattr(module,class_name)
            for test_case in suite_attr['testcases']:
                self.logger.info(" -- Adding Test Case : %s"%test_case)
                test_suite.addTest(suite_class(test_case))
            runner = unittest.TextTestRunner()
            
            runner.run(test_suite)
            
        except Exception as ex:
            print("RunTest :: runSubSuite :: An exception occurred %s" % ex)
            self.logger.error("RunTest :: runSubSuite :: An exception occurred %s" % ex)
            return False

if __name__ == '__main__':
    TestSetup()
    
