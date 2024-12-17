from pyspark.sql.types import *

bq_table_name = "compras_contestadas"
from pyspark.sql.types import *

bq_table_name = "compras_contestadas"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"cc_id_compracontestada": LongType,
	"cc_id_eventocompra": LongType,
	"cc_id_conta": LongType,
	"cc_id_operacao": LongType,
	"cc_datacontestacao": TimestampType,
	"cc_parcelapedida": IntegerType,
	"cc_quantidadeparcelas": IntegerType,
	"cc_status": StringType,
	"cc_id_statuscontestacao": IntegerType,
	"scc_statuscontestacao": StringType,
	"cc_historico": StringType,
	"cc_dataalteracao": TimestampType,
	"cc_responsavel": StringType,
	"cc_id_tiporesolucaocontestacao": IntegerType,
	"trc_tiporesolucaocontestacao": StringType,
	"cc_id_arquivo": IntegerType,
	"cc_valorparcial": DoubleType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
	"audit_control_number": StringType,
	"data2reapresentacao": TimestampType,
	"dataenviocb": TimestampType,
	"motivo2reapresentacao": StringType,
	"razaocb": StringType,
	"status": IntegerType,
	"id_safe": IntegerType
}
