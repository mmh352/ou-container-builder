
FROM python:3.9-slim-buster



ENV USER="ou-user"
ENV UID="1000"
ENV GID="100"
ENV MODULE_CODE="DEMO"
ENV MODULE_PRESENTATION="21J"
ENV HOME="/home/$USER/$MODULE_CODE-$MODULE_PRESENTATION"


USER root


RUN mkdir /home/$USER && \
    useradd -u $UID -g $GID -d $HOME -m $USER


RUN apt-get update -y && \
    apt-get install -y tini git











RUN pip install --no-cache jupyterhub==1.3.0 notebook==6.0.0




RUN mkdir -p /etc/module-content/data && \
    pip install --no-cache git+https://github.com/mmh352/ou-container-content.git
COPY build/content_config.yaml /etc/module-content/config.yaml


COPY content /etc/module-content/data/











RUN mkdir /etc/jupyter
COPY build/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py
COPY build/start-notebook.sh /usr/bin/start.sh
RUN chmod a+x /usr/bin/start.sh



RUN chown -R $USER:$GID $HOME


USER $USER


WORKDIR $HOME
ENTRYPOINT ["tini", "-g", "--"]



CMD ["start.sh"]
