from pyspark.sql.types import *

bq_table_name = "estado_conta"
columns_type = {
	"hash_key": StringType,
	"source": StringType,
	"ec_id_conta": IntegerType,
	"ec_id_emissor": IntegerType,
	"ec_id_produto": IntegerType,
	"ec_proximovencimentoreal": TimestampType,
	"ec_proximovencimentopadrao": StringType,
	"ec_inicioperiodofaturado": TimestampType,
	"ec_terminoperiodofaturado": TimestampType,
	"ec_saldoextratoanterior": DoubleType,
	"ec_basemultacobrada": DoubleType,
	"ec_valorminimoextrato": DoubleType,
	"ec_numerociclo": IntegerType,
	"ec_financiavelextrato": DoubleType,
	"ec_naofinanciavelextrato": DoubleType,
	"ec_dataprevistafinanciamento": TimestampType,
	"ec_vencimentorealanterior": TimestampType,
	"ec_vencimentopadraoanterior": StringType,
	"ec_dataregularizacaofinanciamento": TimestampType,
	"ec_multaextrato": DoubleType,
	"ec_internacionaisdolarextrato": DoubleType,
	"ec_internacionaisreaisextrato": DoubleType,
	"ec_debitosinternacionais": DoubleType,
	"ec_comprasinternacionaisdolar": DoubleType,
	"ec_saquesinternacionaisdolar": DoubleType,
	"ec_diversosinternacionaisdolar": DoubleType,
	"ec_despesasinternacionaisdolar": DoubleType,
	"ec_despesasinternacionaisreais": DoubleType,
	"ec_parcelasfinanciaveis": DoubleType,
	"ec_comprasnacionais": DoubleType,
	"ec_saquesnacionais": DoubleType,
	"ec_tarifasnacionais": DoubleType,
	"ec_debitosdiversosnacionais": DoubleType,
	"ec_multa": DoubleType,
	"ec_encargosfinanciamento": DoubleType,
	"ec_encargosatraso": DoubleType,
	"ec_acertospositivosdiversos": DoubleType,
	"ec_creditosnacionais": DoubleType,
	"ec_debitosnacionais": DoubleType,
	"ec_pagamentos": DoubleType,
	"ec_creditopagamentominimo": DoubleType,
	"ec_correcaocreditominimo": DoubleType,
	"ec_acertosnegativosdiversos": DoubleType,
	"ec_saldoanteriorfinal": DoubleType,
	"ec_financiavelanteriorfinal": DoubleType,
	"ec_datafinanciavelfinal": TimestampType,
	"ec_financiadoanteriorfinal": DoubleType,
	"ec_datafinanciadofinal": TimestampType,
	"ec_naofinanciavelanteriorfinal": DoubleType,
	"ec_datanaofinanciavelfinal": TimestampType,
	"ec_saldoatualfinal": DoubleType,
	"ec_financiavelatualfinal": DoubleType,
	"ec_naofinanciavelatualfinal": DoubleType,
	"ec_flagmulta": BooleanType,
	"ec_flagrefinanciamento": BooleanType,
	"ec_flaganuidade": BooleanType,
	"ec_flagemiteextrato": BooleanType,
	"ec_flagcobrafinanciamento": IntegerType,
	"ec_flagcobramulta": IntegerType,
	"ec_saldoextratoanteriorajustado": DoubleType,
	"ec_statusconta": IntegerType,
	"ec_flagalteracaovencimento": IntegerType,
	"ec_valorminimoextratooriginal": DoubleType,
	"ec_parcelasnaofinanciaveis": DoubleType,
	"ec_valorminimoextratoanterior": DoubleType,
	"ec_valorjamultado": DoubleType,
	"ec_comprajuros": DoubleType,
	"ec_pontosconcedidos": DoubleType,
	"ec_pontosremanescentes": DoubleType,
	"ec_vencimentobasejurospadrao": StringType,
	"ec_vencimentobasejurosreal": TimestampType,
	"ec_rotativopagajuros": DoubleType,
	"ec_saquepagajuros": DoubleType,
	"ec_comprasjurospagajuros": DoubleType,
	"ec_vencimentoprox": TimestampType,
	"ec_saquefaturadoprox": DoubleType,
	"ec_comprasjurosfaturadoprox": DoubleType,
	"ec_debitosfaturadosprox": DoubleType,
	"ec_totalprox": DoubleType,
	"ec_vencimentoposprox": TimestampType,
	"ec_totalposprox": DoubleType,
	"ec_totalfuturo": DoubleType,
	"ec_flagemfaturamento": IntegerType,
	"ec_proximovalorminimo": DoubleType,
	"ec_statuscontabil": IntegerType,
	"ec_pontuacaototalciclo": DoubleType,
	"ec_pontuacaousadaciclo": DoubleType,
	"ec_jurosmora": DoubleType,
	"ec_saldocongelado": DoubleType,
	"ec_principalparcelado": DoubleType,
	"ec_comprassemjurosnaovencidas": DoubleType,
	"ec_parcelascomjurosnaovencidas": DoubleType,
	"ec_saldofuturojuros": DoubleType,
	"ec_saldofuturoparceladocomjuros": DoubleType,
	"ec_saldofuturoparceladosemjuros": DoubleType,
	"ec_encargosciclo": DoubleType,
	"ec_taxadiariaciclo": DoubleType,
	"ec_id_saldodiario": IntegerType,
	"ec_dataentradacreliq": TimestampType,
	"ec_saldoentradacreliq": DoubleType,
	"ec_saldojurosacordo": DoubleType,
	"ec_databaserendimento": TimestampType,
	"ec_dataultaplicacao": TimestampType,
	"ec_saldoaplicacao": DoubleType,
	"ec_rendimentoacumulado": DoubleType,
	"ec_provisaoirdatabase": DoubleType,
	"ec_flagoverlimit": BooleanType,
	"ec_qtdeisencaotarifa": IntegerType,
	"ec_flagfaturaporemail": BooleanType,
	"ec_flagsmsextratoincondicional": IntegerType,
	"ec_saldocompraprogramada": DoubleType,
	"ec_debitosopcionais": DoubleType,
	"ec_debitosrecorrentes": DoubleType,
	"ec_seguros": DoubleType,
	"ec_nossonumero": StringType,
	"ec_vencpadraoanterior": TimestampType,
	"ec_vencbasejurospadrao": TimestampType,
	"ec_proximovencpadrao": TimestampType,
	"ec_statusbonussabado": IntegerType,
	"ec_flagdiferenciado": BooleanType,
	"sd_datasaldo": TimestampType,
	"dh_relatorio": TimestampType,
	"operation": StringType,
	"operation_sequence": IntegerType,
	"production_date": DateType,
}