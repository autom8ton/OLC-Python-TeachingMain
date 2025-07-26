# Conversion factors to bytes
conversion_factors = {
    'B': 1,
    'kB': 1000,
    'MB': 1000**2,
    'GB': 1000**3,
    'TB': 1000**4,
    'PB': 1000**5,
    'KiB': 1024,
    'MiB': 1024**2,
    'GiB': 1024**3,
    'TiB': 1024**4,
    'PiB': 1024**5,
}

def convert_storage(value, from_unit, to_unit):
    from_unit = from_unit.strip()
    to_unit = to_unit.strip()
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        print("Unsupported unit. Please use B, kB, MB, GB, TB, KiB, MiB, GiB, TiB.")
        return -1
    
    # Convert source to bytes
    bytes_value = value * conversion_factors[from_unit]
    # Convert bytes to target unit
    converted_value = bytes_value / conversion_factors[to_unit]
    
    return converted_value

# Example: Convert 10 MB to MiB
result = convert_storage(10, 'MB', 'MiB')
print(f"10 MB is approximately {result:.4f} MiB")
