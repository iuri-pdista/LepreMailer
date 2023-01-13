#!/bin/bash

if [[ $LEPRESENHA = "" ]]; then
	echo "Variavel n/ existente. Criando..."
	export LEPRESENHA="lepresenha2023"
else 
	echo "Variavel ja existente: $LEPRESENHA"
fi
#SHELL
