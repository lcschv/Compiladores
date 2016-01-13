from sys import argv, exit

import sys
FIN = sys.argv[1]
FOUT = sys.argv[2]
if len(sys.argv) != 3:
	print "Parametros Errados\n"
	print "python.py nameTOKENSFILE"
	exit

filein = open(FIN, 'r')
fileout = open(FOUT,'w')
arquivo = []
tipo = ["int","float", "char", "string"]
getingin = ['print','read']
oplogicos = ["EQ","DIFF","LE","Lower","GE", "Greater", "ATTR"]
operators = ["ADD", "SUB", "MULT", "DIV", "MOD", "POW"]
expresao = []
contcond = 0
contwhile = 0
temelse = 0
def leitura():
	global arquivo
	for linha in filein:
		linha = linha.rstrip()
		arquivo += [linha]

leitura()

def declaracao(i):
	global arquivo
	global tipo
	corigelinha = i
	if arquivo[i+2].split(" ")[0] != "Semi":
		fileout.write("ATTR" + " " +str(arquivo[i+1].split(" ")[3]) + " " +str(arquivo[i+3].split(" ")[3])+ "\n")
		corigelinha +=4
	else:
		corigelinha+=3
	return corigelinha

def findexpresao(i):
	global arquivo
	global tipo
	global expresao
	expresao = []
	cont = 0
	corrigelinha = i
	recept = arquivo[i].split(' ')
	corrigelinha +=1
	linha = arquivo[corrigelinha].split(' ')
	while linha[0] != "Semi":
		if linha[0] == "ATTR":
			corrigelinha+=1
		elif linha[0] == "CONST":
			next_line = arquivo[corrigelinha+1].split(' ')
			linhaant = arquivo[corrigelinha-1].split(' ')
			if  next_line[0] == "Semi" and linhaant[0] == "ATTR":
				fileout.write("ATTR" + " " +str(recept[3])+" "+ linha[3]+ "\n")				
				corrigelinha += 1
				aux = 1
			else:
				expresao.append(linha[3])
				corrigelinha +=1
		elif linha[0] == "ID":
			expresao.append(linha[3])
			corrigelinha +=1
		elif linha[0] in operators:
			expresao.append(linha[0])
			corrigelinha +=1	
		else:
			print "Error na expressao da linha: ",recept[1]
			exit()		
		linha = arquivo[corrigelinha].split(' ')

	for j in range(len(expresao)):
		if expresao[j] =="ADD":
			fileout.write("ADD" + " " + "t1"+ " "+str(expresao[j-1])+" "+expresao[j+1] + "\n")
			expresao[j+1] = "t1"
		elif expresao[j] =="MULT":
			fileout.write("MULT" + " " + "t1"+ " "+str(expresao[j-1])+" "+expresao[j+1] + "\n")
			expresao[j+1] = "t1"
		elif expresao[j] =="DIV":
			fileout.write("DIV" + " " + "t1"+ " "+str(expresao[j-1])+" "+expresao[j+1] + "\n")
			expresao[j+1] = "t1"
		elif expresao[j] =="SUB":
			fileout.write("SUB" + " " + "t1"+ " "+str(expresao[j-1])+" "+expresao[j+1] + "\n")
			expresao[j+1] = "t1"
		elif expresao[j] =="MOD":
			fileout.write("MOD" + " " + "t1"+ " "+str(expresao[j-1])+" "+expresao[j+1] + "\n")
			expresao[j+1] = "t1"
		elif expresao[j] =="POW":
			fileout.write("POW" + " " + "t1"+ " "+str(expresao[j-1])+" "+expresao[j+1] + "\n")	
			expresao[j+1] = "t1"
		else:
			a=0
			
	fileout.write("ATTR" + " " +recept[3] + " " +"t1"+ "\n")
	return corrigelinha

def printread(i):
	corrigelinha = i
	linha = arquivo[i].split(" ")
	fileout.write(linha[0] + " " + arquivo[i+1].split(" ")[3] + "\n")
	corrigelinha+=2
	return corrigelinha

def condition(i, contcond):
	global temelse
	linha = arquivo[i].split(' ')
	test = 0
	corrigelinha = i
	corrigelinha +=3
	fileout.write(str(arquivo[corrigelinha].split(' ')[0]) + " " +"c"+str(contcond) +" "+str(arquivo[corrigelinha-1].split(' ')[3]) + " "+str(arquivo[corrigelinha+1].split(' ')[3]) +"\n")
	corrigelinha +=4
	aux = corrigelinha
	linhatest = arquivo[aux].split(' ')
	while linhatest[0] != "CloseBrace":
		aux +=1
		linhatest = arquivo[aux].split(' ')
	if aux+1 < len(arquivo) and arquivo[aux+1].split(' ')[0] == "else":
		fileout.write("JF"+" "+ "c"+str(contcond)+" "+"label"+str(contcond)+"\n")
		temelse =1
	else:
		fileout.write("JF"+" "+ "c"+str(contcond)+" "+"label"+str(contcond)+"\n")
		corrigelinha = aux+1
	return corrigelinha





def geracod():
	global arquivo
	global tipo
	global contcond
	global contwhile
	global temelse
	elsee = 0
	ifff = 0
	for i in range(len(arquivo)):
		linha = arquivo[i].split(" ")
		linhaant= arquivo[i-1].split(' ')
		if linha[0] in tipo:
			i = declaracao(i)
		elif linha[0] == "ID" and linhaant[0] not in tipo and linhaant[0] not in operators and arquivo[i+1].split(' ')[0] == "ATTR":
			i = findexpresao(i)
		elif linha[0] in getingin:
			i = printread(i)
		elif linha[0] == "if":
			i = condition(i,contcond)
			ifff += 1
		elif linha[0] == "else":
			fileout.write("label"+" "+ "label"+str(contcond)+"\n")
			contcond=+1
			elsee += 1
		elif linha[0] == "while":
			fileout.write("label"+" "+ "labelwhile"+str(contwhile)+"\n")
			auuxx= int(i)
		elif elsee == 1 and linha[0] == "CloseBrace":
			elsee -= 1
		elif ifff == 1 and linha[0]== "CloseBrace":
			if temelse !=1:
				fileout.write("label"+" "+ "label"+str(contcond)+"\n")
			ifff -= 1
			temelse -=1
		elif elsee == 0 and ifff == 0 and linha[0] == "CloseBrace":
			auuxx +=3
			fileout.write(str(arquivo[auuxx].split(' ')[0]) + " "+"w" +str(contwhile)+" " + str(arquivo[auuxx-1].split(' ')[3])+" "+str(arquivo[auuxx+1].split(' ')[3]) +"\n")
			fileout.write("JT "+"w"+str(contwhile)+" "+"labelwhile"+ str(contwhile)+"\n")
		else:
			a=1	
geracod()
