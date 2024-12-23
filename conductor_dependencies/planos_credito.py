from pyspark.sql.types import *

bq_table_name = "planos_credito_cdc"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"pc_flagcalculaiofrotativo": BooleanType,
	"pc_flagcalculamora": BooleanType,
	"pc_flagcalculamulta": BooleanType,
	"pc_id_ajuste": StringType,
	"pc_id_operacao": LongType,
	"pc_id_planocredito": LongType,
	"pc_id_produtoentidade": StringType,
	"pc_id_taxajurosapropriacao": LongType,
	"pc_id_tipodebitorecorrente": StringType,
	"pc_ordem": LongType,
	"pc_percentualminimo": DoubleType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}

