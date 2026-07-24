py wordcount.py --runner DataflowRunner --project gcp-data-engineer-04 --region us-central1 --staging_location gs://gcs-bucket-curso-04/staging --temp_location gs://gcs-bucket-curso-04/temp --template_location gs://gcs-bucket-curso-04/templates/wordcount_template

#pip install apache_beam
#pip install apache_beam[gcp]