import json
import numpy as np

npy_file_path = 'fellows.npy'
json_file_path = 'fellows.json'

loaded_data = np.load(npy_file_path, allow_pickle=True).item()

with open(json_file_path, 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print("JSON file saved successfully.")