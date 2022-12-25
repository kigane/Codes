import json

import yaml

with open('base/garbage_classification.json', 'r') as p:
    classes = json.load(p)

print(classes)
with open('base/z.yml', 'w') as f:
    yaml.dump(classes, f)
