#library
import re as e
import dns.resolver
import socket as soc
import smtplib as sl
#enter Address to verify
addrtov = input("enter Email : ")
#specifying regular expression
verified = e.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addrtov)

if verified == None:
    print('Bad Syntax')
else:
    print("Format : OK")

# Get local server hostname
#host = "brickin.info"
#host = "hotmail.com"
host = addrtov.split('@')
domain=host[1]
records = dns.resolver.query(domain , 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)
print(mxRecord)

# SMTP lib setup
server = sl.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(domain)
server.mail('dav22mark@gmail.com')
code, message = server.rcpt(str(addrtov))
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Bad')
