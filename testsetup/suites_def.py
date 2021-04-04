class DefineSuite(object):
    
    class_defns = {
        'sample_suite' :
            {
            'module':'sample_test',
            'class':'SampleTest',
            'testcases':['test_a','test_b']
            }
    }
    
    def get_suite_attributes(self,suite):
        return self.class_defns[suite]
        
    
