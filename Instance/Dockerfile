FROM python:3.10.4
EXPOSE 5000
WORKDIR /fourth_app
RUN pip install flask
COPY . .
CMD ["flask","run","--host","0.0.0.0"] 
