import os

with os.scandir('img') as directory:
    for file in directory:
        if file.name[-6:] == "mcmeta":
            os.remove(f"img/{file.name}")
            os.remove(f"img/{file.name[:-7]}")
