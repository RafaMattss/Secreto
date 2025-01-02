from pyspark.sql.types import *

bq_table_name = "grc_visao_consolidada_hist"
columns_type = {
    "num_cpf_cliente": StringType(),
    "cod_sistema_origem": LongType(),
    "des_sistema_origem": StringType(),
    "id_cliente_so": LongType(),
    "nom_cliente": StringType(),
    "dth_nascimento": TimestampType(),
    "cod_tipo_pessoa": StringType(),
    "dth_ini_relacionamento": TimestampType(),
    "dth_ult_atu_cli_so": TimestampType(),
    "qtd_dias_ult_atu_cli_so": LongType(),
    "cod_modelo_behaviour_score": LongType(),
    "dth_calculo_score": TimestampType(),
    "num_pontuacao_score": FloatType(),
    "cod_rating_credito": LongType(),
    "flg_creliq": StringType(),
    "dth_prim_creliq": TimestampType(),
    "dth_ult_creliq": TimestampType(),
    "flg_carteira_cedida": StringType(),
    "qtd_conta_ativa": LongType(),
    "qtd_emprestimo_ativo": LongType(),
    "qtd_atraso": LongType(),
    "dth_ult_atraso": TimestampType(),
    "qtd_acordo_ativo": LongType(),
    "qtd_acordo_nao_ativo": LongType(),
    "val_total_liberado_prod_parcelado": FloatType(),
    "val_total_financiado_prod_parcelado": FloatType(),
    "qtd_parcelas_prod_parcelado": LongType(),
    "val_saldo_devedor_prod_parcelado": FloatType(),
    "qtde_parcela_em_atraso_prod_parcelado": LongType(),
    "val_saldo_atraso_prod_parcelado": FloatType(),
    "qtd_parcela_a_vencer_prod_parcelado": LongType(),
    "val_saldo_a_vencer_prod_parcelado": FloatType(),
    "qtde_parcela_paga_prod_parcelado": LongType(),
    "val_saldo_pago_prod_parcelado": FloatType(),
    "val_rotativo_limite_maximo": FloatType(),
    "val_rotativo_lim_concedido": FloatType(),
    "val_rotativo_lim_utilizado": FloatType(),
    "val_rotativo_limite_disponivel": FloatType(),
    "val_parcela_facil_limite_concedido": FloatType(),
    "val_parcela_facil_limite_disponivel": FloatType(),
    "lst_contrato_conta_cartao": ArrayType(
        StructType([])
    ),
    "lst_fatura": ArrayType(
        StructType([])
    ),
    "lst_cartao_associado_conta_cliente": ArrayType(
        StructType([])
    ),
    "lst_contrato_emprestimo": ArrayType(
        StructType([])
    ),
    "lst_contrato_cobranca_saas": ArrayType(
        StructType([])
    ),
    "lst_acordo_cobranca_saas": ArrayType(
        StructType([])
    ),
    "dat_geracao_visao": DateType(),
    "dth_inclusao_reg": TimestampType()
}
