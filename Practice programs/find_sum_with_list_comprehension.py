import re
print (sum( [ int(x) for x in re.findall('[0-9]+',open('Files To Read/data_for_regex_assignment.txt').read()) ]))