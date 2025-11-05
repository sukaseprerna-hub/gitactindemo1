import requests
import pandas as pd

# Extract: Read data from a public API
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

# Transform: Convert to DataFrame and select key fields
df = pd.DataFrame(data)
df = df[["id", "name", "email", "company"]]
df["company"] = df["company"].apply(lambda x: x["name"])

# Load: Display transformed result
print("Transformed User Data:")
print(df)
