from pyspark.sql.types import *

bq_table_name = "embossing_mensagens"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"id_embossingmensagens": IntegerType,
	"descricao": StringType,
	"id_area": IntegerType,
	"flagsistema": BooleanType,
	"dh_relatorio": StringType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}