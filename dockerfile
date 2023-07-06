FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "uvicorn", "index:app","--host","0.0.0.0","--reload" ,"--port","8000" ]