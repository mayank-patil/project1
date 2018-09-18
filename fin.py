#library
import re as e
import dns.resolver
import socket as soc
import smtplib as sl
import csv
#enter Address to verify
f = open('test.csv')
csv_f = csv.reader(f)

for row in csv_f:
    addrtov = row[0]
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
    server.connect('ruttiest.com', 2525)
    server.login('ruttiest', 'xpldN0DcFHBm7qtnlo')

# SMTP Conversation
    server.connect(mxRecord)
    server.helo(domain)
    server.mail('dav22mark@gmail.com')
    code, message = server.rcpt(str(addrtov))
    server.quit()
#print(message)
# Assume 250 as Success
    if code == 250:
        print('Success')
    else:
        print('Bad')
