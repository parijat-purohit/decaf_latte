import json
from collections import Counter, defaultdict

# Load the JSON array (list of dicts)
with open("Deep-ML/data.json", "r", encoding="utf-8") as f:
    records = json.load(f)

age_job_mapping = defaultdict(list)

for entry in records:
    age = entry["age"]
    marital = entry["marital"]
    age_job_mapping[age].append(marital)

print("Age\tMarital Status Statistics")
for age, data in sorted(age_job_mapping.items()):
    print(age, '\t', dict(Counter(data)))
