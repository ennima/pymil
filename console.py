import subprocess,datetime

exitCmd = "rasp-quit"
salir = False
print("\n\nBienvenido USUARIO_ADMIN al panel de administracion de ennima_rasp.\n \n")
while (salir!=True):
	
	## 1.- Lee el comando
	#cmd = raw_input("#ADMIN: ")
	file_cmd = open("cmd.txt","r")
	cmd = file_cmd.read()
	file_cmd.close()
	
	##2.- Ejecuta el comando
	if(cmd!=""):
		print("#: "+cmd)
		if(cmd == exitCmd):
			print("bye")
			salir = True

		cmdArr = cmd.split(" ")
		#print(cmdArr)

		p = subprocess.Popen(cmdArr,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p.communicate()
		
		## Salida del comando
		print (out)
		print ("#Error: "+err)
		file_cmd = open("cmd.txt","w")
		cmd = file_cmd.write("")
		file_cmd.close()

