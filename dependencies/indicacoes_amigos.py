from pyspark.sql.types import *

bq_table_name = "indicacoes_amigos"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"ia_id": IntegerType,
	"ia_id_conta": IntegerType,
	"ia_codigo": StringType,
	"ia_datacriacao": TimestampType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": StringType,
	"production_date": DateType,
}