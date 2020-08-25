#for local testing, you can build and run your docker image locally
docker build . -f Dockerfile -t my_image
#to log into the docker image:
docker run -it my_image /bin/bash
