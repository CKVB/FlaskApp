FROM ck1998/ubuntu:1
COPY . /userAppProject
WORKDIR /userAppProject
RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8 
ENV LANG=C.UTF-8
ENV SECRET_KEY=secretkey
ENV FLASK_ENV=production
ENV SQLALCHEMY_TRACK_MODIFICATIONS=False
ENV SQLALCHEMY_ECHO=False
ENV DATABASE_URL=sqlite:///users.db

CMD gunicorn --workers=5 --bind 0.0.0.0:$PORT wsgi:app
