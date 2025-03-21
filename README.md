# Wiktionary Migaku Dictionary

_Parses a Wiktionary database dump into a [Migaku Dictionary](https://github.com/migaku-official/Migaku-Dictionary-Addon) (Anki add-on)._

![Continuous Integration](https://github.com/Irio/migaku-wiktionary/workflows/Continuous%20Integration/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/072ef425b8fe05dc20ff/maintainability)](https://codeclimate.com/github/Irio/migaku-wiktionary/maintainability)

## Build

Before running the application, you need to setup the environment. We recommend using pyenv as part of that setup.

```shell
pyenv virtualenv 3.8.3 migaku_wiktionary
pyenv activate migaku_wiktionary
pip install -r requirements.txt
```

## Usage

```shell
python cli.py --help
python cli.py --lang de download
python cli.py --xml /tmp/dewiktionary-*.xml convert
```

To install one of the exported dictionaries into the Anki's add-on, run the following snippet:

```shell
time python cli.py --xml data/dewiktionary-latest-pages-meta-current.xml convert
export DICTIONARY_PATH=~/Library/Application\ Support/Anki2/addons21/Migaku\ Dictionary/user_files/dictionaries/German/de_deutsch
mkdir -p $DICTIONARY_PATH
cp /tmp/de_deutsch.json $DICTIONARY_PATH/de_deutsch.json
```

## Testing

The project is backed by a test suite. Run it with the following command:

```shell
pip install -r requirements-dev.txt
pytest -vv --cov=migaku_wiktionary
```

<<<<<<< HEAD
This file changed to others.
Okay
=======
You can change this file successfully.
>>>>>>> 83da5adda5a65d6242d8b24f2a58acd4d2d02231
