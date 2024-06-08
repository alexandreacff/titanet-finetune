# Titanet Finetune
Script para executar o ajuste fino do Titanet rapidamente

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Ambiente com python.
- Baixar pacotes pré-requisitos através do .sh de requirements:
```
source requirements.sh
```
> Testes realizados foram feiros utilizado a imagem docker `pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel`.

## 📌 Descrição dos Arquivos

- **run.sh**: Script Bash que verifica a existência do argumento de caminho do diretório e executa o script Python `titanet_finetune.py` com o caminho fornecido.
- **titanet_finetune.py**: Script Python que realiza o processo de fine-tuning do modelo Titanet utilizando os arquivos de manifestos JSON presentes no diretório fornecido.
- **requirements.sh**: Lista de dependências necessárias para executar o script `titanet_finetune.py`.
- **conf/titanet-finetune.yaml**: Arquivo de configuração YAML que define os parâmetros e hiperparâmetros para o processo de fine-tuning do modelo Titanet.


 ## ☕ Guia de Uso

### Passo 1: Clonar o Repositório

Clone o repositório para sua máquina local utilizando o comando:

```sh
git clone https://github.com/alexandreacff/titanet-finetune.git
cd titanet-finetune
```

### Passo 2: Garantir as Dependências

Certifique-se de que todas as dependências necessárias para o script Python `titanet_finetune.py` estejam instaladas. Você pode fazer isso utilizando uma imagem docker e instalando as dependências presentes em um arquivo `requirements.sh`:

```sh
docker run -it --rm --gpus-all --volume $PWD:/workspace --ipc host pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel bash
```

```sh
source requirements.sh
```

### Passo 3: Executar o Script

Para executar o script `run.sh`, forneça o caminho para o diretório que contém os arquivos de manifestos JSON. Por exemplo:

```sh
source run.sh /caminho/para/seu/diretorio_de_arquivos
```

 
