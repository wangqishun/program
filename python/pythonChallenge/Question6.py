import pickle
import requests

url = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
pk = pickle.loads(bytes(url.text, encoding="utf8"))
for j in pk:
	print("".join([i[1] * i[0] for i in j]))