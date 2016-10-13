import re

txt='    Minimum = 5ms, Maximum = 13ms, Average = 6ms'

re1='.*?'	# Non-greedy match on filler
re2='(\\d+)'	# Integer Number 1

rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    int1=m.group(1)
    print "("+int1+")"+"\n"

#-----
# Paste the code into a new python file. Then in Unix:'
# $ python x.py
#-----