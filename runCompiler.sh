#!/bin/bash       

CODEFILEIN=$1;
TOKENSFILE=$2;
outfile=$3;

echo "Executando Analisador Lexico ..."
python lexico.py $CODEFILEIN $TOKENSFILE

echo "Executando Analisador sintatico ..."
python sintatico.py $TOKENSFILE

echo "Executando Analisador semantico ..."
python semantico.py $TOKENSFILE

echo "Executando Gerador de codigo ..."
python gerador.py $TOKENSFILE $outfile
