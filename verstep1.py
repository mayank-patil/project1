#importing regular expression
import re as e
#enter Address to verify
addrtov = input("enter Email : ")
#specifying regular expression
verified = e.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addrtov)

if verified == None:
    print('Bad Syntax')
else:
    print("Format : OK")
