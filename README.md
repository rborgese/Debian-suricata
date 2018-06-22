# Debian-suricata

This is a WIP(Work-In-Progress) GUI that allow the user to easily install or remove suricata from their system and it will feature a "Control center" for managing rules, reviewing logs and probably more...

## Requirements

```
beautifulsoup4
pytest
bottle
pycrypto
gevent-websocket
websocket-client
```

I recommend setting up a virtual environment

There is a bottle server that requires bottle, gevent-websocket and websocket-client.

And there is an http server that only requires beautifulsoup4 it is built using python's standard network libs (It will eventually be deprecated).

But for now you can install all dependencies using:

 ```
 pip install -r requirements.text
 ```

 It will also install pycrypto and pytest however neither encryption nor tests are implemented yet
