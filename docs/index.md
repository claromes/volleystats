# Matchscraper

[![PyPI](https://img.shields.io/pypi/v/matchscraper)](https://pypi.org/project/matchscraper/) [![License)](https://img.shields.io/github/license/claromes/matchscraper)](https://github.com/claromes/matchscraper/blob/main/LICENSE.md)

CLI tool to get volleyball match statistics from the *Web Competition by Data Project* websites in CSV format.

**This tool is not affiliated with Data Project.**

# Docs

## Requirements

- Python 3.8+

## Installation

```shell
pip3 install matchscraper
```

## Usage
```shell
matchscraper --match cbv 1623
```

```shell
Matchscraper: started!

Matchscraper: data/1623_22-10-28_home_fluminense.csv file was created!

Matchscraper: data/1623_22-10-28_guest_barueri-volleyball-club.csv file was created!

Matchscraper: finished!
```

## CLI
>*Match*

Stats of a match in separate files (home and guest).

$ `matchscraper --fed <Federation Acronym> --match <Match ID>`

### Examples

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/MatchStatistics.aspx?mID=1623
    - Federation Acronym: CBV
    - Match ID: 1623
    - Command: $ `matchscraper --fed cbv --match 1623`
    - Output files:
        ```
        data/1623_22-10-28_home_fluminense.csv
        data/1623_22-10-28_guest_barueri-volleyball-club.csv
        ```

- Lithuanian Volleyball Federation
    - Data Project website: https://lvf-web.dataproject.com/MatchStatistics.aspx?mID=2093
    - Federation Acronym: LVF
    - Match ID: 2093
    - Command: $ `matchscraper --fed lvf --match 2093`
    - Output files:
        ```
        data/2093_2022-11-23_guest_jonavos-sc.csv
        data/2093_2022-11-23_home_svaja-viktorija-lsu.csv
        ```
<br>

>*Competition Matches*

List of matches in a competition.

$ `matchscraper --fed <Federation Acronym> --comp <Competition ID>`

### Example

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com//CompetitionMatches.aspx?ID=18
    - Federation Acronym: CBV
    - Competition ID: 18
    - Command: $ `matchscraper --fed 18 --comp cbv`
    - Output files:
        ```
        data/18_competition_matches.csv
        ```

>*Help*

Show help message.

$ `matchscraper --help`

<br>

## Available Page Locales

- pt-BR
- en-GB

## Scraped data (WIP)

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

## Author

[claromes](https://claromes.gitlab.io/)