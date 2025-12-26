from pathlib import Path
import kagglehub    # For data            
import shutil       


# Get Data folder path. If DNE make it. 
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Download OpenSKy dataset using the Kaggle API
download_path = Path(
    kagglehub.dataset_download("ibrahimqasimi/opensky")
)

# Find CSV files in the downloaded dataset
csv_files = list(download_path.glob("*.csv"))

if not csv_files:
    raise RuntimeError("No CSV files found in the downloaded dataset")

# Take the first CSV and copy it into the data folder
source_csv = csv_files[0]
target_csv = DATA_DIR / "adsb.csv"
shutil.copy(source_csv, target_csv)

