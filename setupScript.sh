#!/bin/bash

if [[ $LEPRESENHA = "" ]]; then
	echo "Variavel n/ existente. Criando..."
	export LEPRESENHA="zyixpaabciohafkg"
else 
	echo "Variavel ja existente: $LEPRESENHA"
fi
#SHELL
