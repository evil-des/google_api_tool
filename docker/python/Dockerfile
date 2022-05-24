FROM python:3.7

COPY ../g_api_tool /srv/www/google_api_tool/g_api_tool
COPY ../requirements.txt /srv/www/google_api_tool
COPY ../setup.py /srv/www/google_api_tool

WORKDIR /srv/www/google_api_tool
RUN pip install -r requirements.txt
RUN pip install -e .

WORKDIR /srv/www/google_api_tool/g_api_tool