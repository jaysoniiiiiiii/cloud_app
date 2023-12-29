FROM python:3.10

RUN . /bin/activate


RUN pip freeze > requirements.txt


RUN from app import db
RUN db.create_all()

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
