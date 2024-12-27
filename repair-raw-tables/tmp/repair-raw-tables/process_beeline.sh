#!/bin/bash

# Verifica se algum parametro foi informado
if [[ "$1" == "" ]]; then
    echo "ERRO: informe o caminho do arquivo a partir do diretorio UnificacaoProcon!" && exit;
fi

# Arquivo que sera executado
arquivo=$1

# Faz um split por '/' em $arquivo; pega o nome e extensao
if [[ $arquivo == *"/"* ]]; then
    IFS='/' read -r -a array <<< "$arquivo"
    indice_max=$((${#array[@]} - 1));
    nome_processo="${array[$indice_max]}"
else
    nome_processo=$arquivo
fi

# Faz um split por '.' em $nome_processo; deixa de fora a extensao do arquivo
if [[ $nome_processo == *"."* ]]; then
    IFS='.' read -r -a array <<< "$nome_processo"
    nome_tmptable_processo="${array[0]}"
fi

# Pega o diretorio de execucao do script 'process_beeline'
diretorio_execucao=$(readlink -f "$0")
diretorio_execucao=$(dirname "$diretorio_execucao")

# Carrega as variaveis e funcoes necessarias
parametros=$diretorio_execucao"/setup/parametros.ini"
configuracoes=$diretorio_execucao"/setup/config.sh"
source $parametros
source $configuracoes

# Pegando o caminho do HQL
script_hql=$(get_script_hql)

# Pegando o caminho dos logs
script_log=$(get_script_log)

# Faz a execucao do hql
# execucao_padrao_beeline |& tee $(get_arquivo_log)
if [[ $use_process_log == true ]]; then
    # Executa o hql e gera os logs de inicio e fim
    execucao_padrao_beeline && echo "$arquivo finalizado!"
else
    # Executa o hql sem gerar logs
    execute_beeline && echo "$arquivo finalizado!"
fi