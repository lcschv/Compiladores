from sys import argv, exit

import sys
FIN = sys.argv[1]

if len(sys.argv) != 2:
	print "Parametros Errados\n"
	print "python.py nameTOKENSFILE"
	exit

filein = open(FIN, 'r')

oplogicos = ["EQ","DIFF","LE","Lower","GE", "Greater", "ATTR"]
tipo = ["int","float", "char", "string"]
operators = ["ADD", "SUB", "MULT", "DIV", "MOD", "POW"]
parenteses = ["OpenPar", "ClosePar"]
brace = ["OpenBrace", "OpenBrace"]

#Faz verificacao das declaracoes
#declaracoes podem ser do tipo int/float a = 0; 
#ou int/float a;
def declaracao():
	global j
	global line
	if j+1 >= len(vetor):
				print "error, nao encontrado ID"
				exit(0)
	next_line = vetor[j+1].split(" ")
	global corrigelinha
	corrigelinha = j + 1
	if next_line[0] == "ID" and next_line[1] == line [1]:
		if j+2 >= len(vetor):
				print "error, nao encontrado ATTR"
				exit(0)
		next_line = vetor[j+2].split(" ")
		corrigelinha += 1
		if next_line[0] == "Semi" and next_line[1] == line [1]:   #Declaracao normal int i;
			corrigelinha += 1
		elif next_line[0] == "ATTR" and next_line[1] == line [1]:		#Declaracao com atribuicao int i = 0;
			if j+3 >= len(vetor):
				print "error, nao encontrado const"
				exit(0)
			corrigelinha -=1
			attr()
		else:
			print "Error na SemiColon na linha:", next_line[1],"!\n"
			exit(0)
	else:
		print "Error na linha:", next_line[1], "Nao foi encontrado ID, para declaracao tipo ID; ou tipo id = num; \n"
		corrigelinha = j
		exit(0)

#Realiza a verificacao das atribuicoes do codigo
#atribuicoes podem ser constantes ou IDS
def attr():
	global corrigelinha
	j = corrigelinha
	if j+1 >= len(vetor):
				print "error, nao encontrado const"
				exit(0)
	next_line = vetor[j+1].split(" ")
	corrigelinha = j + 1
	if next_line[0] == "ATTR" and next_line[1] == line [1]:		#Declaracao com atribuicao int i = 0;
		if j+2 >= len(vetor):
				print "error, nao encontrado valor para atribuir"
				exit(0)
		next_line = vetor[j+2].split(" ")
		corrigelinha +=1
		if (next_line[0] == "CONST" or next_line[0] =="ID") and next_line[1] == line [1]:   #verifica atribuicao de Const ou ID
			if j+3 >= len(vetor):
				print "error, nao encontrado SEMI"
				exit(0)
			next_line = vetor[j+3].split(" ")
			if next_line[0] == "Semi" and next_line[1] == line [1]:
				corrigelinha +=1
			else:
				Expr()
			

		elif next_line[0] == "texto" and next_line[1] == line [1]:   #Verifica atribuicao de string
			if j+3 >= len(vetor):
				print "error, nao encontrado SEMI"
				exit(0)
			next_line = vetor[j+3].split(" ")
			corrigelinha += 1
			if next_line[0] == "Semi" and next_line[1] == line [1]:
				corrigelinha +=1
			else:
				print "Error na SemiColon na linha:", next_line[1],"!\n"
				exit(0)
		else:
			print "Error na atribuicao na linha:", next_line[1],", constante para atribuicao nao encontrada!\n"
			exit(0)
	else:
		Expr()

# Realiza verificacao de expressao, apenas aceita expressao simples ID operador ID
# ou id op const;
# const op const;
def Expr():
	global corrigelinha
	j = corrigelinha
	line = vetor[j].split(" ")
	term = line[0]
	if term == "ID" or term == "CONST":
		if j+1 >= len(vetor):
					print "error, nao encontrado SEMI"
					exit(0)
		next_line = vetor[j+1].split(" ")
		corrigelinha += 1
		if next_line[0] in operators and next_line[1] == line [1]:
			next_line = vetor[j+2].split(" ")
			corrigelinha +=1
			if (next_line[0] == "ID" or next_line[0] == "CONST") and next_line[1] == line [1]:
				if j+3 >= len(vetor):
					print "error, nao encontrado SEMI"
					exit(0)
				next_line = vetor[j+3].split(" ")
				corrigelinha += 1
				if next_line[0] == "Semi" and next_line[1] == line [1]:
					corrigelinha +=1
					j = corrigelinha
					return True
				elif next_line[0] in operators and next_line[1] == line [1]:
					corrigelinha+=1
					Expr()
			else:
				print "Error, nao foi encontrado segundo ID ou Const"
				exit(0)
		elif next_line[0] == "Semi" and next_line[1] == line [1]:
			corrigelinha +=1
			return True
		elif next_line[0] == "ATTR" and next_line[1] == line[1]:
			next_line = vetor[j+2].split(" ")
			corrigelinha +=1
			if (next_line[0] == "ID" or next_line[0] == "CONST") and next_line[1] == line [1]:
				if j+3 >= len(vetor):
					print "error, nao encontrado SEMI"
					exit(0)
				next_line = vetor[j+3].split(" ")
				corrigelinha += 1
				if next_line[0] == "Semi" and next_line[1] == line [1]:
					corrigelinha +=1
					j = corrigelinha
					return True
				elif next_line[0] in operators and next_line[1] == line [1]:
					corrigelinha+=1
					Expr()

		else:
			print "Errorrr na linha: ", line[1], "!\n"
			exit(0)
	else:
		print "Error, nao achou ID para atribuir"
		exit(0)

