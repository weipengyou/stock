BUCKET_NAME="model_bucket_ycng_228"
export PYTHONPATH='.'
python src/create_model.py
gsutil cp AAL.pkl gs://${BUCKET_NAME}/AAL.pkl
cd src
python setup.py sdist --formats=gztar
gsutil cp dist/YCNG_228_code-0.1.tar.gz gs://${BUCKET_NAME}/YCNG_228_code-0.1.tar.gz
