from pathlib import Path
import pandas as pd

# Get CVS file
csv_path = Path("data/adsb.csv")
df = pd.read_csv(csv_path)

'''
time_position: when the aircraft position was last updated
last_contact: when the signal was last received
'''
# Use "last_contact" for the time column if "time_position" is unavalible 
time_col = "time_position" if "time_position" in df.columns else "last_contact"
df["time"] = pd.to_datetime(df[time_col], unit="s", utc=True)

# Rename "true_track" column to be "heading" 
df = df.rename(columns={"true_track": "heading"})

# Keep only the following columns 
'''
icao24: aircraft identifier
latitude: latitude
longitude: longitude
baro_altitude: barometric altitude
velocity: velocity
heading: heading
vertical_rate: rate of climb
time: time of the aircrafts state (UTC)
'''
keep = [
    "icao24",
    "latitude",
    "longitude",
    "baro_altitude",
    "velocity",
    "heading",
    "vertical_rate",
    "time",
]
df = df[keep]

# Drop rows missing essential columns 
df = df.dropna(subset=["icao24", "latitude", "longitude", "baro_altitude", "velocity", "heading"])

# Convert units to aviation units
df["alt_ft"] = df["baro_altitude"] * 3.28084      # m -> ft
df["gs_kt"]  = df["velocity"] * 1.94384           # m/s -> knots
df["vs_fpm"] = df["vertical_rate"] * 196.85       # m/s -> ft/min (vertical_rate may contain NaN)

# Inspect table (first 5 rows)
print("\nTime range:", df["time"].min(), "→", df["time"].max())
print("\nColumns now:", list(df.columns))
print("\nFirst 5 rows:\n", df.head())
