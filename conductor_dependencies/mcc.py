from pyspark.sql.types import *

bq_table_name = "mcc"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"mcc_codigomcc": IntegerType,
	"mcc_descricao": StringType,
	"mcc_id_grupomcc": IntegerType,
	"mcc_duracao": IntegerType,
	"mcc_percentualmin": DoubleType,
	"mcc_percentualmax": DoubleType,
	"mcc_intervalomatch": IntegerType,
	"gm_id_grupomcc": IntegerType,
	"gm_descricao": StringType,
	"gm_duracao": IntegerType,
	"gm_percentualmin": DoubleType,
	"gm_percentualmax": DoubleType,
	"gm_intervalomatch": IntegerType,
	"gm_descricaoextrato": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}