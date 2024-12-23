from pyspark.sql.types import *

bq_table_name = "v_debit_card"
columns_type = {
    "account_id": IntegerType,
    "bin": IntegerType,
    "brand": StringType,
    "card_hash": StringType,
    "card_id": IntegerType,
    "embossing_date": StringType,
    "expiration_date": StringType,
    "incorrect_password_attempts": IntegerType,
    "is_temporary_card": BooleanType,
    "issue_date": StringType,
    "name_on_card": StringType,
    "owner": StringType,
    "pan": StringType,
    "person_id": IntegerType,
    "properties": StructType([]),
    "stage_description": StringType,
    "stage_id": IntegerType,
    "status_allow_approve": BooleanType,
    "status_description": StringType,
    "status_id": IntegerType,
    "status_upd_date": StringType,
    "production_date": IntegerType
}

