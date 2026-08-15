FROM python:3.12-alpine

RUN addgroup -S app && adduser -S -G app app
WORKDIR /app
COPY app ./app
USER app
ENTRYPOINT ["python", "-m", "app.job"]
