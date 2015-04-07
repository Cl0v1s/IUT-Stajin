# -*- coding: utf-8 -*-
import csv

def getData(file):
    csv_file = open(file, encoding="latin-1")
    entry = list(csv.reader(csv_file, delimiter = ";"))
    csv_file.close()
    return entry

def purify(entry):
    l = []
    for e in entry:
        v = ""
        v = e.replace("'","&apos;").replace('"', "&quot;")
        l.append(v)
    return l
