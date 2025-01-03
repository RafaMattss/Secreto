from pyspark.sql.types import *

bq_table_name = "v_internet_banking_pj"

columns_type = {
    "id": StringType,
    "eventcode": StringType,
    "eventdescription": StringType,
    "channel": StringType,
    "environment": StringType,
    "version": StringType,
    "datetime": TimestampType,
    "metadata_person_document_type": StringType,
    "metadata_person_document_value": StringType,
    "metadata_person_email": StringType,
    "metadata_person_tokentype": StringType,
    "metadata_person_tokenid": StringType,
    "metadata_person_username": StringType,
    "metadata_person_usertype": StringType,
    "metadata_person_userrequesterprofile": StringType,
    "metadata_transaction_sourceaccount": StringType,
    "metadata_transaction_sourcebranch": StringType,
    "metadata_transaction_identifier": StringType,
    "metadata_transaction_id": StringType,
    "metadata_transaction_type": StringType,
    "metadata_transaction_targetbank": StringType,
    "metadata_transaction_targetagency": StringType,
    "metadata_transaction_targetaccount": StringType,
    "metadata_transaction_sameownership": BooleanType,
    "metadata_transaction_date": TimestampType,
    "metadata_transaction_value": StringType,
    "metadata_transaction_keytype": StringType,
    "metadata_transaction_keyvalue": StringType,
    "metadata_transaction_paymentform": StringType,
    "metadata_transaction_reason": StringType,
    "metadata_transaction_identifieroriginal": StringType,
    "metadata_persontarget_document_type": StringType,
    "metadata_persontarget_document_value": StringType,
    "metadata_billinformation_id": StringType,
    "metadata_billinformation_linetyped": StringType,
    "metadata_billinformation_barcode": StringType,
    "metadata_billinformation_date": TimestampType,
    "metadata_billinformation_datescheduler": TimestampType,
    "metadata_billinformation_value": StringType,
    "metadata_billinformation_inputtype": StringType,
    "metadata_loaninformation_qtdprestacoes": StringType,
    "metadata_loaninformation_datasolicitacao": TimestampType,
    "metadata_loaninformation_dataprimeiraparcela": TimestampType,
    "metadata_loaninformation_datafinalparcela": TimestampType,
    "metadata_loaninformation_valueemprestimo": StringType,
    "metadata_auditoria_auditoriajson": StringType,
    "metadata_pagamento_pagamentojson": StringType,
    "metadata_cobranca_cobrancajson": StringType,
    "metadata_trace_tracejson": StringType,
    "metadata_emprestimo_emprestimojson": StringType,
    "metadata_obs_obsjson": StringType,
    "production_date": IntegerType
}
