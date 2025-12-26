FROM astrocrpublic.azurecr.io/runtime:3.1-9

USER root

RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev \
    && apt-get clean

USER astro