# -*- coding: utf-8 -*-
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import json

from rich.table import Table
from rich import box
from rich import print as rprint


HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0"}


def req(page, word):
    url = "https://www.etymonline.com/" + page + quote(word)
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 404:
        rprint("[italic]Word not found.[/italic]")
        exit()
    return BeautifulSoup(r.content, "lxml")


# plain text output
def o_plain(secs):
    print()
    for ix, sec in enumerate(secs):
        title = sec.find(["h1", "h2", "h3"])
        if title:
            print(title.text.strip())
        else:
            print("[No title found]")

        pb = sec.find_all(["p", "blockquote"])
        newline = "\n" if ix != len(secs) - 1 else ""
        for j in pb:
            if j.name == "blockquote":
                print(">>" + j.text.strip())
            elif j.name == "p" and j.text.strip() != "":
                print(j.text.strip() + newline)
    print()


# rich output
def o_rich(word, secs, related):
    table = Table(
        title=f"\n[bright_cyan][link=https://www.etymonline.com/word/{word}]{word} | Online Etymology Dictionary[/link][/bright_cyan]",
        show_header=False,
        box=box.SQUARE,
    )
    table.add_column()
    for ix, sec in enumerate(secs):
        title = sec.find(["h1", "h2", "h3"])
        if title:
            table.add_row(f"[bright_cyan]{title.text.strip()}[/bright_cyan]")
        else:
            table.add_row("[bright_cyan][No title found][/bright_cyan]")

        pb = sec.find_all(["p", "blockquote"])
        for jx, j in enumerate(pb):
            newline = "" if ix == len(secs) - 1 and jx == len(pb) - 1 else "\n"
            if j.name == "blockquote":
                table.add_row(f">[italic grey82]{j.text.strip()}[/italic grey82]{newline}")
            elif j.name == "p" and j.text.strip() != "":
                table.add_row(j.text.strip() + newline)

    if related:
        related_items = [li.text.strip() for li in related.find_all("li")]
        if related_items:
            table.add_row(f"\n[bright_cyan]Entries related to [italic]{word}[/italic]:[/bright_cyan]")
            table.add_row("[wheat4]" + ", ".join(related_items) + "[/wheat4]")

    rprint(table)


# UPDATED trending words function
def o_trend():
    # Fetch a known word page (e.g., 'test') because trending sidebar is there
    soup = req("word/", "test")
    ul = soup.find("ul", class_="list-none list-none grid grid-cols-1")
    if not ul:
        rprint("[italic red]Could not find trending words list on the page.[/italic red]")
        return
    words = [a.get_text().strip() for a in ul.find_all("a", title=True)]
    rprint("[bright_cyan]Trending Words:[/bright_cyan]")
    rprint(", ".join(words))


# fuzzy search
def o_fuzzy(word):
    r = requests.get(f"https://www.etymonline.com/api/etymology/fuzzy?key={quote(word)}", headers=HEADERS)
    if r.status_code != 200:
        rprint("[italic red]Fuzzy search failed.[/italic red]")
        return
    j = json.loads(r.text)
    rprint("[wheat4]" + ", ".join(j) + "[/wheat4]")


def main(word, p, t, f):
    if t:
        o_trend()
    elif f:
        o_fuzzy(word)
    else:
        soup = req("word/", word)
        secs = soup.find_all("section", class_="prose-lg")
        related = soup.select_one("ul.list-none.flex.gap-2.flex-wrap")
        if p:
            o_plain(secs)
        else:
            o_rich(word, secs, related)
