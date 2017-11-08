import zipfile,re

z = zipfile.ZipFile("./channel.zip")
comment_map = {}
for filename in z.namelist():
    comment_map[filename] = z.getinfo(filename).comment

comm = ""
start = "90052.txt"
rec = re.compile("nothing is (\d+)")
while True:
    text = str(z.read(start))
    match = rec.search(text)
    if match:
        start = match.group(1) + ".txt"
        comm += comment_map[start].decode()
    else:
        break

print(text)
print(comm)