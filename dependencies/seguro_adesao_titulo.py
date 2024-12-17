from pyspark.sql.types import *

bq_table_name = "seguro_adesao_titulo"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"at_id_adesaoseguro": IntegerType,
	"at_no_titulocapitalizacao": StringType,
	"at_cd_identificacao": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
