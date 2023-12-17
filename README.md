# Volley Stats

[![PyPI](https://img.shields.io/pypi/v/volleystats)](https://pypi.org/project/volleystats/) [![License)](https://img.shields.io/github/license/claromes/volleystats)](https://github.com/claromes/volleystats/blob/main/LICENSE.md)

CLI tool to get volleyball statistics from the Data Project Web Competition websites (WCM)

**This tool is not affiliated with Genius Sports Company**

## Requirements

- Python 3.8+

## Installation

```shell
pip install volleystats
```

## Usage

```
volleystats [--help] --fed FED (--match MATCH | --comp COMP) [--log]
```

- `--fed`, `-f`: Federation Acronym (required)
- `--match`, `-m`: Statistics of a single match (required, unless `--comp` is provided)
- `--comp`, `-c`: List of matches in a competition (required, unless `--match` is provided)
- `--log`, `-l`: View the logging during scraping
- `--help`, `-h`: Show help

## Federations and Leagues Acronym

**European Volleyball**

- `fshv`: Albanian Volleyball Federation
- `osbih`: Bosnia and Herzegovina Volleyball Federation
- `bvf`: Bulgarian Volleyball Federation
- `bvl`: Baltic League
- `vbl`: Bundesliga
- `hos`: Croatian Volleyball Federation
- `cvf`: Czech Volleyball Federation
- `dvbf`: Danish Volleyball Federation
- `evf`: Estonian Volleyball Federation
- `fbf`: Faroe Islands Volleyball Association
- `eope`: Hellenic Volleyball Federation
- `hvf`: Hungary Volleyball Federation
- `bli`: Icelandic Volleyball Association
- `iva`: Israel Volleyball Association
- `fipav`: Italian Volleyball Federation
- `lvf`: Lithuanian Volleyball Federation
- `mva`: Malta Volleyball Association
- `nvbf`: Norwegian Volleyball Federation
- `fpv`: Portuguese Volleyball Federation
- `frv`: Romanian Volleyball Federation
- `ossrb`: Serbian Volleyball Federation
- `svf`: Slovak Volleyball Federation
- `ozs`: Slovenian Volleyball Federation
- `rfevb`: Spanish Volleyball Federation
- `svbf`: Swedish Volleyball Federation
- `swi`: Swiss Volley
- `tvf`: Turkish Volleyball Federation
- `pvlu`: Professional Volleyball League of Ukraine

**South American Volleyball**

- `feva`: Argentine Volleyball Federation
- `cbv`: Brazilian Volleyball Confederation
- `fcv`: Cordoba Volleyball Federation
- `fpdv`: Peruvian Volleyball Federation

## Data Project Web Competition endpoints

- Base URL: `<Fed_Acronym>`-web.dataproject.com

- Endpoins:
    - /MainHome

    - /History?ID=`<Fed_ID>`

    - /CompetitionHome?ID=`<Category_ID>` (*could be female and male, pro or young*)

    - /CompetitionMatches?ID=`<Competition_ID>`

    - /MatchStatistics?mID=`<Match_ID>`&ID=`<Competition_ID>`

## Available Page Locales

- pt-BR
- en-GB

## Docs

- [Usage examples](https://github.com/claromes/volleystats/blob/main/docs/EXAMPLES.md)
- [Roadmap](https://github.com/claromes/volleystats/blob/main/docs/ROADMAP.md)
- [Changelog](https://github.com/claromes/volleystats/blob/main/docs/CHANGELOG.md)

## Development

$ `git clone git@github.com:claromes/volleystats.git`

$ `cd volleystats`

$ `pip install -r requirements.txt`

$ `pip install --editable .`

## License

The package is licensed under the terms of the [GNU General Public License v3.0](https://github.com/claromes/volleystats/blob/main/LICENSE.md)

## Author

Claromes ([GitHub](https://github.com/claromes))
