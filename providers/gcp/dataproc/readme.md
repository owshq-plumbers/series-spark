# Google DataProc - Apache Spark

[running jobs in production for dataproc](https://cloud.google.com/blog/products/data-analytics/7-best-practices-for-running-cloud-dataproc-in-production)  
[tips for running long-running clusters](https://cloud.google.com/blog/products/data-analytics/10-tips-for-building-long-running-clusters-using-cloud-dataproc)  

> * deployment option = gcloud, deployment manager & terraform
> * cluster creation = compute engine [ce]
> * name = owshq-spark-dev-01
> * region = us-east1
> * zone = us-east1-c
> * cluster type = standard [1 master & multiple workers]
> * versioning = 2.1 [Debian 11, Hadoop 3.3, Spark 3.3]
> * component gateway = enable
> * machine family = general-purpose
> * series = n2
> * type = n2-standard-2 [2 vcpus & 8 gb] x [2]
> * access = allow api access of all gcp services
> * cloud storage location = us-east1
> * storage name = owshq-landing-zone
> * time to provision = [90 secs]

### interact with gcs using google [cloud shell]
```sh 
gsutil ls gs://owshq-landing-zone/files
gsutil ls gs://owshq-landing-zone/files/users
gsutil ls gs://owshq-landing-zone/files/business
gsutil ls gs://owshq-landing-zone/files/reviews

gsutil ls gs://owshq-landing-zone/app
```

### submit a job on dataproc [apache spark]
```sh
dataproc-batch-etl-yelp-py-01
gs://owshq-landing-zone/app/cluster.py

gcloud dataproc jobs wait dataproc-batch-etl-yelp-py --project silver-charmer-243611 --region us-east1

6 min 16 sec
```

### submit a job on dataproc [serverless]
```sh
serverless-batch-etl-yelp-py-01
gs://owshq-landing-zone/app/cluster.py

gcloud dataproc batches submit --project silver-charmer-243611 \
  --region us-central1 pyspark \
  --batch serverless-batch-etl-yelp-py-01 gs://owshq-landing-zone/app/cluster.py \
  --version 2.1 \
  --subnet default
  
4 min 18 sec
```
