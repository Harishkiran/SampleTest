#import logger as log
import global_var
import logging
import os


class createTestReport(object):

    def __init__(self):
        self.html = global_var.log_path + '/Test_Results.html'
        
    def create_test_report_header(self):
        
        logpath = global_var.log_path
        logpath = os.path.expanduser(logpath)
        self.html = logpath + '/Test_Results.html'
        print('Setting up Result File at %s'%self.html)
        if not os.path.isfile(self.html):
            self.testreport = open(self.html, 'w+')
            title = '<html>\n<body>\n' 
            self.testreport.write(title)
            self.testreport.flush()
        else:
            self.testreport = open(self.html, 'a+')
        
    def create_test_report_table(self):
        table_header = '<table border="1" bgcolor="White"><tr bgcolor="#82f58f">'
        table_header = table_header + '<tr><td align="center" colspan="100%%" bgcolor="#82d5f5"><h3>suite: %s</h3></td></tr>' % global_var.suite_name
        table_header = table_header + '''           
                   <tr>
                       <th bgcolor="#F0F8FF">Test</th>
                       <th bgcolor="#F0F8FF">Test Case Summary</th>
                       <th bgcolor="#F0F8FF">Result</th>
                       <th bgcolor="#F0F8FF">Failure Reason</th>
                   </tr>\n'''
        self.testreport.write(table_header)
        self.testreport.flush()
        return True

    def write_to_test_report(self, data):
        self.testreport.write('<tr>\n')
        col_val = '<td align="left">%s</td>\n' % data['name']
        self.testreport.write(col_val)
        col_val='<td align="left">'
        for summary in data['summary'].split('\n'):
            col_val += '%s<br>' % summary
        col_val += '</td>\n' 
        self.testreport.write(col_val)
        if not data['result'] or data['result'] == 'FAIL':
            col_val = '<td align="center" bgcolor="red"><b>FAIL</b></td>\n'
            self.testreport.write(col_val)
        else:
            col_val = '<td align="center">PASS</td>\n'
            self.testreport.write(col_val)
        if data['comment'] != '':
            col_val='<td align="left"><FONT COLOR="red">'
            for comment in data['comment'].split('\n'):
                col_val += '%s<br>' % comment
            col_val += '</FONT></td>\n' 
            self.testreport.write(col_val)
        else:
            col_val = '<td align="left">NA</td>\n'
            self.testreport.write(col_val)
        self.testreport.write('</tr>\n')
        self.testreport.flush()


    def close_test_table_tag(self):
        self.testreport.write('</table>\n')
        self.testreport.flush()
        return True

    def close_test_report(self):
        footer = '''</body>
                    </html>'''
        self.testreport.write(footer)
        self.testreport.close()
        return True
