#!/usr/bin/python
import json
import sys
import argparse
with open("data/cfg.json") as file:
    cfg = json.load(file)
def new_subject():
    if args.subject in cfg:
        print("subject exists")
    else:
        cfg[name] = []
def marks():

parser = argparse.ArgumentParser(description="your best mark system interface")
parser.add_argument("subject", nargs="?", type=str, help="subject")
parser.add_argument("--mark", nargs="?", type=int, help="mark")
parser.add_argument("--newsubject", help="New Subject")
args = parser.parse_args()

if __name__ == "__main__":
    if args.mark != "":
        pass