from pyspark.sql.types import *

bq_table_name = "debito_recorrente"
columns_type = {
    "hash_key": StringType,
    "source": StringType,
    "cd_id_conta": IntegerType,
    "cd_id_tipodebitorecorrente": IntegerType,
    "cd_datainicio": TimestampType,
    "cd_datafim": TimestampType,
    "cd_status": IntegerType,
    "cd_arquivoenvio": StringType,
    "cd_combinacao": IntegerType,
    "cd_flagsinistro": IntegerType,
    "cd_dataultimopagamento": TimestampType,
    "cd_id_usuario": IntegerType,
    "cd_login": StringType,
    "cd_origem": StringType,
    "cd_numerociclo": IntegerType,
    "cd_id_promotorvenda": IntegerType,
    "cd_datafinalvigencia": TimestampType,
    "cd_contadornaopgto": IntegerType,
    "cd_contadornaopgtoconsec": IntegerType,
    "cd_flagpagamento": BooleanType,
    "cd_flagadesao": BooleanType,
    "cd_flagnumsorte": BooleanType,
    "cd_id_tipoenderecorisco": IntegerType,
    "cd_nomeestabelecimento": StringType,
    "cd_id_motivo": IntegerType,
    "cd_id_contadebitorecorrente": IntegerType,
    "cd_dataproximoenvio": TimestampType,
    "cd_parcelapedida": IntegerType,
    "td_id_tipodebitorecorrente": IntegerType,
    "td_descricao": StringType,
    "td_tipocarta": IntegerType,
    "td_valor": DoubleType,
    "td_flagestornoautomatico": BooleanType,
    "td_flagativo": BooleanType,
    "td_flagopcional": BooleanType,
    "td_numeroapolice": StringType,
    "td_flaggeranumerosorte": BooleanType,
    "td_vlrrepassadoseguradora": DoubleType,
    "td_flagseguro": BooleanType,
    "td_flaglancatransacao": BooleanType,
    "td_flagextratoincondicional": BooleanType,
    "td_flagdebitoincondicional": BooleanType,
    "td_flagadesaoautomatica": BooleanType,
    "td_faixaetaria": StringType,
    "td_sorteiosmensais": StringType,
    "td_descricaoapolice": StringType,
    "td_flagadereautomatico": BooleanType,
    "td_id_termoseguroservico": IntegerType,
    "td_flaginserefila": BooleanType,
    "td_id_produto": IntegerType,
    "td_qtdtentativascobranca": IntegerType,
    "td_id_ajustes": IntegerType,
    "td_condicoesgeraissiteportadorcredito": StringType,
    "td_flagtransfautomatica": BooleanType,
    "td_codigoprodutomapfre": StringType,
    "td_flaganuidadebonificada": BooleanType,
    "td_descricaoabreviada": StringType,
    "td_codigoclientemapfre": StringType,
    "td_codigoplanomapfre": StringType,
    "td_codigoempresamapfre": StringType,
    "td_valortitulomapfre": DoubleType,
    "td_flagdependente": BooleanType,
    "td_quantidadedependente": IntegerType,
    "td_id_grupo": IntegerType,
    "td_valorbonus": DoubleType,
    "td_numeroparcelas": IntegerType,
    "td_idademinima": IntegerType,
    "td_idademaxima": IntegerType,
    "dh_relatorio": TimestampType,
    "operation": StringType,
    "operation_sequence": IntegerType,
    "production_date": DateType,
}
