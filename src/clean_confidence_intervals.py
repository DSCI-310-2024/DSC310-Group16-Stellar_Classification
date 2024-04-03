def clean_confidence_intervals(exoplanet_data):
    """
    Removes confidence intervals, keeping only the mean value.
    """
    return exoplanet_data.apply(lambda col: col.str.split("&").str[0] if col.dtype == "object" else col)