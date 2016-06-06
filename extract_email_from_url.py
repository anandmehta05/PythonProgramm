import re
def Find(pat,text):
	match=re.match(pat,text)
	if match:
		print match.group()
	else:
		print "Not Found"
Find(r'[\w.]+@[\w.]+','https:\\www.github.com\er.anandmehta.com')