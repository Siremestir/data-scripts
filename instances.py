import random
import files_lib
import grid_lib

def parse_tsv_bin(file):
    """Parses a tsv file into an array of arrays for MOCA-I
    For binary intensities
    :param file : the tsv file to parse
    :return : an array of arrays
    """
    lines = files_lib.import_tsv(file)
    del lines[0]
    return lines


def parse_tsv_quant(file):
    """Parses a tsv file into an array of arrays for MOCA-I
    For quantitative intensities
    :param file : the tsv file to parse
    :return : an array of arrays
    """
    lines = files_lib.import_tsv(file)
    del lines[0]
    res = []

    # Normalizing to reduce the impact of age on the intensities
    norm_lines = []
    for line in lines:
        norm_line = grid_lib.normalize(line)
        norm_lines.append(norm_line)

    res = grid_lib.discretize(norm_lines, 30)

    # for i in range(len(lines)):
        
    #     if lines[i][0] == 'B':
    #         species = "boeuf"
    #     else:
    #         species = "auroch"
    #     res[i].append(species)

    print(res)
    return res


def parse_tsv_bin_desc(file, newfile, qual_poss, target_attr, target):
    """Parses a tsv file into a .desc file for MOCA-I
    For binary intensities
    WARNING: This function assumes there is a qualitative attribute at the
    beginning of each row, and it will be the one targeted.
    :param file : the tsv file to parse
    :param newfile : the file to create or overwrite
    :param qual_poss : a list of all possible values for the qualitative attribute
    :param target_attr : the name of the qualitative attribute (i.e "species")
    :param target : which specific attribute to predict for (i.e "buffalo")
    :return : void
    """
    content = files_lib.import_tsv(file)
    attributes = content[0]
    del attributes[0]

    try:
        desc = open(newfile, "x")
    except FileExistsError:
        desc = open(newfile, "w")
    
    first_line = "@attribute " + target_attr + " {" + qual_poss[0]
    del qual_poss[0]
    for poss in qual_poss:
        first_line = first_line + "," + poss

    first_line += "}\n"
    desc.write(first_line)

    for attribute in attributes:
        desc.write("@attribute " + attribute + " {0,1}\n")
    
    desc.write("@prediction " + target_attr + " = " + target)


def parse_tsv_quant_desc(file, newfile, qual_poss, target_attr, target):
    """Parses a tsv file into a .desc file for MOCA-I
    For quantitative intensities
    WARNING: This function assumes there is a qualitative attribute at the
    beginning of each row, and it will be the one targeted.
    :param file : the tsv file to parse
    :param newfile : the file to create or overwrite
    :param qual_poss : a list of all possible values for the qualitative attribute
    :param target_attr : the name of the qualitative attribute (i.e "species")
    :param target : which specific attribute to predict for (i.e "buffalo")
    :return : void
    """
    content = files_lib.import_tsv(file)
    attributes = content[0].copy()
    del attributes[0]
    arr_intensities = content[1:].copy()

    try:
        desc = open(newfile, "x")
    except FileExistsError:
        desc = open(newfile, "w")

    first_line = "@attribute " + target_attr + " {" + qual_poss[0]
    del qual_poss[0]
    for poss in qual_poss:
        first_line = first_line + "," + poss

    first_line += "}\n"
    desc.write(first_line)

    norm_lines = []

    for intensities in arr_intensities:
        norm_lines.append(grid_lib.normalize(intensities))

    for norm_line in norm_lines:
        del norm_line[0]

    intervals = grid_lib.make_intervals(norm_lines, 3)
    for attribute in attributes:
        attr_line = "@attribute " + attribute + " <{" + intervals[0]
        for i in range(1,len(intervals)):
            attr_line = attr_line + "," + intervals[i]
        attr_line += "}\n"

        desc.write(attr_line)
    
    desc.write("@prediction " + target_attr + " = " + target)


# data = parse_tsv_bin("feature_matrix_without_intensities.tsv")
# # print(data)
# random.shuffle(data)
# # remain = write_training(data, "test.training")
# # write_test(remain, "mh-builder/instances/rulemining/ft_icr/ft_icr.1.test")
# remain = files_lib.write_training(data, "mh-builder/instances/rulemining/ft_icr/ft_icr.1.training")
# files_lib.write_test(remain, "mh-builder/instances/rulemining/ft_icr/ft_icr.1.test")
