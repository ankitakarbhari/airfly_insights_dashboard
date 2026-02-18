import pandas as pd

df = pd.read_csv("data/raw/Airline Dataset Updated - v2.csv")

print("Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

# samplig
df_sample = df.sample(frac=0.3, random_state=42)

# memory optimization
df['origin'] = df['origin'].astype('category')
df['destination'] = df['destination'].astype('category')

# Handale Null Vlaue
df['dep_delay'] = df['dep_delay'].fillna(0)
df['arr_delay'] = df['arr_delay'].fillna(0)
df = df.dropna(subset=['flight_date'])

# convert date_time
df['flight_date'] = pd.to_datetime(df['flight_date'], errors='coerce')
df = df.dropna(subset=['flight_date'])

#create features
df['month'] = df['flight_date'].dt.month
df['day_of_week'] = df['flight_date'].dt.dayofweek
df['hour'] = df['flight_date'].dt.hour
# df['route'] = df['origin'] + "-" + df['destination']

# saved cleaned dataset
df.to_csv("data/processed/airline_cleaned.csv", index=False)

print("Preprocessing Completed")