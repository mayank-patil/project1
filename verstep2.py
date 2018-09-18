import dns.resolver
addrtov = input("email : ")
host = addrtov.split('@')
domain=host[1]
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)
print(mxRecord)
