import frontend as front

text = ""
def pressed(instance):
    print(front.Grid().input.text)
def textchanged(instance, value):
    text = value
if __name__ == "__main__":
    front.app().run()