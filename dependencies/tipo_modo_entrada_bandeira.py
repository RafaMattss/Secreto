from pyspark.sql.types import *

bq_table_name = "tipo_modo_entrada_bandeira"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"meb_codigo": StringType,
	"meb_descricao": StringType,
	"meb_id_bandeira": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
