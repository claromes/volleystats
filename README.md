# Matchscraper

[![PyPI](https://img.shields.io/pypi/v/matchscraper)](https://pypi.org/project/matchscraper/)

CLI tool to get volleyball match statistics from the *Web Competition by Data Project* websites in CSV format.

**This tool is not affiliated with Data Project.**

## Requirements

- Python 3.8+

## Installation

```shell
pip3 install matchscraper
```

## Usage
```
matchscraper --fed cbv --match 1623
```

```
                    .
                    |`.
                    |  `.
                    |-_  `.
                    |  -_  `._
____________________|____-_ _|_______________,
',                         -_|                ',
  ',                         |                  ',
    ',                       |                    ',
      ',_____________________|______________________',
	    Matchscraper

Matchscraper: started!

Matchscraper: data/1623_22-10-28_home_fluminense.csv file was created!

Matchscraper: data/1623_22-10-28_guest_barueri-volleyball-club.csv file was created!

Matchscraper: finished!
```

## Scraped data (WIP)

- Competition
    - Competition ID
    - Home Team
    - Guest Team

- Match
    - Match ID
    - Match date
    - Home Team
    - Guest Team

- Points
    - Total Points by player
    - Break Points by player
    - Win-Lost by player
    - Totals

## [Documentation](https://claromes.github.io/matchscraper/)

## Development

$ `git clone git@github.com:claromes/matchscraper.git`

$ `cd matchscraper`

$ `pip install -r requirements.txt`
