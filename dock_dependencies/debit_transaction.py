from pyspark.sql.types import *

bq_table_name = "v_debit_transaction"
columns_type = {
    "account_id": IntegerType,
    "amount": DoubleType,
    "card_id": IntegerType,
    "current_installments": IntegerType,
    "event_id": IntegerType,
    "iscredit": BooleanType,
    "merchant": StringType,
    "merchant_id": IntegerType,
    "properties": StructType([]),
    "source_date": StringType,
    "total_installments": IntegerType,
    "transaction_date": StringType,
    "transaction_id": IntegerType,
    "transaction_type": StringType,
    "transaction_type_description": StringType,
    "transaction_type_id": IntegerType,
    "production_date": IntegerType
}