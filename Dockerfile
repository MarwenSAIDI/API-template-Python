FROM python:3.13

WORKDIR /api

COPY . .

RUN apt-get update 
RUN pip install --no-cache-dir -r app/requirements.txt

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]