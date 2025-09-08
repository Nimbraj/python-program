import pickle
import os

print("Current working directory:", os.getcwd())

# Pickling (writing object to file)
with open("dumps.pkl", "wb") as file:  # fixed filename (no space)
    pickle.dump(["abc", "xyz", "jagtap", 123, 12232], file)

# Unpickling (reading object back from file)
with open("dumps.pkl", "rb") as file:
    data = pickle.load(file)
    print("Unpickled Data:", data)
