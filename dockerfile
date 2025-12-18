FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app.py backend/init_db.py ./
COPY backend/templates/ templates/
COPY scripts/run.sh ./

RUN chmod +x run.sh

EXPOSE 5000
CMD ["./run.sh"]
