from pyspark.sql.types import *

bq_table_name = "log_evento"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"le_id_logevento": IntegerType,
	"le_campo": StringType,
	"le_valoratual": StringType,
	"le_valoranterior": StringType,
	"le_id_tabela": IntegerType,
	"ts_nometabela": StringType,
	"le_processo": StringType,
	"le_datamodificacao": TimestampType,
	"le_modificadopor": StringType,
	"le_chave": StringType,
	"le_id_sessao": IntegerType,
	"le_id_atendimento": IntegerType,
	"le_codigotabela": IntegerType,
	"le_chaveorigem": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": StringType,
	"production_date": DateType,
}