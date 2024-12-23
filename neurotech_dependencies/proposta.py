from pyspark.sql.types import *

bq_table_name = "proposta"
columns_type = {
    "hash_key": StringType,
    "source": StringType,
    "codigooperacao": StringType,
    "codigoproposta": StringType,
    "nomepolitica": StringType,
    "resultado": StringType,
    "instante_data": TimestampType,
    "mensagem": StringType,
    "sucesso": StringType,
    "versaopolitica": StringType,
    "dth_inclusao": TimestampType,
    "tempo_execucao_msec": DoubleType,
    "instanceinicio": TimestampType,
    "instantefim": TimestampType,
    "production_date": IntegerType
}
