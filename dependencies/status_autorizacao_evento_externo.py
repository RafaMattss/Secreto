from pyspark.sql.types import *

bq_table_name = "status_autorizacao_evento_externo"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"sae_id_statusautorizacoeseventosexternos": IntegerType,
	"sae_status": IntegerType,
	"sae_descricao": StringType,
	"sae_flagpagamentovalidocorrespondente": IntegerType,
	"sae_flagpermitealteracaostatuscorrespondente": IntegerType,
	"sae_flagpermitecancelamentocorrespondente": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}
