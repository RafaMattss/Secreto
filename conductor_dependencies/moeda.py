from pyspark.sql.types import *

bq_table_name = "moeda"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"mo_codigomoeda": StringType,
	"mo_descricao": StringType,
	"mo_simbolo": StringType,
	"mo_id_moeda": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}