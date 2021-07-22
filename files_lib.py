import csv

def import_tsv(filename):
    """Parses a .tsv file into an array of arrays
    :param filename : the name of the file to parse
    :return : an array of arrays with the contents of the file
    """
    csv = open(filename)
    print("Loading file " + filename)
    text_csv = csv.read()
    tmp_array = text_csv.split('\n')
    array = []
    for line in tmp_array:
        array.append(line.split('\t'))
    csv.close()
    return array


def import_csv(filename):
    """Parses a .csv file into an array of arrays
    :param filename : the name of the file to parse
    :return : an array of arrays with the contents of the file
    """
    csv = open(filename)
    print("Loading file " + filename)
    text_csv = csv.read()
    tmp_array = text_csv.split('\n')
    array = []
    for line in tmp_array:
        array.append(line.split(','))
    csv.close()
    return array


def write_csv(arrays, filename):
    """Writes an array of arrays into a .csv file
    :param arrays : the array of arrays containing the information to write
    :param filename : the name of the file to create or overwrite, extension included
    :return : void
    """
    try:
        csvfile = open(filename, 'w' ,newline='')
    except FileNotFoundError:
        csvfile = open(filename, 'x' ,newline='')
    res_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
    for array in arrays:
        row = []
        for element in array:
            row.append(element)
        res_writer.writerow(row)
    csvfile.close()


def write_training(data, file_name):
    """Writes a .training file with two third of data
    :param data : an array of arrays
    :param file_name : what to name the .training file (extension included)
    :return : the remaining data
    """
    try:
        training = open(file_name, "x")
    except FileExistsError:
        training = open(file_name, "w")
    length = len(data) * 2 // 3
    training.write("Nb Individuals: " + str(length) + "\n")
    for h in range(length):
        line = data[h]
        training.write('{')
        for i in range(len(line)):
            if i > 0:
                training.write(',')
            training.write(str(i) + " " + str(line[i]))
        training.write("}\n")

    remain = data[length:]
    training.close()
    return remain


def write_test(data, file_name):
    """Writes a .test file with the one remaining third of data
    WARNING: To use AFTER write_training
    :param data : an array of arrays
    :param file_name : what to name the .test file (extension included)
    :return : void
    """
    try:
        test = open(file_name, "x")
    except FileExistsError:
        test = open(file_name, "w")
    test.write("Nb Individuals: " + str(len(data)) + "\n")
    for h in range(len(data)):
        line = data[h]
        test.write('{')
        for i in range(len(line)):
            if i > 0:
                test.write(',')
            test.write(str(i) + " " + str(line[i]))
        test.write("}\n")

    test.close()