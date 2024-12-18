from pyspark.sql.types import *

bq_table_name = "limite_portador"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"lp_id_limiteportador": IntegerType,
	"lp_id_conta": IntegerType,
	"lp_portador": IntegerType,
	"lp_limite": DoubleType,
	"lp_disponivel": DoubleType,
	"lp_id_usuario": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}