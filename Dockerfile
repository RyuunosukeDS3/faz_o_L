FROM python:latest
WORKDIR /workspace

COPY ./* /workspace
RUN pip install -r requirements.txt

CMD python /workspace/main.py