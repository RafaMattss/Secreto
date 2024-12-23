from pyspark.sql.types import *

bq_table_name = "v_credit_person"
columns_type = {
    "bank_account": StringType,
    "bank_agency": StringType,
    "bank_code": IntegerType,
    "birth_date": StringType,
    "birth_place": StringType,
    "document_id": StringType,
    "document_issuer": StringType,
    "email": StringType,
    "father": StringType,
    "gender": StringType,
    "graduation_degree": StringType,
    "mother": StringType,
    "name": StringType,
    "nationality": StringType,
    "occupation": StringType,
    "person_id": IntegerType,
    "person_type": StringType,
    "politically_exposed": BooleanType,
    "properties": StructType([]),
    "salary": DoubleType,
    "spouse_name": StringType,
    "spouse_salary": DoubleType,
    "tax_identification_number": StringType,
    "production_date": IntegerType
}