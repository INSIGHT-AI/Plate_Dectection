import easyocr


def extract_plate_no(filename):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename)
    print(result)
    return result

if __name__ == "__main__":
    extract_plate_no('Numberplate.jpg')