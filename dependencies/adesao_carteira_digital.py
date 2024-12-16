from pyspark.sql.types import *

bq_table_name = "adesao_carteira_digital"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"acd_id_adesaocarteiradigital": IntegerType,
	"acd_id_pessoa": IntegerType,
	"acd_dt_cadastro": TimestampType,
	"acd_dt_fim": TimestampType,
	"acd_nm_usuario_adesao": StringType,
	"acd_nm_usuario_cancelamento": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}