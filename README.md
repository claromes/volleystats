# Volley Stats

[![PyPI](https://img.shields.io/pypi/v/volleystats)](https://pypi.org/project/volleystats/)

Command-line tool to scrape volleyball statistics from Data Project Web Competition websites.

Volley Stats facilitates the export of data in CSV format of volleyball matches and competitions organized by entities that use Data Project WCM. The tool streamlines the collection of individual matches, match lists, and automates the retrieval of individual match data from the competition matches list.

Additionally, it documents the structure of URLs for Web Competition websites, simplifying the search for identifiers (mID, ID, PID), and also supplies acronyms for the main entities utilizing Data Project Management.

**This tool is not affiliated with Genius Sports Italy.**

## Installation

### Requirement

- Python 3.8+

```shell
pip install volleystats
```

# Documentation

- [Extracted Data](#extracted-data)
- [Usage](#usage)
    - [Match](#match)
    - [Competition Matches](#competition-matches)
    - [Competition Matches with PID](#competition-matches-with-pid)
    - [Matches via Competition Matches file](#matches-via-competition-matches-file)
    - [Help](#help)
    - [Log](#log)
    - [Output messages](#output-messages)
- [Data Project Web Competition URLs structure](#data-project-web-competition-urls-structure)
    - Hostname
    - Pathnames and search parameters
- [Federations, Confederations and Leagues Acronym](#federations-confederations-and-leagues-acronym)
    - European Volleyball
    - South American Volleyball
- [Troubleshooting](#troubleshooting)
    - [Match files collected from batch file](#match-files-collected-from-batch-file)

## Extracted Data

- Competition
    - Competition ID
    - Home Team
    - Guest Team
    - Home Points
    - Guest Points
    - Date
    - Location

- Match
    - Match ID
    - Match date
    - Home Team
    - Guest Team
    - Coach
    - Location
    - Total Points
    - Break Points
    - Win-Lost
    - Total Serves
    - Serve Erros
    - Serve Points
    - Total Receptions
    - Reception Erros
    - Positive Pass Percentage (Pos%)
    - Excellent/ Perfect Pass Percentage (Exc.%)
    - Total Attacks
    - Attack Erros
    - Blocked Attack
    - Attack Points (Exc.)
    - Attack Points Percentage (Exc.%)
    - Block Points

## Usage

```
volleystats [--help] --fed FED (--match MATCH | --comp COMP | --batch CSV_FILE_PATH) [--pid PID] [--log]
```

- `--fed`, `-f`: Federation Acronym (required)
- `--match`, `-m`: Statistics of a single match (required, unless `--comp` or `--batch` are provided)
- `--comp`, `-c`: List of matches in a competition (required, unless `--match` or `--batch` are provided)
- `--pid`, `-p`: PID of the competition (optional, only when `--comp` is provided)
- `--batch`, `-b`: CSV file path with Match IDs (Competition Matches output) (required, unless `--match` or `--comp` are provided)
- `--log`, `-l`: View the logging during scraping
- `--help`, `-h`: Show help message

### Match

```shell
volleystats --fed FED --match MATCH
```

#### Examples

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/MatchStatistics.aspx?mID=1623
    - Federation Acronym: CBV
    - Match ID: 1623
    - Command: $ `volleystats --fed cbv --match 1623`
    - Output files:
        ```
        data/cbv-1623-22-10-28-guest-barueri-volleyball-club.csv
        data/cbv-1623-22-10-28-home-fluminense.csv
        ```

- Lithuanian Volleyball Federation
    - Data Project website: https://lvf-web.dataproject.com/MatchStatistics.aspx?mID=2093
    - Federation Acronym: LVF
    - Match ID: 2093
    - Command: $ `volleystats --fed lvf --match 2093`
    - Output files:
        ```
        data/lvf-2093-2022-11-23-guest-jonavos-sc.csv
        data/lvf-2093-2022-11-23-home-svaja-viktorija-lsu.csv
        ```

### Competition Matches

```shell
volleystats --fed FED --comp COMP
```

#### Example

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/CompetitionMatches.aspx?ID=18
    - Federation Acronym: CBV
    - Competition ID: 18
    - Command: $ `volleystats --fed cbv --comp 18`
    - Output file:
        ```
        data/cbv-18-2022-2023-competition-matches.csv
        ```

### Competition Matches with PID

In some competitions, PID can be used to distinguish between seasons, such as regular season and playoffs. Therefore, it is necessary to submit this value to obtain statistics separately.

```shell
volleystats --fed FED --comp COMP --pid PID
```

#### Examples

- Bundesliga
    - Data Project website: https://vbl-web.dataproject.com/CompetitionMatches.aspx?ID=162&PID=173
    - Federation Acronym: VBL
    - Competition ID: 162
    - PID: 173
    - Season: Regular
    - Command: $ `volleystats --fed vbl --comp 162 --pid 173`
    - Output file:
        ```
        data/vbl-162-173-2022-2023-competition-matches.csv
        ```
    ---
    - Data Project website: https://vbl-web.dataproject.com/CompetitionMatches.aspx?ID=162&PID=174
    - Federation Acronym: VBL
    - Competition ID: 162
    - PID: 174
    - Season: Playoffs
    - Command: $ `volleystats --fed vbl --comp 162 --pid 174`
    - Output file:
        ```
        data/vbl-162-174-2023-2023-competition-matches.csv
        ```

### Matches via Competition Matches file

```shell
volleystats --fed FED --batch CSV_FILE_PATH
```

#### Example

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/MatchStatistics.aspx?mID=ID
    - Federation Acronym: CBV
    - CSV file path (output of the [Competition Matches](#competition-matches)): data/cbv-18-2022-2023-competition-matches.csv
    - Command: $ `volleystats --fed cbv --batch data/cbv-18-2022-2023-competition-matches.csv`
    - Output files:
        ```
        data/cbv-1623-22-10-28-guest-barueri-volleyball-club.csv
        data/cbv-1623-22-10-28-home-fluminense.csv
        data/cbv-1618-2022-11-01-guest-energis-8-s-o-caetano.csv
        data/cbv-1618-2022-11-01-home-esporte-clube-pinheiros.csv
        data/cbv-1619-2022-11-01-guest-abel-moda-volei.csv
        data/cbv-1619-2022-11-01-home-gerdau-minas.csv
        ...
        ```

### Help

```shell
volleystats --help
```

### Log
```shell
volleystats --fed FED (--match MATCH | --comp COMP | --batch CSV_FILE_PATH) --log
```

### Output messages

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
volleystats: data/cbv-1623-22-10-28-home-fluminense.csv file was created
volleystats: data/cbv-1623-22-10-28-guest-barueri-volleyball-club.csv file was created
volleystats: finished
```

## Data Project Web Competition URLs structure

- Hostname: `<Fed_Acronym>`-web.dataproject.com

- Pathnames and search parameters:
    - /MainHome

    - /History?ID=`<Fed_ID>`

    - /CompetitionHome?ID=`<Category_ID>` (*could be Women, Men, Pro or Youth, e.g.*)

    - /CompetitionMatches?ID=`<Competition_ID>`&PID=`<PID>` (*PID could be regular season or playoffs, e.g.*)

    - /MatchStatistics?mID=`<Match_ID>`&ID=`<Competition_ID>`

## Federations, Confederations and Leagues Acronyms

**European Volleyball**

- `fshv`: [Albanian Volleyball Federation](https://fshv-web.dataproject.com/MainHome.aspx)
- `bvl`: [Baltic League](https://bvl-web.dataproject.com/MainHome.aspx)
- `bevl`: [Belgium Volleyball Federation](https://bevl-web.dataproject.com/MainHome.aspx)
- `osbih`: [Bosnia and Herzegovina Volleyball Federation](https://osbih-web.dataproject.com/MainHome.aspx)
- `bvf`: [Bulgarian Volleyball Federation](https://bvf-web.dataproject.com/MainHome.aspx)
- `vbl`: [Bundesliga](https://vbl-web.dataproject.com/MainHome.aspx)
- `hos`: [Croatian Volleyball Federation](https://hos-web.dataproject.com/MainHome.aspx)
- `cvf`: [Czech Volleyball Federation](https://cvf-web.dataproject.com/MainHome.aspx)
- `evf`: [Estonian Volleyball Federation](https://evf-web.dataproject.com/MainHome.aspx)
- `fbf`: [Faroe Islands Volleyball Association](https://fbf-web.dataproject.com/MainHome.aspx)
- `lml`: [Finland Volleyball League](https://lml-web.dataproject.com/MainHome.aspx)
- `eope`: [Hellenic Volleyball Federation](https://eope-web.dataproject.com/MainHome.aspx)
- `hvl`: [Hellenic Volleyball League](https://hvl-web.dataproject.com/MainHome.aspx)
- `hvf`: [Hungary Volleyball Federation](https://hvf-web.dataproject.com/MainHome.aspx)
- `bli`: [Icelandic Volleyball Association](https://bli-web.dataproject.com/MainHome.aspx)
- `iva`: [Israel Volleyball Association](https://iva-web.dataproject.com/MainHome.aspx)
- `fipav`: [Italian Volleyball Federation](https://fipav-web.dataproject.com/MainHome.aspx)
- `vfrk`: [Volleyball Federation of Republic of Kazakhstan](https://vfrk-web.dataproject.com/MainHome.aspx)
- `latvf`: [Latvian Volleyball Federation](https://latvf-web.dataproject.com/MainHome.aspx)
- `lnv`: [Ligue Nationale de Volley](https://lnv-web.dataproject.com/MainHome.aspx)
- `lvf`: [Lithuanian Volleyball Federation](https://lvf-web.dataproject.com/MainHome.aspx)
- `mva`: [Malta Volleyball Association](https://mva-web.dataproject.com/MainHome.aspx)
- `nvbf`: [Norwegian Volleyball Federation](https://nvbf-web.dataproject.com/MainHome.aspx)
- `fpv`: [Portuguese Volleyball Federation](https://fpv-web.dataproject.com/MainHome.aspx)
- `frv`: [Romanian Volleyball Federation](https://frv-web.dataproject.com/MainHome.aspx)
- `ossrb`: [Serbian Volleyball Federation](https://ossrb-web.dataproject.com/MainHome.aspx)
- `svf`: [Slovak Volleyball Federation](https://svf-web.dataproject.com/MainHome.aspx)
- `ozs`: [Slovenian Volleyball Federation](https://ozs-web.dataproject.com/MainHome.aspx)
- `rfevb`: [Spanish Volleyball Federation](https://rfevb-web.dataproject.com/MainHome.aspx)
- `svbf`: [Swedish Volleyball Federation](https://svbf-web.dataproject.com/MainHome.aspx)
- `swi`: [Swiss Volley](https://swi-web.dataproject.com/MainHome.aspx)
- `tvf`: [Turkish Volleyball Federation](https://tvf-web.dataproject.com/MainHome.aspx)
- `uvf`: [Ukrainian Volleyball Federation](https://uvf-web.dataproject.com/MainHome.aspx)
- `pvlu`: [Professional Volleyball League of Ukraine](https://pvlu-web.dataproject.com/MainHome.aspx)

**South American Volleyball**

- `feva`: [Argentine Volleyball Federation](https://feva-web.dataproject.com/MainHome.aspx)
- `cbv`: [Brazilian Volleyball Confederation](https://cbv-web.dataproject.com/MainHome.aspx)
- `fcv`: [Cordoba Volleyball Federation](https://fcv-web.dataproject.com/MainHome.aspx)
- `fpdv`: [Peruvian Volleyball Federation](https://fpdv-web.dataproject.com/MainHome.aspx)

## Troubleshooting

### Match files collected from batch file

In some cases, empty files may be returned, usually named as `<fed_acronym>-<match_id>-guest_stats.csv` and `<fed_acronym>-<match_id>-home_stats.csv`. This can happen due to the hiding of a match in the competition listing, either because it was canceled or incorrectly entered. The match is hidden from view, but it remains accessible in the HTML, causing the tool to return an empty file. In such cases, simply ignore and delete this file.

It can also happen that the data is only available in PDF, which makes scraping impossible.

## Development

$ `git clone git@github.com:claromes/volleystats.git`

$ `cd volleystats`

$ `pip install -r requirements.txt`

$ `pip install --editable .`

## Author

[Claromes](https://claromes.com)
