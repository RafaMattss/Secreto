from pyspark.sql.types import *

bq_table_name = "v_credit_account"
columns_type = {
    "account_id": IntegerType,
    "create_date": StringType,
    "delivery_address": StringType,
    "due_day": IntegerType,
    "next_due_date": StringType,
    "next_real_due_date": StringType,
    "person_id": IntegerType,
    "product": StructType([]),
    "properties": StructType([]),
    "status_description": StringType,
    "status_id": IntegerType,
    "production_date_origem": IntegerType,
    "dth_inc": TimestampType,
    "production_date": IntegerType,
}
