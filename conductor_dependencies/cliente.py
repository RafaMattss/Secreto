from pyspark.sql.types import *

bq_table_name = "cliente"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"pf_id_pessoafisica": IntegerType,
	"pf_id_emissor": IntegerType,
	"pf_nome": StringType,
	"pf_cpf": StringType,
	"pf_datanascimento": StringType,
	"pf_sexo": StringType,
	"pf_numeroidentidade": StringType,
	"pf_orgaoidentidade": StringType,
	"pf_estadoidentidade": StringType,
	"pf_dataemissaoidentidade": StringType,
	"pf_cic": StringType,
	"pf_statuscic": IntegerType,
	"pf_flagalteracaocic": IntegerType,
	"pf_flagdeficientevisual": BooleanType,
	"pf_tipopessoa": IntegerType,
	"pf_statuspf": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType
}