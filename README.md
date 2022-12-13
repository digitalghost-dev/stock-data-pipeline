# Stock Data Pipeline with Python and Google Cloud

<div>
    <img alt="Version" src="https://img.shields.io/badge/Current Version-1.1-blue.svg?cacheSeconds=2592000" />
    <img alt="Version" src="https://img.shields.io/badge/Project Number-1-orange.svg?cacheSeconds=2592000" />
</div>

## Description
> This is my first project and attempt at creating a data pipeline. It's a simple example, but it helps to understand how data can flow from one place to another. In this case, an API through cloud services then to my website.

> It being a simple data pipeline, no fancy data engineering tools are used. Only Python and a few Google Cloud services.

This pipeline provides basic information from all the companies in the [S&P500](https://markets.businessinsider.com/index/components/s&p_500?op=1). The statistics shown for each company is:
* Ticker Symbol
* Company Name
* Current Price
* Percent Change
* P/E Ratio

[View the frontend](https://www.digitalghost.dev/projects/stock-data-pipeline) of the data.

## How the Pipeline Works

This data pipeline follows an ETL process and can be broken down in the following steps:

1. Within a Compute Engine virtual machine, `main.py` runs and does the following:
    1. Calls the IEX Cloud API.
    2. The data is cleaned by removing commas, hyphens, and/or other extra characters from the **company name** column.
    3. Creates a `csv` file with the cleaned data.
    4. Copies the `csv` file to a Cloud Storage bucket.
    5. Uploads the `csv` file to BigQuery. 
        * *Note:* `bq_update.py` holds the code for uploading to BigQuery but is called from within `main.py` to keep files more organized.
    6. A CRON job in the virtual machine runs `main.py` every 15 minutes, 9:00 - 16:00 EST, Monday through Friday with updated data.
2. Using the [BigQuery API](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries) and when the [webpage](https://www.digitalghost.dev/projects/data-pipeline) is loaded, the data is queried and then displayed.
    * *Note:* The file that connects to BigQuery to pull the data when the page loads is located in my [wesbite repository](https://github.com/digitalghost-dev/website/) since that renders the frontend.

### Pipeline Flowchart
![stock-data-flowchart](https://storage.googleapis.com/personal-website-nv-bucket/stock-data-flowchart.png)

## Services used

* **API:** [IEX Cloud](https://www.iexcloud.io)
* **Google Cloud services**
    * **Virtual Machine:** [Compute Engine ](https://cloud.google.com/compute)
    * **Object Storage:** [Cloud Storage](https://cloud.google.com/storage)
    * **Data Warehouse:** [BigQuery](https://cloud.google.com/bigquery/)

## Changlog

### Version 1.0

* Set up the initial files and infastructure.
* The four metrics shown are the **ticker symbol**, **company name**, **current price**, and **percent change**.

#### Version 1.1

* Adding the P/E Ratio as a new metric.