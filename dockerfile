FROM python:3.9-slim

WORKDIR .

COPY main.py .

RUN pip install pytest

CMD ["python", "main.py"]
