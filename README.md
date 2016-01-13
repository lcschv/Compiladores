
						Gerador de código + Compilador

Implementado para a disciplina de Compiladores no curso de Ciência da Computação da Universidade Federal de São João del Rei.

Aluno: Lucas Chaves Lima

Objetivo: 
	O objetivo deste trabalho foi implementar um analisador sintático para a  linguagem c ( com algumas modificações). 

Motivação:
	Este analisador deve servir de base para o analisador semântico que será desenvolvidofuturamente. Para isso o analisador léxico deve  retornar uma lista de tokens da linguagem, dado essa lista de tokens retornada pelo analisador léxico, o analisador sintático nos retorna se o código possue algum erro na forma, ou seja, se essa lista de tokens é um codigo compilável ou não.

Como compilar: 
	É necessário ter em seu computador o interpretador da linguagem Python.

	No terminal linux o comando para compilar/interpretar:
		sh runCompiler.sh Arquivodeentrada ArquivoSaidaTokens CodigoGerado
