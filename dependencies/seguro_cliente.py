from pyspark.sql.types import *

bq_table_name = "seguro_cliente"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"cli_id_cliente": IntegerType,
	"cli_id_emissor": IntegerType,
	"cli_tp_cliente": IntegerType,
	"cli_no_conta": StringType,
	"cli_tp_cartao": IntegerType,
	"cli_no_diavencimento": IntegerType,
	"cli_tp_titularidade": IntegerType,
	"cli_id_pessoa": IntegerType,
	"pes_id_pessoa": IntegerType,
	"pes_nm_pessoa": StringType,
	"pes_no_cpf": StringType,
	"pes_dt_nascimento": TimestampType,
	"pes_tp_sexo": IntegerType,
	"pes_nm_mae": StringType,
	"pes_no_rg": StringType,
	"pes_dt_emissaorg": TimestampType,
	"pes_cd_uf_rg": StringType,
	"pes_no_pis": StringType,
	"pes_no_cns": StringType,
	"pes_no_declaracaonascidovivo": StringType,
	"pes_tp_estadocivil": IntegerType,
	"pes_tp_grauparentesco": IntegerType,
	"pes_id_endereco": IntegerType,
	"pes_id_contato": IntegerType,
	"pes_tp_pessoa": StringType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
    "cli_fl_contacredito": BooleanType
}