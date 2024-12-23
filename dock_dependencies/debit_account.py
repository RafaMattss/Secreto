from pyspark.sql.types import *

bq_table_name = "v_debit_account"
columns_type = {
    "next_due_date": StringType,
    "delivery_address": StringType,
    "product": StructType([]),
    "status_description": StringType,
    "account_id": IntegerType,
    "due_day": IntegerType,
    "status_id": IntegerType,
    "next_real_due_date": StringType,
    "create_date": StringType,
    "properties": StructType([]),
    "person_id": IntegerType,
    "production_date_origem": IntegerType,
    "dth_inc": TimestampType,
    "production_date": IntegerType,
}
