from pyspark.sql.types import *

bq_table_name = "controle_vencimento"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"cv_id_controlevencimentos": IntegerType,
	"cv_datavencimento": TimestampType,
	"cv_dataprevistacorte": TimestampType,
	"cv_datarealizacaocorte": TimestampType,
	"cv_dataprevistafaturamento": TimestampType,
	"cv_datarealizacaofaturamento": TimestampType,
	"cv_dataprevistavencimento": TimestampType,
	"cv_datarealizacaovencimento": TimestampType,
	"cv_usuario": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
