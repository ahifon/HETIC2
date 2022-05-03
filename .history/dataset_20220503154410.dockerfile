FROM ubuntu

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

#RUN apt update

#RUN pip install -r requirements.txt

RUN apt install python3 -y
#RUN apt install pip
RUN pip install sklearn

WORKDIR /app

COPY generate.py ./

# Expose port 
ENV PORT 80000

CMD streamlit run app.py
#CMD ["python3", "./generate.py"]