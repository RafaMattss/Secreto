from pyspark.sql.types import *

bq_table_name = "refinanciamento"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"rf_id_refinanciamento": IntegerType,
	"rf_id_conta": IntegerType,
	"rf_id_eventocompra": IntegerType,
	"rf_datarefinanciamento": TimestampType,
	"rf_rotativopagajuros": DoubleType,
	"rf_debitosfaturadosprox": DoubleType,
	"rf_totalposprox": DoubleType,
	"rf_totalrefinanciado": DoubleType,
	"rf_numeroparcelas": IntegerType,
	"rf_valorparcela": DoubleType,
	"rf_taxajuros": DoubleType,
	"rf_valoriof": DoubleType,
	"rf_cet": DoubleType,
	"rf_responsavel": StringType,
	"rf_status": IntegerType,
	"rf_valorantecipacaopendente": DoubleType,
	"rf_valorparcelasfuturas": DoubleType,
	"rf_valorabatimentojuros": DoubleType,
	"rf_flagsaldototal": BooleanType,
	"rf_totalarefinanciar": DoubleType,
	"rf_statuscashback": IntegerType,
	"rf_percentualcashback": DoubleType,
	"rf_valorcashback": DoubleType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType
}
