import json
import sys

root_object = {"perturbed": {}, "unperturbed": {}}
variables = map(lambda e: [e[0], int(e[1])], map(lambda e: e.split("; "), map(str.strip, sys.stdin.readlines())))

for variable in variables:
    if variable[1] > 100 or variable[1] < -20:
        root_object["unperturbed"][variable[0]] = variable[1]
    else:
        root_object["perturbed"][variable[0]] = variable[1]

f = open("curvature.json", "w")
json.dump(root_object, f)
f.close()
