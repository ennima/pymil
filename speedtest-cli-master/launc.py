import subprocess,datetime

def getSpeedTest():
	print ("Check speed...")
	p = subprocess.Popen(['python', 'speedtest_cli.py','--simple'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	print out

	data = out.split('\n')
	print "Data: ",data
	downSpeed = data[1].split(' ')
	downSpeed_val =downSpeed[1]
	downSpeed_unit = downSpeed[2]
	print "#Download Speed: ",downSpeed_val,"unit: ",downSpeed_unit



#Secuencia de arranque
inicio1 = datetime.datetime.now()

#Despliega un loader
p = subprocess.Popen(['play', 'test.jpg', '-fs'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#out, err = p.communicate()
#Corre un speed test
getSpeedTest()

#Quita el loader
p.terminate()

final1 = datetime.datetime.now()
delta1 = final1 - inicio1
print ("Speed Tarda: ",str(delta1))
#print err