import json
import sys
print("Welcome to mark manager")
print("type in a command:")
with open("data/cfg.json") as file:
    cfg = json.load(file)
if __name__ == "__main__":
    cmd = input("")
    if cmd == "marks":
        print("please give us more information")
    elif cmd.startswith("addsubject "):
        subject = cmd.split(" ")[1]
        cfg[subject] = []
        print(f"subject {subject} added")
    elif cmd == "quit" or cmd == "\q":
        print("bye")
        sys.exit()
    elif cmd.startswith("addmark "):
        if "-s " in cmd:
            subject = cmd.split("-s ")[1]
            newsubject = ""
            for i in subject:
                if i == " ":
                    break
                else:
                    newsubject += i
            if newsubject not in cfg:
                print(f"the subject {newsubject} doesn't exist")
            else:
                subject = newsubject
        if "-m" in cmd:
            mark = cmd.split("-m ")[1]
        if " " in mark:
            mark = mark.split(" ")[0]
        cfg[subject].append(mark)
        with open("data/cfg.json", "w") as file:
            file.write(json.dumps(cfg, indent=4)