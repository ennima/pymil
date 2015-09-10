import subprocess,datetime,os


def ping(hostname_):
	hostname = hostname_ #example
	response = os.system("ping " + hostname)

	#and then check the response...
	if response == 0:
	  #print hostname, 'is up!'
	  return True
	else:
	  #print hostname, 'is down!'
	  return False

print(ping("127.0.3.3"))