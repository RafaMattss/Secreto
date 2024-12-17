from pyspark.sql.types import *

bq_table_name = "seguro_endereco"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"id_endereco": IntegerType,
	"nm_logradouro": StringType,
	"no_logradouro": StringType,
	"dc_complemento": StringType,
	"nm_bairro": StringType,
	"nm_municipio": StringType,
	"cd_uf": StringType,
	"no_cep": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
