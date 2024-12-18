from pyspark.sql.types import *

bq_table_name = "remuneracao_ativacao_conta"
columns_type = {
    "hash_key": StringType,
    "source": StringType,
    "id": IntegerType,
    "dataativacao": TimestampType,
    "id_conta": IntegerType,
    "id_estabelecimento": IntegerType,
    "matricula": StringType,
    "funcaoativa": StringType,
    "dh_relatorio": TimestampType,
    "operation": StringType,
    "operation_sequence": IntegerType,
    "production_date": DateType
}

