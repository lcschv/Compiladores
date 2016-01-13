from sys import argv, exit

import sys
FIN = sys.argv[1]

if len(sys.argv) != 2:
	print "Parametros Errados\n"
	print "python.py nameTOKENSFILE"
	exit

filein = open(FIN, 'r')
idtable = []
tipo = ["int","float", "char", "string"]
operators = ["ADD", "SUB", "MULT", "DIV", "MOD", "POW"]
arquivo = []
dict_add = dict()


def tabelaConversao():
	global dict_add

	dict_add['int'] = dict()
	dict_add['float'] = dict()
	dict_add['string'] = dict()
	dict_add['char'] = dict()

	dict_add['int']['int'] = 'int'
	dict_add['int']['float'] = 'float'
	dict_add['int']['string'] = 0
	dict_add['int']['char'] = 0

	dict_add['float']['float'] = 'float'
	dict_add['float']['int'] = 'float'
	dict_add['float']['string'] = 0
	dict_add['float']['char'] = 0

	dict_add['string']['string'] = 'string'
	dict_add['string']['int'] = 0
	dict_add['string']['float'] = 0
	dict_add['string']['char'] = 0
tabelaConversao()

def checkDeclaracao():
	global arquivo
	global idtable
	for linha in filein:
		linha = linha.rstrip()
		arquivo += [linha]	
	for i in range(len(arquivo)):
		linha = arquivo[i].split(" ")
		if linha[0] in tipo:
			if arquivo[i+2].split(" ")[0] != "Semi":
				idtable += [{'type': linha[0] , 'id':arquivo[i+1].split(" ")[3], 'linha':linha[1], 'value':arquivo[i+3].split(" ")[3], 'inici':linha[1]}]				
				if linha[0] == 'int':
					if arquivo[i+3].split(" ")[4] != "i":
						print "Type error na linha:",linha[1], " tipo esperado era",linha[0],"."
						exit()
				elif linha[0] == "float":
					if arquivo[i+3].split(" ")[4] != "f":
						print "Type error na linha:",linha[1], " tipo esperado era",linha[0],"."
						exit()
				else:
					if arquivo[i+3].split(" ")[4] != "s":
						print "Type error na linha:",linha[1], " tipo esperado era",linha[0],"."
						exit()
			else:	
				idtable += [{'type': linha[0] , 'id':arquivo[i+1].split(" ")[3],'linha':linha[1], 'inici':0, 'value':0}]
	for k in range(len(idtable)):
		for j in range(k+1, len(idtable)):
			if (idtable[k]['id'] == idtable[j]['id']) and (idtable[k]['type'] != idtable[j]['type']):
				print "Error, a variavel: " + "'"+ idtable[j]['id'] +"'"+ " foi declarada duas vezes nas linhas: " + idtable[k]['linha'] +', '+ idtable[j]['linha'] + "."
				exit()
	
	for m in range(len(arquivo)):
		if arquivo[m][0:5] == "print":
			for i in range(len(idtable)):
				if idtable[i]["id"] == arquivo[m+1].split(' ')[3]:
					if (int(idtable[i]["linha"]) >= int(arquivo[m].split(' ')[1])):
						print  "Variavel :",idtable[i]["id"] ," foi usada antes de ser declarada"
						exit()
checkDeclaracao()
def checkInicializacao():
	global arquivo
	global idtable
	found = 0
	for i in range(len(arquivo)):
		linha = arquivo[i].split(" ")
		if linha[0] == "ID":
			for k in idtable:
				if linha[3] == k['id']:
					found = 1
					if int(linha[1]) < int(k['linha']):
						print "Variavel","'",linha[3],"'" ,"utilizada antes de ser declarada"
						exit()
			if found == 0:
				print "Variavel","'",linha[3],"'" , "nao declarada"
				exit()
			found = 0
checkInicializacao()

