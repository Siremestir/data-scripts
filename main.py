import instances
import files_lib
import grid_lib

import random

# # Example

# instances.parse_tsv_bin_desc("example_input_bin.tsv", "example_output_bin.desc", ["buffalo", "cow"], "species", "cow")

# data = instances.parse_tsv_bin("example_input_bin.tsv")

# data = grid_lib.uniformize(data, 'B', 0, "buffalo")
# data = grid_lib.uniformize(data, 'C', 0, "cow")

# random.shuffle(data)

# remains = files_lib.write_training(data, "example_output_bin.training")
# files_lib.write_test(remains, "example_output_bin.test")

instances.parse_tsv_bin_desc("../feature_matrix_without_intensities_2_copy.tsv", "../mh-builder/instances/rulemining/ft_icr/ft_icr.5.desc", ["autruche", "oiseau_act16", "pigeon_act21", "poulet", "thon_albacore", "thon_obese", "thon_rouge", "thon", "agneau", "baleine_act1", "belette_act20", "boeuf_act3", "boeuf_act6", "boeuf_act9", "bois_daim", "campagnol_des_champs_act17", "campagnol_terrestre_act23", "cerf", "chamois", "chat_act24", "cheval", "chevreuil", "chien_act25", "daim_os_long", "daim", "homme_act2", "lapin", "lapin_act19", "marmotte_act22", "porc", "rat_noir_act18", "renard", "sanglier_act4", "sanglier_act5", "taupe_act15", "XXX"], "species", "XXX")

data = instances.parse_tsv_bin("../feature_matrix_without_intensities_2_copy.tsv")

random.shuffle(data)

remains = files_lib.write_training(data, "../mh-builder/instances/rulemining/ft_icr/ft_icr.5.training")
files_lib.write_test(remains, "../mh-builder/instances/rulemining/ft_icr/ft_icr.5.test")