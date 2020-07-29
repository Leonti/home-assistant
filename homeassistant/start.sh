#!/bin/bash

# Revert once lights are configured
#cp /tmp/configuration.yaml /config/configuration.yaml
cp /tmp/ui-lovelace.yaml /config/ui-lovelace.yaml

python -m homeassistant --config /config
