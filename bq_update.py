def bigqueryupload():
    from config import table_name, uri
    from google.cloud import bigquery

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
            bigquery.SchemaField("PercentChange", "FLOAT"),
            bigquery.SchemaField("PE_Ratio", "FLOAT")
        ],
    )

    # Make an API request.
    uri = uri
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )

    # Waits for the job to complete.
    load_job.result()  

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))