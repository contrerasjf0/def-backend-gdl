FROM python:3.5
COPY apiDamificados/requirements.txt /apiDamificados/requirements.txt
RUN pip install -r /apiDamificados/requirements.txt  
WORKDIR /apiDamificados
COPY apiDamificados /apiDamificados
<<<<<<< HEAD
#CMD gunicorn --bind 0.0.0.0:8000 apiDamificados.wsgi:application
CMD sh auto.sh
=======
# CMD gunicorn --bind 0.0.0.0:8000 apiDamificados.wsgi:application
CMD sh auto.sh
>>>>>>> 2882e28efd676cb341c600d5c99284f137e5873a
