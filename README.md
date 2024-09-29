# Care Livekit

[![Release Status](https://img.shields.io/pypi/v/care_livekit.svg)](https://pypi.python.org/pypi/care_livekit)
[![Build Status](https://github.com/ohcnetwork/care_livekit/actions/workflows/build.yaml/badge.svg)](https://github.com/ohcnetwork/care_livekit/actions/workflows/build.yaml)

Care Livekit is a plugin for care to add voice auto fill support using external services like OpenAI whisper and Google Speech to Text.

## Features

- Voice auto fill support for care
- Support for OpenAI whisper and Google Speech to Text

## Installation

https://care-be-docs.ohc.network/pluggable-apps/configuration.html

https://github.com/ohcnetwork/care/blob/develop/plug_config.py

To install care livekit, you can add the plugin config in [care/plug_config.py](https://github.com/ohcnetwork/care/blob/develop/plug_config.py) as follows:

```python
...

livekit_plug = Plug(
    name="livekit",
    package_name="git+https://github.com/ohcnetwork/care_livekit.git",
    version="@master",
    configs={},
)
plugs = [livekit_plug]
...
```

## Local Development

To develop the plug in local environment along with care, follow the steps below:

1. Go to the care root directory and clone the plugin repository:

```bash
cd care
git clone git@github.com:ohcnetwork/care_livekit.git
```

2. Add the plugin config in plug_config.py

```python
...

livekit_plugin = Plug(
    name="livekit", # name of the django app in the plugin
    package_name="/app/care_livekit", # this has to be /app/ + plugin folder name
    version="", # keep it empty for local development
    configs={}, # plugin configurations if any
)
plugs = [livekit_plug]

...
```

3. Tweak the code in plugs/manager.py, install the plugin in editable mode

```python
...

subprocess.check_call(
    [sys.executable, "-m", "pip", "install", "-e", *packages] # add -e flag to install in editable mode
)

...
```

4. Rebuild the docker image and run the server

```bash
make re-build
make up
```

[!IMPORTANT]: Do not push these changes in a PR. These changes are only for local development.

## Configuration

The following configurations variables are available for Care Livekit:

- `LIVEKIT_API_URL`: Websocket URL for the Livekit server, default is `wss://livekit.ohc.network`
- `LIVEKIT_API_KEY`: API key for the Livekit server
- `LIVEKIT_API_SECRET`: API secret for the Livekit server
- `LIVEKIT_ROOM_NAME_PREFIX`: Prefix for the room name, default is `care-`

The plugin will try to find the API key from the config first and then from the environment variable.

## License

This project is licensed under the terms of the [MIT license](LICENSE).

---

This plugin was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) using the [ohcnetwork/care-plugin-cookiecutter](https://github.com/ohcnetwork/care-plugin-cookiecutter).
