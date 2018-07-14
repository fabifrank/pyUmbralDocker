FROM python:3.7.0-stretch

ENV PATH="/root/.local/bin:${PATH}"

COPY ./contents /contents
COPY ./pyUmbral/ /contents/ 
RUN pip install --user pipenv
RUN cd /contents && pipenv install

CMD ["/bin/bash"]
