FROM python:3.9

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port", "8080", "--server.fileWatcherType=none"]

CMD ["app.py"]