# Realiza o print ID; ou print "texto";
def printing():
	if j+1 >= len(vetor):
		print "error, nao encontrado ID"
		exit(0)
	next_line = vetor[j+1].split(" ")
	global corrigelinha
	corrigelinha = j + 1
	if (next_line[0] == "ID" or next_line[0] == "texto") and next_line[1] == line [1]:
		if j+2 >= len(vetor):
			print "Faltando SemiColon na linha:", next_line[1], "!\n"
			exit(0)
		next_line = vetor[j+2].split(" ")
		corrigelinha +=1
		if next_line[0] == "Semi" and next_line[1] == line [1]:
			corrigelinha +=1
		else:
			print "Faltando SemiColon na linha:", next_line[1], "!\n"
			exit(0)
	else:
		print "Nao foi encontrado nada para printar na linha:" , next_line[1], "!\n" 
		exit(0)

#  Realiza o read ID;
def reading():
	if j+1 >= len(vetor):
		print "error, nao encontrado ID"
		exit(0)
	next_line = vetor[j+1].split(" ")
	global corrigelinha
	corrigelinha = j + 1
	if (next_line[0] == "ID") and next_line[1] == line [1]:
		if j+2 >= len(vetor):
			print "Faltando SemiColon na linha:", next_line[1], "!\n"
			exit(0)
		next_line = vetor[j+2].split(" ")
		corrigelinha +=1
		if next_line[0] == "Semi" and next_line[1] == line [1]:
			corrigelinha +=1
		else:
			print "Faltando SemiColon na linha:", next_line[1], "!\n"
			exit(0)
	else:
		print "Nao foi encontrado nada para read na linha:" , next_line[1], "!\n"  
		exit()
#verifica se a condicao esta do formato (a oplogico b)
def ExprCond():
	global corrigelinha
	j = corrigelinha
	line = vetor[j].split(" ")
	term = line[0]
	if term == "ID" or term == "CONST":
		next_line = vetor[j+1].split(" ")
		corrigelinha += 1
		if next_line[0] in oplogicos and next_line[1] == line [1]:
			next_line = vetor[j+2].split(" ")
			corrigelinha +=1
			if (next_line[0] == "ID" or next_line[0] == "CONST") and next_line[1] == line [1]:
				if j+3 >= len(vetor):
					print "error, nao encontrado fecha parenteses"
					exit(0)
				next_line = vetor[j+3].split(" ")
				corrigelinha += 1
				if next_line[0] == "ClosePar" and next_line[1] == line [1]:
					corrigelinha +=1
					j = corrigelinha
					return True
				else:
					print "nao encontrou ClosePar na linha:", line[1]
					exit(0)
			else:
				print "Nao foi encontrado ID ou Constante na condicao na linha:",line[1]
				exit(0)
		else:
			"Nao foi encontrado operador logico na linha:", line[1]
			exit(0)
	else:
		print "Nao foi encontrado o ID na linha:", line[1]
		exit(0)
#verifica se ha abertura de parenteses, 
#se tem parenteses ele chama a exprCond para verificar
#se tiver certo abre um novo contexto 
def cond():
	global corrigelinha, p
	j = corrigelinha
	line = vetor[j].split(" ")
	term = line[0]
	if term == "if" or term == "while":
		next_line = vetor[j+1].split(" ")
		corrigelinha +=1
		if next_line[0] == "OpenPar" and next_line[1] == line[1]:
			next_line = vetor[j+2].split(" ")
			corrigelinha +=1
			ExprCond()
			j = corrigelinha
			next_line = vetor[j].split(" ")

			if next_line[0] == "OpenBrace":
				corrigelinha +=1
				codigo()
				j = corrigelinha
				if j >= len(vetor):
					#print "Error, nao encontrado CloseBraces"
					exit(0)
				next_line = vetor[j].split(" ")
				if next_line[0] == "CloseBrace":
					corrigelinha +=1
				else:
					print "Faltou fechar chaves"
					exit(0)
			else:
				print "Faltou Open Braces na linha:", line[1]
				exit(0)
		else:
			print "Error, Parenteses nao encontrado na condicao na linha: ", line[1]
			exit(0)
		exit(0)
	else:
		exit(0)


#REALIZA LEITURA DO ARQUIVO E SALVA EM UM VETOR LINHA A LINHA
vetor = []
linha = 0
line = []
corrigelinha = 0
p = 0
j= 0
j = 0
for i in filein:
	i=i.rstrip()
	vetor += [i.strip()]

#REALIZA LEITURA LINHA A LINHA DO ARQUIVO
def codigo():
	global j
	global line
	j = corrigelinha
	while j < len(vetor):
		line = vetor[j].split(" ")
		token = line[0]
		if token in tipo:
			declaracao()
			j = corrigelinha
		elif token == "ID":
			attr()
			j = corrigelinha
		elif token == "print":
			printing()
			j = corrigelinha
		elif token == "read":
			reading()
			j = corrigelinha
		elif token == "if":
			cond()
			j = corrigelinha
		elif token == "while":
			cond()
			j = corrigelinha
		elif token == "else":
			p = j
			cond()
			j = corrigelinha
		else:
			j +=1
codigo()
