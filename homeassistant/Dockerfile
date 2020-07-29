FROM homeassistant/raspberrypi3-homeassistant:0.113.2

COPY ui-lovelace.yaml /tmp/ui-lovelace.yaml
COPY configuration.yaml /tmp/configuration.yaml
COPY start.sh /tmp/start.sh

COPY lights /lights
RUN pip3 install -r /lights/requirements.txt

RUN chmod +x /tmp/start.sh

CMD ["bash","/tmp/start.sh"]
