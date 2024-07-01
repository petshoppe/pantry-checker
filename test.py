print("welcome to list maker")
print(
    "im gonna need a list of your favorite bands,\
    followed by the genre that they are."
)
print("when youre done, type 'done'")
done = False
bandlist = []
while done is False:
    band = input("give me a band name")
    if band == "done":
        done = True
    elif band != "done":
        genre = input("what is their genre?")
        bandlist.append([band, genre])
        print("ok how about the next one?")
print(bandlist)

