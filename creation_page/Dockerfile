FROM python:3.9.13

# this is for the non-root user way of starting the container

ARG USER=adminuser
ARG UID=1000
ARG GID=1000
ARG PW=adminuser
RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | \
      chpasswd
USER ${UID}:${GID}
WORKDIR /home/${USER}

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
COPY --chown=adminuser:adminuser . /app
CMD sleep 50s && python3 main.py
