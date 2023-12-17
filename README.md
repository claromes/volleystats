# Volley Stats

[![PyPI](https://img.shields.io/pypi/v/volleystats)](https://pypi.org/project/volleystats/) [![License)](https://img.shields.io/github/license/claromes/volleystats)](https://github.com/claromes/volleystats/blob/main/LICENSE.md)

CLI tool to get volleyball statistics from the Data Project Web Competition websites (WCM)

> [!IMPORTANT]
> This tool is not affiliated with Genius Sports Company

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

volleystats: started

volleystats: data/1623_22-10-28_home_fluminense.csv file was created!

volleystats: data/1623_22-10-28_guest_barueri-volleyball-club.csv file was created!

volleystats: finished
```

## CLI

### Match

>Stats of a match in separate files (home and guest).

$ `volleystats --fed <Federation Acronym> --match <Match ID>`

**Examples**

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/MatchStatistics.aspx?mID=1623
    - Federation Acronym: CBV
    - Match ID: 1623
    - Command: $ `volleystats --fed cbv --match 1623`
    - Output files:
        ```
        data/1623_22-10-28_home_fluminense.csv
        data/1623_22-10-28_guest_barueri-volleyball-club.csv
        ```

- Lithuanian Volleyball Federation
    - Data Project website: https://lvf-web.dataproject.com/MatchStatistics.aspx?mID=2093
    - Federation Acronym: LVF
    - Match ID: 2093
    - Command: $ `volleystats --fed lvf --match 2093`
    - Output files:
        ```
        data/2093_2022-11-23_guest_jonavos-sc.csv
        data/2093_2022-11-23_home_svaja-viktorija-lsu.csv
        ```
<br>

### Competition Matches

>List of matches in a competition.

$ `volleystats --fed <Federation Acronym> --comp <Competition ID>`

**Examples**

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com//CompetitionMatches.aspx?ID=18
    - Federation Acronym: CBV
    - Competition ID: 18
    - Command: $ `volleystats --fed cbv --comp 18`
    - Output files:
        ```
        data/18_competition_matches.csv
        ```
<br>

### Help

>Show help message.

$ `volleystats --help`

<br>

### Log

>Set logging.

$ `volleystats --fed <Federation Acronym> [--match MATCH] [--comp COMP] --log`

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

## Main WCM endpoints

- Base URL: `<Fed_Acronym>`-web.dataproject.com

- Endpoins:
    - /MainHome

    - /History?ID=`<ID_Fed>`

    - /CompetitionHome?ID=`<Category_ID>` (*could be female and male, pro or young*)

    - /CompetitionMatches?ID=`<Competition_ID>`

    - /MatchStatistics?mID=`Match_ID>`&`ID=Competition_ID>`

## Available Page Locales

- pt-BR
- en-GB

## Available Data (WIP)

- Competition
    - [x] Competition ID
    - [x] Home Team
    - [x] Guest Team
    - [ ] Home Points
    - [ ] Guest Points
    - [ ] Date
    - [ ] Location

- Match
    - [x] Match ID
    - [x] Match date
    - [x] Home Team
    - [x] Guest Team
    - [ ] Coach
    - [ ] Location
    - [ ] Final result
    - [ ] Result per SET

- Vote
    - [ ] Vote by player

- Points
    - [x] Total Points by player
    - [ ] Total Points by player per SET
    - [x] Break Points by player
    - [x] Win-Lost by player
    - [x] Totals

- Serve
    - [ ] Total Serves by player
    - [ ] Serve Erros by player
    - [ ] Serve Points by player
    - [ ] Totals

- Reception
    - [ ] Total Receptions by player
    - [ ] Reception Erros by player
    - [ ] Positive Pass Percentage by player
    - [ ] Excellent/ Perfect Pass Percentage by player
    - [ ] Totals

- Attack
    - [ ] Total Attacks by player
    - [ ] Attack Erros by player
    - [ ] Blocked Attack by player
    - [ ] Attack Points by player
    - [ ] Attack Points Percentage by player
    - [ ] Totals

- Block
    - [ ] Block Points by player
    - [ ] Totals

## Development

$ `git clone git@github.com:claromes/volleystats.git`

$ `cd volleystats`

$ `pip install -r requirements.txt`

$ `pip install --editable .`

## License

The package is licensed under the terms of the [GNU General Public License v3.0](LICENSE.md)

## Author

[Claromes](https://claromes.gitlab.io)
