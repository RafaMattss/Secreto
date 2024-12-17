from pyspark.sql.types import *

bq_table_name = "status_cartao"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"sct_id_statuscartao": IntegerType,
	"sct_status": IntegerType,
	"sct_descricao": StringType,
	"sct_respautorizador": StringType,
	"sct_flagreemitecartao": BooleanType,
	"sct_flagcobratarifa": BooleanType,
	"sct_flagemiteprovisorio": BooleanType,
	"sct_flagalteranome": BooleanType,
	"sct_flagcancelaconta": BooleanType,
	"sct_statusdestinoconta": IntegerType,
	"sct_flagalterastatus": BooleanType,
	"sct_flagcancelamento": BooleanType,
	"sct_respautorizadoratm": StringType,
	"sct_flagcadastrosenha": IntegerType,
	"sct_flagcadastranovasenha": IntegerType,
	"sct_flagofereceseguroatdo": StringType,
	"sct_statusdestinodesbloqueio": IntegerType,
	"sct_flagreemitemigracao": BooleanType,
	"sct_statusdestinomigracao": IntegerType,
	"sct_statusreemissaomigracao": IntegerType,
	"sct_flagpermitedesbloqueio": BooleanType,
	"sct_flagcancelardesbloqueio": BooleanType,
	"sct_respautorizadorvisa": StringType,
	"sct_flagbloqueiosenhaincorreta": BooleanType,
	"sct_respautorizadormastercard": StringType,
	"sct_flagreversivel": BooleanType,
	"sct_flagstatusfraude": BooleanType,
	"sct_flagavisaemissor": BooleanType,
	"sct_flagprepago": BooleanType,
	"sct_flagenviaexceptionfile": BooleanType,
	"sct_id_motivoembossing": IntegerType,
	"sct_flagfaztransferencia": BooleanType,
	"sct_flagrecebetransferencia": BooleanType,
	"sct_flagexibevalorreemissao": BooleanType,
	"sct_flagreemiteautcartao": BooleanType,
	"sct_respautorizadormasterrepower": StringType,
	"sct_flagpermitebloqueio": IntegerType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}