import pandas as pd

cardiovascularData = pd.read_csv(
    r"C:\Users\james\Downloads\comp sci work\JamesCook24-Jack-CW\cardio_train.csv",
    delimiter=";"
)

print(cardiovascularData.describe())
print("length:", len(cardiovascularData))

rules = {
    "age": (9125, 27375),   # days (25–75 years)
    "height": (100, 228),   # cm
    "weight": (39.9, 225),  # kg
    "ap_hi": (70, 175),     # systolic mm Hg
    "ap_lo": (50, 110)      # diastolic mm Hg
}

def cleaningData(ds, rules):
    cleaning = ds.copy()

    # Apply simple range rules
    for col, (min_val, max_val) in rules.items():
        cleaning = cleaning[(cleaning[col] >= min_val) & (cleaning[col] <= max_val)]

    # BMI-style rule (height in cm → m)
    h_m = cleaning["height"] / 100
    w = cleaning["weight"]
    bmi_condition = (w / 10 >= h_m**2) & (w / 75 <= h_m**2)
    cleaning = cleaning[bmi_condition]

    # Blood pressure consistency
    ap_hi = cleaning["ap_hi"]
    ap_lo = cleaning["ap_lo"]
    diff = ap_hi - ap_lo

    bp_condition = (ap_hi > ap_lo) & (diff <= 90)
    cleaning = cleaning[bp_condition]

    return cleaning


cleanData = cleaningData(cardiovascularData, rules)
cleanData = cleanData.drop_duplicates()

print(cleanData.describe())
print("length:", len(cleanData))

cleanData.to_csv('cleaned_cardio_train3.csv', index=False)
