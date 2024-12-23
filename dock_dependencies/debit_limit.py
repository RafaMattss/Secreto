from pyspark.sql.types import *

bq_table_name = "v_debit_limit"
columns_type = {
    "account_id": DoubleType,
    "available_balance": DoubleType,
    "available_point": DoubleType,
    "credit_limit": DoubleType,
    "installment_available_balance": DoubleType,
    "installment_limit": DoubleType,
    "international_available_balance": DoubleType,
    "international_purchase_limit": DoubleType,
    "international_withdrawal_available": DoubleType,
    "international_withdrawal_limit": DoubleType,
    "maximum_limit": DoubleType,
    "properties": StructType([]),
    "tranche_available_balance": DoubleType,
    "tranche_limit": DoubleType,
    "withdrawal_available_balance": DoubleType,
    "withdrawal_limit": DoubleType,
    "production_date": IntegerType
}

