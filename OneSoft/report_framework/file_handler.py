def read_data_from_file(filename: str):
    """Read data from race files"""
    data = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                data.append(line)
    return data
