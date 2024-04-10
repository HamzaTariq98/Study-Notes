FROM python:3.11-slim



# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# RUN pip install --upgrade pip

WORKDIR /app


# RUN chmod +x /app/src

# RUN pip install --no-cache-dir --upgrade -r code/src/requirements.txt


COPY src/requirements.txt src/requirements.txt

RUN pip install -r src/requirements.txt

COPY src src
RUN pip install ./src


# WORKDIR /code/src

# ENV PYTHONPATH "${PYTHONPATH}:/code/src"

COPY api.py .

EXPOSE 8005

CMD ["bash"]
