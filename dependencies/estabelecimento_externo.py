from pyspark.sql.types import *

bq_table_name = "estabelecimento_externo"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"ee_id_estabelecimento_visa": IntegerType,
	"ee_nome_estabelecimento_visa": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}