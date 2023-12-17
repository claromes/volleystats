# Examples

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
### Competition Matches

```shell
volleystats --fed FED --comp COMP
```

- Brazilian Volleyball Confederation
    - Data Project website: https://cbv-web.dataproject.com//CompetitionMatches.aspx?ID=18
    - Federation Acronym: CBV
    - Competition ID: 18
    - Command: $ `volleystats --fed cbv --comp 18`
    - Output files:
        ```
        data/18_competition_matches.csv
        ```

### Help

```shell
volleystats --help
```

### Log
```shell
volleystats --fed FED (--match MATCH | --comp COMP) --log
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
volleystats: data/1623_22-10-28_home_fluminense.csv file was created
volleystats: data/1623_22-10-28_guest_barueri-volleyball-club.csv file was created
volleystats: finished
```
