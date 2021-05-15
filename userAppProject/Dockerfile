FROM ubuntu
COPY . /userAppProject
WORKDIR /userAppProject
RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8 
ENV LANG=C.UTF-8
CMD ["gunicorn","--workers=5","--bind","0.0.0.0:5000","userApp:app"]