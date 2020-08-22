#!/usr/bin/python
import json
import sys
import argparse
with open("../data/cfg.json") as file:
    cfg = json.load(file)
def new_subject():
    if args.subject in cfg:
        print("subject exists")
    else:
        cfg[name] = []
def marks():
    pass
parser = argparse.ArgumentParser(description="your best mark system interface")
parser.add_argument("subject", nargs="?", type=str, help="subject")
parser.add_argument("--mark", nargs="?", type=int, help="mark")
parser.add_argument("--marks", help="show marks of a specific subject")
parser.add_argument("--newsubject", help="New Subject")
args = parser.parse_args()

if __name__ == "__main__":
    print(args.marks)
    if args.mark != None:
        if args.subject not in cfg:
            print("subject doesn't exist")
        else:
            cfg[args.subject].append(args.mark)
            with open("../data/cfg.json", "w") as file:
                file.write(json.dumps(cfg, indent=4))
    elif args.marks != None:
        if args.marks == "all":
            if args.subject not in cfg:
                print("invalid subject")
            else:
                print(cfg[args.subject])
    elif args.newsubject != None:
        cfg[args.subject] = []
        with open("../data/cfg.json", "w") as file:
            file.write(json.dumps(cfg, indent=4))