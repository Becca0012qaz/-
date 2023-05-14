FROM python:slim

ADD ./requirements.txt /
ADD ./app /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt


# # 下载和配置浏览器驱动程序
# # 例如，下载和配置Chrome驱动程序
# RUN apt-get update && apt-get install -y wget unzip
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_$(dpkg --print-architecture))/chromedriver_linux64.zip && \
#     unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
#     rm /tmp/chromedriver.zip


EXPOSE 5000

CMD ["python", "app.py"]
