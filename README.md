# PyUmbral Docker

Interactive Docker shell to play around with pyUmbral implementation [https://github.com/nucypher/pyUmbral](https://github.com/nucypher/pyUmbral) due to dependency issues on mac and python installation.

# Install

Run the following command to build the docker container. It will per default download and install all the dependencies:

```
docker build -t py-umbral-docker .
```

# Run

1. To run an interactive shell:

```
docker run -it py-umbral-docker /bin/bash
```

2. Then activate the pipenv:

```
cd /contents/pyUmbral && pipenv shell
```

3. And work with your files (`/contents/files/test.py` in this example):

```
cd /contents/files && python test.py
```

# Development Environment

To edit files in `./contents/files` locally and work with them in running docker container start the docker container with a volume:

```
docker run -v $(pwd)/contents:/contents -it py-umbral-docker /bin/bash
```

Then proceed with step `2.` in `Run` above.


# Whats PyUmbral?

PyUmbral is the Python Implementation of the Umbral Proxy Re-Encryption Scheme. The Umbral PRE Scheme was developed by David Núñez and enables splitting of re-encryption keys used for proxy re-encryption. See the whitepaper here: [https://github.com/nucypher/umbral-doc/blob/master/umbral-doc.pdf](https://github.com/nucypher/umbral-doc/blob/master/umbral-doc.pdf).
