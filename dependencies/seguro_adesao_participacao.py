from pyspark.sql.types import *

bq_table_name = "seguro_adesao_item"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"asi_id_adesaoseguroitem": IntegerType,
	"asi_id_adesaoseguro": IntegerType,
	"asi_id_pessoa": IntegerType,
	"asi_cd_item": IntegerType,
	"asi_dt_iniciovigencia": TimestampType,
	"asi_dt_terminovigencia": TimestampType,
	"asi_fl_titular": BooleanType,
	"asi_tp_statusintegracao": IntegerType,
	"asi_dt_exclusao": TimestampType,
	"asi_dt_adesao": TimestampType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
