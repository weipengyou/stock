BUCKET_NAME="model_bucket_ycng_228"
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
REGION=us-central1
gsutil mb -l $REGION gs://$BUCKET_NAME
