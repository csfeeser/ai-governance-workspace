FROM python:3.12-slim

# DejaVu gives the PDF export full Unicode coverage (dashes, curly quotes).
RUN apt-get update && apt-get install -y --no-install-recommends fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Student work lives here. Mount a volume so it survives container restarts.
ENV DATA_DIR=/data
VOLUME /data
EXPOSE 2224

CMD ["gunicorn", "-b", "0.0.0.0:2224", "-w", "1", "--threads", "4", "server:app"]
