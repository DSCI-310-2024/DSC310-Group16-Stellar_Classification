

def clean_confidence_intervals(exoplanet_data):
    """
    Removes confidence intervals, keeping only the mean value.
    """
    return exoplanet_data.apply(lambda col: col.str.split("&").str[0] if col.dtype == "object" else col)

def rename_columns(exoplanet_data):
    """
    Renames columns by removing 'str' from the end of column names.
    """
    for col in exoplanet_data.columns:
        if col.endswith("str"):
            return exoplanet_data.rename(columns={col: col[:-3]})

def filter_and_categorize_spectral_types(exoplanet_data):
    """
    Filters the data to keep only the rows where the values in the "st_spectype" column are among 
    the specified spectral types: "O", "B", "A", "F", "G", "K", or "M" and converts spectral type 
    column to category type.
    """
    # Filters rows by spectral type 
    exoplanet_data = exoplanet_data.loc[exoplanet_data["st_spectype"].isin(["O", "B", "A", "F", "G", "K", "M"])]
    # Converts spectral type column to category type
    exoplanet_data["st_spectype"] = exoplanet_data["st_spectype"].astype("category")
    return exoplanet_data