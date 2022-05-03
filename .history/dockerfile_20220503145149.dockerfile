FROM python:3.7

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
#RUN apt update

#RUN pip install -r requirements.txt

RUN apt install python3 -y
#RUN apt install pip
RUN pip install streamlit

WORKDIR /app

COPY app.py ./

# Expose port 
ENV PORT 8501

CMD streamlit run app.py
#CMD ["python3", "./app.py"]