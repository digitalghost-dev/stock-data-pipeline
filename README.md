# Stock Data Pipeline with Python and Google Cloud

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://storage.googleapis.com/website-storage-bucket/icons/danger.svg">
>   <img alt="Tip" src="https://storage.googleapis.com/website-storage-bucket/icons/danger.svg">
> </picture><br>
> This project is now archived. The visualization still works but has stopped being updated as of March 30th, 2022. Archival was set due to no longer wanting to pay for API usage.


> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://storage.googleapis.com/website-storage-bucket/icons/warning.svg">
>   <img alt="Tip" src="https://storage.googleapis.com/website-storage-bucket/icons/warning.svg">
> </picture><br>
> Any data in this project or on my website is for informational purposes only and should not be taken as invesment advice.

<br>

<div>
    <img alt="Version" src="https://img.shields.io/badge/Project Number-1-orange.svg?cacheSeconds=2592000" />
</div>

## Overview
* Extracts and transforms S&P 500 stock data with Python from a financial API.
* Data is loaded into Cloud Storage then transferred to BigQuery and rendered on my webpage.
* Python code runs on a scheduled cron job through a virtual machine with GCP Compute Engine.

### Important Links
* [Visualization](https://www.digitalghost.dev/stock-data-pipeline)
* [Documentation](https://github.com/digitalghost-dev/stock-data-pipeline/wiki/Stock-Data-Pipeline-Documentation)

## How the Pipeline Works

### Data Pipeline
1. A cron job triggers `main.py` to run.
2. `main.py` calls the IEX Cloud API.
3. The data is processed and cleaned by removing commas, hyphens, and/or other extra characters from the **company name** column.
4. `main.py` creates a `csv` file with the prepared data.
5. `load.py` copies the `csv` file to a Cloud Storage bucket.
6. The `csv` file is loaded to BigQuery.
7. Using the [BigQuery API](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries) and when the [webpage](https://www.digitalghost.dev/projects/stock-data-pipeline) is loaded, the data is queried and then displayed.

### CI/CD
* None

### Notes:
* The file that connects to BigQuery to pull the data when the page loads is located in my [wesbite repository](https://github.com/digitalghost-dev/website/) since that renders the frontend.
* The pipeline does not account for holidays.

### Pipeline Flowchart
![stock-data-flowchart](https://storage.googleapis.com/pipeline-flowcharts/stock-data-pipeline-flowchart.png)

## Services Used
* **APIs:** [IEX Cloud](https://www.iexcloud.io)
* **Google Cloud Services:**
    * **Virtual Machine:** [Compute Engine ](https://cloud.google.com/compute)
    * **Object Storage:** [Cloud Storage](https://cloud.google.com/storage)
    * **Data Warehouse:** [BigQuery](https://cloud.google.com/bigquery/)
* **Scheduler:** [cron](https://en.wikipedia.org/wiki/Cron)
* **Visualization:** [Flask](https://flask.palletsprojects.com/en/2.2.x/) and HTML
