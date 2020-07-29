FROM homeassistant/raspberrypi3-homeassistant:0.113.2

COPY lights /lights
RUN pip3 install -r /lights/requirements.txt

COPY start.sh /tmp/start.sh
RUN chmod +x /tmp/start.sh

COPY ui-lovelace.yaml /tmp/ui-lovelace.yaml
COPY configuration.yaml /tmp/configuration.yaml

CMD ["bash","/tmp/start.sh"]