def checkTypes(i):
	global arquivo
	global idtable
	a = 0
	aux = 1
	expresao = []
	corrigelinha = i
	recept = arquivo[corrigelinha].split(' ')
	for k in range(len(idtable)):
			if idtable[k]['id'] == recept[3]:
				recepttipo= idtable[k]['type']
	corrigelinha +=1
	linha = arquivo[corrigelinha].split(' ')
	while linha[0] != "Semi":
		if linha[0] == "ATTR":
			corrigelinha+=1
		elif linha[0] == "CONST":
			next_line = arquivo[corrigelinha+1].split(' ')
			linhaant = arquivo[corrigelinha-1].split(' ')
			if  next_line[0] == "Semi" and linhaant[0] == "ATTR":
				for m in range(len(idtable)):
					if recept[3] == idtable[m]['id']:
						idtable[m]['value'] = linha[3]
				corrigelinha += 1
				aux = 1
			else:
				expresao.append(linha[4])
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
		for k in range(len(idtable)):
			if expresao[j] == idtable[k]['id']:
				expresao[j] = str(idtable[k]['type'])
			if expresao[j] == "i":
				expresao[j] = "int"
			if expresao[j] == "f":
				expresao[j] = "float"
			
	for j in range(len(expresao)):
		if expresao[j] == "ADD":
			if dict_add[expresao[j-1]][expresao[j+1]] == 0:
				print "Type Error, expressao nao pode ser realizada na linha: ",recept[1]
				exit()
			else:
				expresao[j+1] = dict_add[expresao[j-1]][expresao[j+1]]
		elif expresao[j] == "MULT":
			if (expresao[j-1] == 'string' or expresao[j-1] == 'char') or (expresao[j+1] == 'string' or expresao[j+1] == 'char'):
				print "Type Error, nao eh possivel multiplicar strings/char na linha: ",recept[1]
				exit()
			if dict_add[expresao[j-1]][expresao[j+1]] == 0:
				print "Type Error, nao foi possivel realizar expressao na linha:", recept[1]
				exit()
			else:
				expresao[j+1] = dict_add[expresao[j-1]][expresao[j+1]]
		elif expresao[j] == "SUB":
			if (expresao[j-1] == 'string' or expresao[j-1] == 'char') or (expresao[j+1] == 'string' or expresao[j+1] == 'char'):
				print "Type Error, nao eh possivel multiplicar strings/char na linha: ",recept[1]
				exit()
			if dict_add[expresao[j-1]][expresao[j+1]] == 0:
				print "Type Error, nao foi possivel realizar expressao na linha:", recept[1]
				exit()
			else:
				expresao[j+1] = dict_add[expresao[j-1]][expresao[j+1]]
		elif expresao[j] == "DIV":
			if (expresao[j-1] == 'string' or expresao[j-1] == 'char') or (expresao[j+1] == 'string' or expresao[j+1] == 'char'):
				print "Type Error, nao eh possivel multiplicar strings/char na linha: ",recept[1]
				exit()
			if dict_add[expresao[j-1]][expresao[j+1]] == 0:
				print "Type Error, nao foi possivel realizar expressao na linha:", recept[1]
				exit()
			else:
				expresao[j+1] = 'float'	
		else:
			a=0

	if aux != 0 and len(expresao)>0:
		if expresao[-1] != recepttipo:
			print "WARNING!!"
			print "Expressao da linha:", recept[1]
			print "Tipo esperado era: ", recepttipo, "mas expresao resulta:",expresao[-1]


	return int(corrigelinha)

def findAttrs():
	global arquivo
	global idtable
	for i in range(len(arquivo)):
		linha = arquivo[i].split(' ')
		linhaant= arquivo[i-1].split(' ')	
		if linha[0] == "ID" and linhaant[0] not in tipo and linhaant[0] not in operators and arquivo[i+1].split(' ')[0] == "ATTR":
			i = checkTypes(i)

findAttrs()



