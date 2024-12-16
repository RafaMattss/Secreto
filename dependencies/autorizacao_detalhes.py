from pyspark.sql.types import *

bq_table_name = "autorizacoes_detalhes"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"id": LongType,
	"uuid": StringType,
	"jarvis_score": IntegerType,
	"fraude_score": IntegerType,
	"fraude_rule_score": IntegerType,
	"fraude_reason_code": IntegerType,
	"fraude_reason_code2": IntegerType,
	"fraude_reason_code3": IntegerType,
	"cidade": StringType,
	"pais": StringType,
	"cep": StringType,
	"token": StringType,
	"id_token": LongType,
	"data_autorizacao": StringType,
	"indicador_comercio_eletronico": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
