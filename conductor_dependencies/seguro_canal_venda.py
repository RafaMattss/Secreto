from pyspark.sql.types import *

bq_table_name = "seguro_canal_venda"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"id_canalvenda": IntegerType,
	"cd_canalvenda": StringType,
	"nm_canalvenda": StringType,
	"fl_canalpadrao": BooleanType,
	"id_emissor": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
