from pyspark.sql.types import *

bq_table_name = "telefone"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"t_id_telefone": IntegerType,
	"t_id_tipotelefone": IntegerType,
	"tt_tipotelefone": StringType,
	"t_id_pessoafisica": IntegerType,
	"t_id_estabelecimento": IntegerType,
	"t_ddd": StringType,
	"t_telefone": StringType,
	"t_ramal": StringType,
	"t_proprietario": StringType,
	"t_situacao": IntegerType,
	"t_situacaotelefone": IntegerType,
	"t_statusativo": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
