import os,sys

def init_global_var():
    global log_path
    global result_path
    global log_file
    global test_suite_path
    global suite_name
    global logger
    
    log_path = "/home/versa/sample_logs"
    log_file = "log.txt"
    test_suite_path = "/home/versa/sample_learn/suites/"
    suite_name = ''
    print(log_path)
    print(log_file)
    
    