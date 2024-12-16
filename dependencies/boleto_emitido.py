from pyspark.sql.types import *

bq_table_name = "boleto_emitido"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"be_id_boleto": IntegerType,
	"be_id_tipoboleto": IntegerType,
	"tb_descricaotipoboleto": StringType,
	"be_id_conta": IntegerType,
	"be_dataemissao": TimestampType,
	"be_statusboleto": StringType,
	"be_situacaoboleto": StringType,
	"be_valorboleto": DoubleType,
	"be_datavencimento": TimestampType,
	"be_nossonumero": DoubleType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}