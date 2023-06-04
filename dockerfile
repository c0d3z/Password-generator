FROM python:3.9-slim

WORKDIR app/

COPY main.py .

RUN pip install pytest

COPY . .

CMD ["python", "main.py"]
