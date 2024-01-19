# Usage examples

### Match

```shell
volleystats --fed FED --match MATCH
```

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/MatchStatistics.aspx?mID=1623
    - Federation Acronym: CBV
    - Match ID: 1623
    - Command: $ `volleystats --fed cbv --match 1623`
    - Output files:
        ```
        data/cbv-1623-22-10-28-home-fluminense.csv
        data/cbv-1623-22-10-28-guest-barueri-volleyball-club.csv
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

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com//CompetitionMatches.aspx?ID=18
    - Federation Acronym: CBV
    - Competition ID: 18
    - Command: $ `volleystats --fed cbv --comp 18`
    - Output file:
        ```
        data/cbv-18-2022-2023-competition-matches.csv
        ```

### Matches via Competition Matches file

```shell
volleystats --fed FED --batch CSV_PATH_FILE
```

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com/MatchStatistics.aspx?mID=ID
    - Federation Acronym: CBV
    - CSV batch file (output of the [Competition Matches](#competition-matches)): data/cbv-18-2022-2023-competition_matches.csv
    - Command: $ `volleystats --fed cbv --batch data/cbv-18-2022-2023-competition_matches.csv`
    - Output files:
        ```
        data/cbv-1623-22-10-28-home-fluminense.csv
        data/cbv-1623-22-10-28-guest-barueri-volleyball-club.csv
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
volleystats --fed FED (--match MATCH | --comp COMP | --batch CSV_PATH_FILE) --log
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
