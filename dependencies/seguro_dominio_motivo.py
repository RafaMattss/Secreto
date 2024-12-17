from pyspark.sql.types import *

bq_table_name = "seguro_dominio_motivo"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"mtc_id_motivocancelamento": IntegerType,
	"mtc_id_emissor": IntegerType,
	"mtc_tp_cancelamento": IntegerType,
	"mtc_nm_motivocancelamento": StringType,
	"mtc_fl_ativo": BooleanType,
	"mtc_fl_visibilidadelojista": BooleanType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
