from pyspark.sql.types import *

bq_table_name = "proposta_detalhe"
columns_type = {
    "hash_key": StringType,
    "source": StringType,
    "codigooperacao": StringType,
    "entradas": MapType(StringType(), StringType()),
    "calculadas": MapType(StringType(), StringType()),
    "outros": MapType(StringType(), StringType()),
    "retornos": MapType(StringType(), StringType()),
    "variaveis": MapType(StringType(), StringType()),
    "fluxo_regras": MapType(StringType(), StringType()),
    "banco": MapType(StringType(), StringType()),
    "instante_data": TimestampType,
    "production_date": IntegerType
}
