from pyspark.sql.types import *

bq_table_name = "desbloqueio_cartao"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"dc_id_cartao": IntegerType,
	"dc_cartao": StringType,
	"dc_codigodesbloqueio": StringType,
	"dc_datahora": TimestampType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}