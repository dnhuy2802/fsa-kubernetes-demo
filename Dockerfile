FROM python:3.11.7-alpine3.19

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

# CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]