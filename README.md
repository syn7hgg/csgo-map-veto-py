# CS:GO Map Veto

[![](https://img.shields.io/github/issues/synth-dev/csgo-map-veto-py?style=flat-square)
](https://github.com/synth-dev/csgo-map-veto-py/issues)
[![](https://img.shields.io/github/license/synth-dev/csgo-map-veto-py?style=flat-square)]()

A command-line map veto system for CS:GO written in Python 3.

## Installation
First of all, make sure to have installed Python 3.2 or above. Else the script won't run.

Download the latest release from the [releases page](https://github.com/synth-dev/csgo-map-veto-py/releases), extract the zip file
to an easy to remember, convenient place.

Inside the extracted folder, open a terminal and run the following command:

```bash
pip install -r requirements.txt
```

This will automatically install all required libraries and packages for you.

The script is now all set and ready to go. Just run this command:

```bash
python main.py
```

if you're on Windows. If that doesn't work or you're on Linux/Mac, the execute:

```bash
python3 main.py
```

## Usage

#### Creating and modifying map pools
You can use the default map pools this project already comes with or you can also create
your own. In order to do that, just create a JSON file inside the ``pools/`` directory and
follow this structure:

```json
{
  "pool_name": "An awesome name for the map pool",
  "maps": [
    "Map 1",
    "Map 2",
    "Map 3",
    "Mapssss",
    "More Mapssssss",
    "Enough"
  ]
}
```

#### Veto Types
This project currently supports both Bo1 and Bo3 veto/picks. You'll be asked to choose a veto type
when using the app.

##### Bo1 Veto
> Ban/Ban/Ban/Ban/Ban until 3 maps remain, then Random

##### Bo3 Veto
> Ban/Ban/Pick/Pick/Ban/Ban/Ban until 3 maps remain, then Random

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://mit-license.org/)