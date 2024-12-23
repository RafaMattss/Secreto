from pyspark.sql.types import *

bq_table_name = "seguro_count"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"tabela": StringType,
	"linhasenviadas": IntegerType,
	"dataexecucao": TimestampType,
	"production_date": DateType,
}