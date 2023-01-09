def check_file(filename: str):
    """Check if file exist and has txt format"""
    try:
        with open(filename) as txt_file:
            txt_file.read()
    except FileNotFoundError as error:
        return error
    except UnicodeDecodeError:
        return 'Application works only with txt files'
    return False
