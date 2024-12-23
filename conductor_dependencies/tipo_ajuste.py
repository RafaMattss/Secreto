from pyspark.sql.types import *

bq_table_name = "tipo_ajuste"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"ta_id_ajuste": IntegerType,
	"ta_descricao": StringType,
	"ta_flagcredito": BooleanType,
	"ta_flagtransacaodisputa": BooleanType,
	"ta_flagpagamentolojista": BooleanType,
	"ta_toleranciavalorminimoextrato": DoubleType,
	"ta_flagsistema": IntegerType,
	"ta_tipoeventoexternooriginal": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
