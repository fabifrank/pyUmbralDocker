FROM python:3.7.0-stretch

ENV PATH="/root/.local/bin:${PATH}"

COPY ./pyUmbral /pyUmbral
COPY ./contents /contents
RUN pip install --user pipenv
RUN cd /pyUmbral && pipenv install && pipenv install '-e .' --dev


CMD ["/bin/bash"]
