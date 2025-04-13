FROM python:3.11-slim

WORKDIR /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG platform='local'

RUN if [ "$platform" = "raspberry" ] ; then \
    apt install -y --no-cache python3-rpi.gpio \
    && pip install RPi.GPIO \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    fi

COPY . .

EXPOSE 8000

ENV PYTHONPATH="/"

CMD ["python3", "main.py"]
