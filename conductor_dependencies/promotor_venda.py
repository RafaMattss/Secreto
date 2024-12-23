from pyspark.sql.types import *

bq_table_name = "promotor_venda"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"id_promotorvenda": IntegerType,
	"nome": StringType,
	"apelido": StringType,
	"cpf": StringType,
	"datainclusao": TimestampType,
	"id_usuario": IntegerType,
	"id_emissor": IntegerType,
	"chapa": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": StringType,
	"production_date": DateType,
}
