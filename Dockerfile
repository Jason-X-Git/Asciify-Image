FROM python:3.10

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . ./

EXPOSE 8000
CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "--port", "8000", "main:app"]