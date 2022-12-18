# Superscraper

Brazilian Volleyball Super League (Women) web scraper

# Requirements

- Python 3.8+
- Scrapy 2.7.1

# Installation

$ `git clone git@github.com:openvb/superscraper.git`

# Usage

python superliga.py [Match ID]

## Example

$ `python superliga.py 1623`

Output:

```
data/1623_22-10-28_home_fluminense.csv
data/1623_22-10-28_guest_barueri-volleyball-club.csv
```

# Scraped data

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


# License
[GNU General Public License v3.0](https://github.com/openvb/superscraper/blob/main/LICENSE.md)