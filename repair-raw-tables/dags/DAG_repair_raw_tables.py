from airflow import DAG
from datetime import timedelta, datetime
from airflow.models import Variable
import os
import sys
from airflow.utils.task_group import TaskGroup
from airflow.providers.ssh.operators.ssh import SSHOperator

bucket_path = Variable.get("BUCKET_INTERMEDIARY")
project_path = f"{bucket_path}/repair-raw-tables"

conn = "jdbc:hive2://di-pnb-dev-spark3-master0.di-pnb-h.tyoz-sbgs.cloudera.site:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2;retries=5;sslTrustStore=/var/lib/cloudera-scm-agent/agent-cert/cm-auto-global_truststore.jks;trustStorePassword=TrbBpNN3cX11C61ZS3Z94C3dG1"
process_beeline2 = "beeline -u '" + conn + "' -f "

start_date = datetime(2024, 12, 27)

default_args = {
    "depends_on_past": False,
    "retry_delay": timedelta(minutes=5),
    "retries": 3,
    "email_on_retry": False,
    "email_on_failure": False,
    "on_failure_callback": print,
}


with DAG(
    "repair_raw_tables",
    start_date=start_date,
    description="Este projeto atualiza os dados das tabelas raw após a ingestão feita pelo BigQuery.",
    schedule="0 23 * * *",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    max_active_tasks=6,
    tags=[
        "FINOPS",
        "RAW",
        "DESENVOLVIMENTO",
        "PYSPARK",
        "DIARIO",
        "BIGQUERY",
        "DATAENG",
    ]
) as repair_raw_tables:
    
    t_sync = SSHOperator(
        task_id="t_sync",
        ssh_conn_id="test-ssh",
        command=(
            "gsutil rsync -d -r gs://airflow_bucket_bi/repair-raw-tables/ "
            "/tmp/repair-raw-tables"
        ),
    )

    with TaskGroup("repair_raw_tables") as repair_conductor:
        repair_conductor = SSHOperator(
            task_id="repair_conductor",
            ssh_conn_id="test-ssh",
            command="sh "
            + process_beeline2
            + 'src/raw_conductor.sql && echo "repair_conductor ok"',
        )

        repair_dock = SSHOperator(
            task_id="repair_dock",
            ssh_conn_id="test-ssh",
            command="sh "
            + process_beeline2
            + 'src/raw_dock.sql && echo "repair_dock ok"',
        )

        repair_neurotech = SSHOperator(
            task_id="repair_neurotech",
            ssh_conn_id="test-ssh",
            command="sh "
            + process_beeline2
            + 'src/raw_neurotech.sql && echo "repair_neurotech ok"',
        )

        repair_grc = SSHOperator(
            task_id="repair_grc",
            ssh_conn_id="test-ssh",
            command="sh "
            + process_beeline2
            + 'src/risco_gestao_risco_consolidado.sql && echo "risco_gestao_risco_consolidado ok"',
        )

    repair_conductor
    repair_dock
    repair_neurotech
