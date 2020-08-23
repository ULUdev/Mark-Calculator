#!/usr/bin/python
import json
import sys
import argparse
with open("../data/cfg.json") as file:
    cfg = json.load(file)
with open("../data/inf.json") as file:
    inf = json.load(file)
parser = argparse.ArgumentParser(description="your best mark system interface")
parser.add_argument("subject", nargs="?", type=str, help="subject")
parser.add_argument("--mark", nargs="?", type=int, help="mark")
parser.add_argument("--marks", help="show marks of a specific subject")
parser.add_argument("--newsubject", help="New Subject")
parser.add_argument("--info", help="info about the project")
args = parser.parse_args()

def main():
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
    elif args.info != None:
        if args.info not in inf:
            print("Not a property of the programm")
        else:
            print(inf[args.info])
if __name__ == "__main__":
    main()