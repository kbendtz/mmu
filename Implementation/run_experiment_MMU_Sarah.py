# -*- coding: utf-8 -*-
import socket

# Main script for running the MMU experiment
# Calling separate functions for each experiment
# block.

#########################################################################

# Import the experiment functions (from file_name import function_name)
# from file import function
from L2_facial_exp import run_L2_facial_exp
from L2_prosody import run_L2_prosody
from S2 import run_S2
#from S1_facial_exp import run_S1_facial_exp
from S1_prosody import run_S1_prosody

# Paths
# Sarah: Check your personal paths

computer = socket.gethostname()

image_path = ""
sound_path = ""
text_path = " "

print "computer: ", computer

laptop = 0

if computer == "Rasputin" or computer == "Rasputin.local" or "wlan-su-10-201-6-147.local.su.se": # or ...
    
    print "I'm on Rasputin"

    # Sound and images are saved in separate folders.
    # Text is saved in a text file.

    image_path = "/Users/sarah/MMU/Implementation/Images/"
    sound_path = "/Users/sarah/MMU/Implementation/Sound/"
    text_path = "/Users/sarah/MMU/Implementation/Text/"

    # Input data from participants

    data_path = "/Users/sarah/MMU/Implementation/Data/"

    laptop = 1
    
else:

    # Sound and images are saved in separate folders.
    # Text is saved in a text file.

    image_path = "/Users/bendtz/Dropbox/Research/CIV/MMU/Implementation/Images/"
    sound_path = "/Users/bendtz/Dropbox/Research/CIV/MMU/Implementation/Sound/"
    text_path = "/Users/bendtz/Dropbox/Research/CIV/MMU/Implementation/Text/"

    # Input data from participants

    data_path = "/Users/bendtz/Dropbox/Research/CIV/MMU/Implementation/Data/"

##############################################

# Pretest or not?
pretest = 1
# pretest = 0
# pretest_order = 1
pretest_order = 2

##############################################



image_path_L2 = image_path + "L2/"
sound_path_L2 = sound_path + "L2/"
text_file_L2 = text_path + "L2/L2_trial_texts.txt"
data_path_L2_facial_exp = data_path + "L2/Facial_exp/"
data_path_L2_prosody = data_path + "L2/Prosody/"
text_file_S2 = text_path + "S2/S2_trial_texts.txt"
data_path_S2 = data_path + "S2/"
image_path_S1 = image_path + "S1/"
sound_path_S1 = sound_path + "S1/"
text_path_S1 = text_path + "S1/"
data_path_S1_facial_exp = data_path + "S1/Facial_exp/"
data_path_S1_prosody = data_path + "S1/Prosody/"

# Functions for each block

# L2: Recognize request for response ##########

# run_L2_facial_exp(image_path_L2, data_path_L2_facial_exp, laptop, pretest, pretest_order)

# S2: Produce request for response ###########

# run_S2(data_path_S2, laptop, pretest, pretest_order)

# S1: Regognize request for clarification #####

# run_S1_prosody(sound_path_S1, data_path_S1_prosody, laptop, pretest, pretest_order)

# L2: Recognize request for response ##########

run_L2_prosody(sound_path_L2, data_path_L2_prosody, laptop, pretest, pretest_order)

#run_S1_facial_exp(pretest = 0, image_path_S2, text_path_S2, data_path_S2_facial_exp)
#



