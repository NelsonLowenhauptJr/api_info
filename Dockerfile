FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR .
COPY requirements.txt ./app/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r ./app/requirements.txt
COPY . ./app/
EXPOSE 8000