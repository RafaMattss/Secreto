from pyspark.sql.types import *

bq_table_name = "tipo_origem_resolucao_bandeira"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"tbd_id_tipoorigemresolucao": IntegerType,
	"tbd_sigla": StringType,
	"tbd_descricao": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
