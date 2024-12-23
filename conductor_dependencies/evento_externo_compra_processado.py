from pyspark.sql.types import *

bq_table_name = "evento_externo_compra_processado"
columns_type = {
    "hash_key": StringType,
    "source": StringType,
    "ee_id_eventocompra": IntegerType,
    "ee_id_origem": IntegerType,
    "ee_id_movimento": IntegerType,
    "ee_id_remessa": IntegerType,
    "ee_dataremessa": TimestampType,
    "ee_lote": IntegerType,
    "ee_numeroestabelecimento": IntegerType,
    "ee_dvnumeroestabelecimento": IntegerType,
    "ee_descricao": StringType,
    "ee_cartao": StringType,
    "ee_datacompra": TimestampType,
    "ee_codigoautorizacao": StringType,
    "ee_id_operacao": IntegerType,
    "ee_valorcompra": DoubleType,
    "ee_numeroparcelas": IntegerType,
    "ee_valorparcela": DoubleType,
    "ee_quantidademoeda": DoubleType,
    "ee_fatortotalajustado": DoubleType,
    "ee_fatorbancoajustado": DoubleType,
    "ee_fatortaxaadministracao": DoubleType,
    "ee_fatorcomissaogarantia": DoubleType,
    "ee_fatortotal": DoubleType,
    "ee_id_estabelecimento": IntegerType,
    "ee_datapagamentolojista": TimestampType,
    "ee_datafinanciamento": TimestampType,
    "ee_datamovimento": TimestampType,
    "ee_datavencimentocomprainicial": TimestampType,
    "ee_datavencimentocomprafinal": TimestampType,
    "ee_flagselecionado": IntegerType,
    "ee_flagrefinanciamento": IntegerType,
    "ee_tipocompra": IntegerType,
    "ee_tipopagamento": IntegerType,
    "ee_tipocalculoprestacao": IntegerType,
    "ee_tipoliquidacao": IntegerType,
    "ee_id_credor": IntegerType,
    "ee_valorcomissao": DoubleType,
    "ee_valorliquido": DoubleType,
    "ee_valorcontrato": DoubleType,
    "ee_valorencargostotais": DoubleType,
    "ee_valorencargosbancarios": DoubleType,
    "ee_valorgarantias": DoubleType,
    "ee_valoragenciamento": DoubleType,
    "ee_tipoentrada": StringType,
    "ee_taxajuros": DoubleType,
    "ee_valoriof": DoubleType,
    "ee_valortac": DoubleType,
    "ee_id_autorizacao": IntegerType,
    "ee_id_conta": IntegerType,
    "ee_dataentradacompra": TimestampType,
    "ee_primeiraparcela": DoubleType,
    "ee_origem": StringType,
    "ee_origemresolucao": StringType,
    "ee_status": IntegerType,
    "ee_datavencimentoreal": TimestampType,
    "ee_datavencimentopadrao": StringType,
    "ee_dataprocessamentolojista": TimestampType,
    "ee_carencia": IntegerType,
    "ee_id_contaportador": IntegerType,
    "ee_numerocontrato": StringType,
    "ee_id_borderaux": IntegerType,
    "ee_dataprocessamentolojista2": TimestampType,
    "ee_valorcomissao2": DoubleType,
    "ee_statuslojista": IntegerType,
    "ee_id_eventocompraorigem": IntegerType,
    "ee_codigomoeda": IntegerType,
    "ee_mcc": IntegerType,
    "ee_codigoacquiring": LongType,
    "ee_id_incoming": IntegerType,
    "ee_identificacaotransacao": StringType,
    "ee_id_estabelecimento_visa": IntegerType,
    "ee_nome_estabelecimento_visa": StringType,
    "ee_cicloconciliacao": IntegerType,
    "ee_codigomoedadestino": StringType,
    "ee_valordestino": DoubleType,
    "ee_valororigem": DoubleType,
    "ee_valortaxasaque": DoubleType,
    "ee_id_eventoexternoredecompartilhada": IntegerType,
    "ee_id_emissorredecompartilhada": IntegerType,
    "ee_id_estabelecimento_externo": IntegerType,
    "ee_id_cartao": IntegerType,
    "ee_pdv": StringType,
    "ee_databaixa": TimestampType,
    "ee_acquirereferencenumber": StringType,
    "ee_lifecicleauthorization": IntegerType,
    "ee_id_nivelseguranca": IntegerType,
    "ee_taxaembarque": DoubleType,
    "ee_valorentrada": DoubleType,
    "ee_descricaoitempedido": StringType,
    "ee_id_pedido": IntegerType,
    "ee_codautredecompartilhada": StringType,
    "dh_relatorio": TimestampType,
    "operation": StringType,
    "operation_sequence": IntegerType,
    "ee_transactionuuid": StringType,
    "ee_flagtransacaointernet": BooleanType,
    "ee_flagtransacaostandin": BooleanType,
    "ee_codestabelecimentocomercial": StringType,
    "ee_id_adquirente": IntegerType,
    "ee_valorsaqueapartado": DoubleType,
    "ee_cotacao": DoubleType,
    "ee_flagtransacaotokenizada": BooleanType,
    "ee_datavencpadrao": StringType,
    "production_date": DateType,
}