![screenshot](https://raw.githubusercontent.com/agmmnn/etym-cli/master/imgs/ss.png)

Command-line tool for [etymonline.com](https://www.etymonline.com/), the Online Etymology Dictionary with rich output.

## Install

```
pip install etym-cli
```

## Usage

```
etym <word>
```

```
etym lawyer
```

![output](https://raw.githubusercontent.com/agmmnn/etym-cli/master/imgs/output.png)

## Arguments

```
-p, --plain plain text output
$ etym -p lawyer
lawyer (n.)
late 14c. lauier, lawer, lawere (mid-14c. as a surname), "one versed in law, one whose profession is suits in court...

-t, --trend returns trending words
$ etym -t
Trending Words:

1. self, 2. science, 3. genus, 4. poliomyelitis, 5. water, 6. witch, 7. light, 8. understand, 9. demon, 10. person

-f, --fuzzy returns fuzzy search results
$ etym -f la
la, la tene, la-di-da, la-la, la-z-boy, lab, labarum, labefaction, label, labia, labial, labialize, labiate, labile,
labio-
```

# License

MIT
