import instances
import files_lib
import grid_lib

import random

instances.parse_tsv_bin_desc("example_input_bin.tsv", "example_output_bin.desc", ["buffalo", "cow"], "species", "cow")

data = instances.parse_tsv_bin("example_input_bin.tsv")

data = grid_lib.uniformize(data, 'B', 0, "buffalo")
data = grid_lib.uniformize(data, 'C', 0, "cow")

random.shuffle(data)

remains = files_lib.write_training(data, "example_output_bin.training")
files_lib.write_test(remains, "example_output_bin.test")