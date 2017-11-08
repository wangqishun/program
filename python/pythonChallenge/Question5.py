import requests
import re

rec = re.compile("and the next nothing is (\d+)")
num = "8022"
while True:
    req = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + num)
    print(num)
    match = rec.search(req.text)
    if match:
        num = match.group(1)
    else:
        break

print(req.text)
#peak.html