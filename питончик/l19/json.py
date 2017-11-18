import json

content = {}
content["log"] = "Aslan_lion"
content["pass"] = "12345"

f = open("database2.txt","a")

json.dump(content, f)
f.close()
f = open("database2.txt","r")
jObj = json.load(f)
print(jObj["log"])
f.close()


