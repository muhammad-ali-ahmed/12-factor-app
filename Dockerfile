FROM python:3.12 as builder

WORKDIR /app

COPY ./* ./

RUN pip install -r requirements.txt --no-cache-dir


FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/

COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]