from pyspark.sql.types import *

bq_table_name = "v_debit_adjustment"
columns_type = {
    "account_id": IntegerType,
    "adjustment_id": IntegerType,
    "amount": DoubleType,
    "external_establishment_description": StringType,
    "create_date": StringType,
    "iscredit": BooleanType,
    "properties": StructType([]),
    "source_date": StringType,
    "status_description": StringType,
    "status_id": IntegerType,
    "type_adjustment_description": StringType,
    "type_adjustment_id": IntegerType,
    "user": StringType,
    "production_date": IntegerType
}