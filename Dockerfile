FROM python:3.7.2
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 
