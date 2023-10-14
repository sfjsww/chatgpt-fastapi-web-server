#FROM hub.fuxi.netease.com/ai-project/python:3.8
FROM hub.fuxi.netease.com/ai-project/python38fuxisdk012:test

COPY /aceexlibs /usr/lib
COPY . /app
WORKDIR /app


#RUN pip3 install --force fuxi-sdk[runtime,rl]==0.3.0 --extra-index-url http://ace-external:IWxhkFffc40YJPvE@apps-hp.danlu.netease.com:41842/repository/ace-external-hosted/simple --trusted-host apps-hp.danlu.netease.com
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["python3", "main.py"]
