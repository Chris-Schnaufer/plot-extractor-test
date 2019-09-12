FROM agdrone/base_extractor_plot:1.0
LABEL maintainer="Chris Schnaufer <schnaufer@email.arizona.edu>"

# Standard extractor setup
COPY extractor_info.json extractor.py configuration.py /home/extractor/
ENV \
    RABBITMQ_QUEUE="terra.dronepipeline.test-canopycover" 

# ADD ADDITIONAL INITIALIZATION STEPS HERE
