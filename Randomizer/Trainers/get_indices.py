import json

trainer_file = open('trdata_array_clean.json', 'r')
trainer = json.load(trainer_file)
trainer_file.close()

for entry in trainer['values']:
    if "_dlc1"