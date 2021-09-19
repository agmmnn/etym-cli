# -*- coding: utf-8 -*-
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import json

from rich.table import Table
from rich import box
from rich import print as rprint


def req(page, word):
    url = "https://www.etymonline.com/" + page + quote(word)
    r = requests.get(url)
    if r.status_code == 404:
        rprint("[italic]Word not found.[/italic]")
        exit()
    return BeautifulSoup(r.content, "lxml")


# plane text output
def o_plain(secs):
    print()
    for ix, i in enumerate(secs):
        print(i.find(class_="word__name--TTbAA").text)
        newline = "\n" if ix != len(secs) - 1 else ""
        for j in i.section.find_all(["p", "blockquote"]):
            if j.name == "blockquote":
                print(">>" + j.text)
            elif j.name == "p" and j.text != "":
                print(j.text + newline)
    print()


# rich output
def o_rich(word, secs, related):
    table = Table(
        title="\n[bright_cyan][link=https://www.etymonline.com/word/{}]{} | Online Etymology Dictionary[/link][/bright_cyan]".format(
            word, word
        ),
        show_header=False,
        box=box.SQUARE,
    )
    table.add_column()
    for ix, i in enumerate(secs):
        table.add_row(
            "[bright_cyan]" + i.find(class_="word__name--TTbAA").text + "[/bright_cyan]"
        )
        pb = i.section.find_all(["p", "blockquote"])
        for jx, j in enumerate(pb):
            newline = "" if ix == len(secs) - 1 and jx == len(pb) - 1 else "\n"
            # print(ix, jx, len(secs) - 1, len(pb) - 1)
            if j.name == "blockquote":
                table.add_row(
                    ">[italic grey82]" + j.text + "[/italic grey82]" + newline
                )
            elif j.name == "p" and j.text != "":
                table.add_row(j.text + newline)
    if related != None:
        table.add_row(
            "\n[bright_cyan]Entries related to [italic]"
            + word
            + "[/italic]:[/bright_cyan]"
        )
        related.find_all("dfg", {"class": None})
        r_lst = []
        for i in related:
            r_lst.append(i.text)
        table.add_row("[wheat4]" + ", ".join(r_lst) + "[/wheat4]")

    rprint(table)


# returns trending words
def o_trend():
    soup = req("search?q=", "z")
    t_lst = [
        i.text for i in soup.find("div", {"trending__normal--2eWJF"}).find_all("li")
    ]
    rprint("[bright_cyan]Trending Words:[/bright_cyan]")
    rprint(", ".join(t_lst))


# returns fuzzy search results
def o_fuzzy(word):
    soup = req("api/etymology/fuzzy?key=", word)
    j = json.loads(soup.text)
    rprint("[wheat4]" + ", ".join(j) + "[/wheat4]")


def main(word, p, t, f):
    if t:
        o_trend()
    elif f:
        o_fuzzy(word)
    else:
        soup = req("word/", word)
        # find all word sections
        secs = soup.find_all("div", {"class": "word--C9UPa"})
        # find related word section
        related = soup.find("ul", {"related__container--22iKI"})
        # get output
        if p == True:
            o_plain(secs)
        else:
            o_rich(word, secs, related)
