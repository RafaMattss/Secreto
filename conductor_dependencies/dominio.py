from pyspark.sql.types import *

bq_table_name = "dominio"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"cc_id_campo": IntegerType,
	"cc_nome": StringType,
	"cc_descricao": StringType,
	"ccd_id_campo": IntegerType,
	"ccd_ocorrencia": IntegerType,
	"ccd_codigo": StringType,
	"ccd_descricao": StringType,
	"dt_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType
}
