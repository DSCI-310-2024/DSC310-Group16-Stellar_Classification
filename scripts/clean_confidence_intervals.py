def clean_confidence_intervals(exoplanet_data):
    return exoplanet_data.apply(
        lambda col: col.str.split("&").str[0] if col.dtype == "object" else col
    )
