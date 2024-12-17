from pyspark.sql.types import *

bq_table_name = "dado_bancario_conta"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"db_id_conta": IntegerType,
	"db_banco": IntegerType,
	"db_agencia": IntegerType,
	"db_contacorrente": StringType,
	"db_dvagencia": IntegerType,
	"db_dvcontacorrente": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"db_id_tipocontabancaria": IntegerType,
	"production_date": DateType,
}
