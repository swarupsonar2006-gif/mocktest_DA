# Practical 5: Exploratory Data Analysis

## Aim

To perform exploratory data analysis on sales data, examining data quality, distributions, outliers, correlations, group differences, and trends.

## What the scripts do

- Generate reproducible sample sales data when no input file is configured.
- Inspect the data shape, columns, data types, missing values, and duplicate rows.
- Calculate descriptive statistics and categorical frequency counts.
- Visualize the sales distribution and identify outliers.
- Calculate numeric correlations and compare sales across regions.
- Examine sales trends over time.
- Save charts such as `step5_distribution.png`, `step7_correlation.png`, `step8_groups.png`, and `step9_trend.png`.

## Requirements

- Python 3
- NumPy
- pandas
- Matplotlib
- Seaborn

Install the dependencies if needed:

```powershell
python -m pip install numpy pandas matplotlib seaborn
```

## Run

From this folder, run any of the numbered scripts:

```powershell
python .\1.py
```

Replace `1.py` with `2.py` or `3.py` to run another copy. To analyze a file instead of generated sample data, set `FILE_PATH` near the top of the script to a CSV or Excel file path.
