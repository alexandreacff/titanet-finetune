#!/bin/bash

# Verifica se o argumento $1 (manifest path) foi fornecido
if [ -z "$1" ]; then
    echo "Erro: Por favor, forneça o diretório dos manifests (.json) como argumento."
    echo "Exemplo de uso: $0 /caminho/para/seu/diretorio_de_arquivos"
    exit 1
fi

DATA_DIR="$1"
NUM_CLASSES=12459

python3 titanet_finetune.py $DATA_DIR $NUM_CLASSES
