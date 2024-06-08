# Titanet Finetune
Script para executar o ajuste fino do Titanet rapidamente

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Ambiente com python.
- Baixar pacotes pré-requisitos através do .sh de requirements:
```
source requirements.sh
```
> Testes realizados foram feiros utilizado a imagem docker X.

 ## ☕ Guia de Uso

## Descrição dos Arquivos

- **run.sh**: Script Bash que verifica a existência do argumento de caminho do diretório e executa o script Python `titanet_finetune.py` com o caminho fornecido.
- **titanet_finetune.py**: Script Python que realiza o processo de fine-tuning do modelo Titanet utilizando os arquivos de manifestos JSON presentes no diretório fornecido.
- **requirements.sh**: Lista de dependências necessárias para executar o script `titanet_finetune.py`.
- **conf/titanet-finetune.yaml**: Arquivo de configuração YAML que define os parâmetros e hiperparâmetros para o processo de fine-tuning do modelo Titanet.


### Passo 1: Clonar o Repositório

Clone o repositório para sua máquina local utilizando o comando:

```sh
git clone https://github.com/alexandreacff/titanet-finetune.git
cd titanet-finetune
```

### Passo 2: Garantir as Dependências

Certifique-se de que todas as dependências necessárias para o script Python `titanet_finetune.py` estejam instaladas. Você pode fazer isso criando um ambiente virtual e instalando as dependências listadas em um arquivo `requirements.txt` (caso disponível):

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Passo 3: Executar o Script

Para executar o script `run.sh`, forneça o caminho para o diretório que contém os arquivos de manifestos JSON. Por exemplo:

```sh
source run.sh /caminho/para/seu/diretorio_de_arquivos
```

 
