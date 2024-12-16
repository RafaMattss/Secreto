from pyspark.sql.types import *

bq_table_name = "adesao_debito_automatico"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"id": IntegerType,
	"dataadesao": TimestampType,
	"id_contadigital": IntegerType,
	"id_contacredito": IntegerType,
	"id_tipodebitoautomatico": IntegerType,
	"descricaotipodebitoautomatico": StringType,
	"responsavel": StringType,
	"datacancelamento": TimestampType,
	"responsavelcancelamento": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}