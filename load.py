from config import table_name, cloud_storage_bucket
from google.cloud import bigquery
import subprocess

def csv_file():

    # Running a shell command to upload to Cloud Storage.
    subprocess.run(["gsutil cp *.csv " + cloud_storage_bucket], shell=True)

def bigquery_upload():

    # Construct a BigQuery client object.
    client = bigquery.Client()
    table_id = table_name

    # Creating table schema
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        schema=[
            bigquery.SchemaField("Ticker", "STRING"),
            bigquery.SchemaField("Company", "STRING"),
            bigquery.SchemaField("Price", "FLOAT"),
            bigquery.SchemaField("Change", "FLOAT"),
            bigquery.SchemaField("PE_Ratio", "FLOAT")
        ],
    )

    # Make an API request.
    load_job = client.load_table_from_uri(
        cloud_storage_bucket, table_id, job_config=job_config
    )

    # Waits for the job to complete.
    load_job.result()  

    destination_table = client.get_table(table_id)
    print(f"Loaded {destination_table.num_rows} rows.")