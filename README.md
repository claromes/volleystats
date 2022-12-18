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
- [x] Total Points by player
- [x] Break Points by player
- [x] W-L by player

# TODO

- readme
    - complete scraped data list
    - list of each term