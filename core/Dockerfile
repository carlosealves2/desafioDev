FROM python:3.9.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt update && apt upgrade -y && apt install netcat -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/core/entrypoint.sh" ]
CMD [ "run" ]
