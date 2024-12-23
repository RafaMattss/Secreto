from pyspark.sql.types import *

bq_table_name = "adesao_pacote_tarifa"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"ac_id_conta": IntegerType,
	"pt_id_pacotetarifa": IntegerType,
	"pt_descricaopacotetarifa": StringType,
	"ac_valortarifa": DoubleType,
	"ac_dataativacao": TimestampType,
	"ac_datadesativacao": TimestampType,
	"ac_datafimciclo": TimestampType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}