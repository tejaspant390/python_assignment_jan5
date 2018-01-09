def dispmsg(name):
    print("Hello",name," Have a good day.")


name = str(input("Enter your name: "))

if name == "":
    raise Exception("INVALID !!! YOU MUST HAVE A NAME")
else:
    dispmsg(name)