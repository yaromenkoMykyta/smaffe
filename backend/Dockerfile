FROM python:3.11-slim

WORKDIR /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG platform='local'

RUN if [ "$platform" = "raspberry" ] ; then \
    pip install RPi.GPIO ; \
    fi

COPY . .

EXPOSE 8000

ENV PYTHONPATH="/"

CMD ["python3", "main.py"]
