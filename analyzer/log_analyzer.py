import json

f = open("../logger/log_test.txt", 'r', encoding="UTF-8")
line = f.readline()
i = 0
set_ids = set()
while line:
    n_f = line.index("[")
    n_y = line.index("应") + 1
    line = line.replace(line[n_f:n_y], "")
    jsonDump = json.loads(line)
    print(jsonDump["data"])
    for x in jsonDump["data"]:
        if x["status"] == '未推送':
            set_ids.add(x["ad"])
            print(x["ad"], " ", x["status"])
    line = f.readline()
f.close()
print(set_ids)
