from pyspark.sql.types import *

bq_table_name = "seguro_parcela"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"par_id_parcelaseguro": IntegerType,
	"par_id_adesaoseguro": IntegerType,
	"par_no_parcela": IntegerType,
	"par_dt_vencimento": TimestampType,
	"par_vl_parcela": DoubleType,
	"par_tp_situacao": IntegerType,
	"par_dt_situacao": TimestampType,
	"par_dt_emissao": TimestampType,
	"par_tp_situacaocobranca": IntegerType,
	"par_tp_situacaotransferencia": IntegerType,
	"par_no_titulocapitalizacao": StringType,
	"par_fl_pagamentopdv": BooleanType,
	"par_dt_enviocobranca": TimestampType,
	"par_dt_postagemparcela": TimestampType,
	"par_dt_liquidacao": TimestampType,
	"par_tp_formapagamento": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
