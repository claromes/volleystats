# volleystats

[![PyPI](https://img.shields.io/pypi/v/volleystats)](https://pypi.org/project/volleystats/)

`volleystats` is a CLI tool to get volleyball statistics from the Data Project Web Competition websites (WCM)

**This tool is not affiliated with Data Project.**

## Requirements

- Python 3.8+

## Installation

```shell
pip3 install volleystats
```

## Usage
```
volleystats --fed cbv --match 1623
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
	    volleystats

volleystats: started!

volleystats: data/1623_22-10-28_home_fluminense.csv file was created!

volleystats: data/1623_22-10-28_guest_barueri-volleyball-club.csv file was created!

volleystats: finished!
```

## Available Data (WIP)

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

## [Documentation](https://openvb.github.io/volleystats)

## Development

$ `git clone git@github.com:claromes/volleystats.git`

$ `cd volleystats`

$ `pip install -r requirements.txt`
