FROM python:3-alpine
COPY app.py /app.py
RUN pip install flask
RUN pip install requests
CMD ["python", "/app.py"]