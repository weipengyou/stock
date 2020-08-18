#https://cloud.google.com/ai-platform/prediction/docs/exporting-for-prediction#joblib

MODEL_NAME='stock_predictor'
VERSION_NAME='v12'
BUCKET_NAME="model_bucket_ycng_228"
REGION=us-central1

gcloud ai-platform models create $MODEL_NAME \
  --regions $REGION

gcloud components install beta

gcloud beta ai-platform versions create $VERSION_NAME \
  --model $MODEL_NAME \
  --runtime-version 1.13 \
  --python-version 3.5 \
  --origin gs://$BUCKET_NAME/ \
  --package-uris gs://${BUCKET_NAME}/YCNG_228_code-0.1.tar.gz \
  --prediction-class predictor.MyPredictor
