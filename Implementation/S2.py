#!/usr/bin/env python
# -*- coding: utf-8 -*-
# L2 Recognize request for response
# This function runs the L2 facial expression
# experiment

###############################################

# import some libraries from PsychoPy
from psychopy import visual, core, event
from psychopy import gui
from PyQt4.QtCore import QPoint
# import python libraries
import sounddevice as sd
import numpy as np
import soundfile as sf
import socket
import random as rand
import codecs
import json
from playsound import playsound
#from psychopy import prefs
#prefs.general['audioLib'] = ['sounddevice','pygame','pyo']
#prefs.general['audioDrive'] = ['coreaudio','portaudio']
import S2_trial_texts #TODO# Fix so that this can be in the Text/L2 folder
import S2_trial

# If pretest is run, we would like to run two sets of set trial orders. Put pretest_order to 1 or 2

def run_S2(data_path, laptop = 1, pretest = 0, pretest_order = 1):


    print "Running L2  prosody experiment"
    print ""
    if laptop:
        print "Running on a laptop:",
    
    
    # Debugging switch:
    waiting_time = 1
    #waiting_time = 0.01
    waiting_time_2 = 2

    # Create a window
    # Laptop screen
    # fullscreen mode: When fullscreen mode is chosen, psychopy will alert
    # if the monitor size is not given as the window pixel size (first argument).
    # The problem with the fullscreen mode is that it it hiding dialog boxes.
    # If we close the window and show the dialog box, there will be no background
    # drawn and the desktop of the computer will be shown. Since this is even worse
    # we will skip fullscreen.
    if laptop:
        win = visual.Window([1440,900], color = (1,1,1), monitor="testMonitor", units="pix") #, fullscr = True)
    # Large screen:
    else:
        win = visual.Window([1800,1000], color = (1,1,1), monitor="testMonitor", units="pix")
    
    ####################################
    # Welcome and retrieve user info   #
    ####################################
    
    text_stim = visual.TextStim(win, height = 50, wrapWidth = 5000)
    text_stim.pos = (0,0)
    text_stim.color = "black"
    text_stim.bold = True



    # Input user info:
    # The pos argument must be given
    # input_box = gui.Dlg(title="", labelButtonOK="OK", labelButtonCancel="Avbryt", pos=QPoint(800,500))
    input_box = gui.Dlg(title="", labelButtonOK="OK", labelButtonCancel="Avbryt", pos=(800,500))
    input_box.addField(u'Ange subject ID')
    input_data = input_box.show()
   
    if not input_box.OK:
        print "User name not entered, quitting test"
        return
    else:
        participant_ID = input_data[0].replace(" ", "_")
        print 'p ID'
        print type(participant_ID)
        print repr(participant_ID)
        print unicode(participant_ID).encode('utf8')


    ####################################
    # Instructions and test trial      #
    ####################################

    # Instructions
    text_stim_instr = visual.TextStim(win, height = 25, wrapWidth = 1000, font="Times")
    text_stim_instr.pos = (0,0)
    text_stim_instr.color = "black"


    text_stim_instr.setText(u'Här kommer ett exempel (som inte ingår i det riktiga testet)!')

    text_stim_instr.draw()
    win.flip()
    core.wait(waiting_time*5)

   #================================

    S2_trial.S2_instruction_trial(win, data_path)

   #================================

    win.flip()

    input_box = gui.Dlg(title="", labelButtonOK = "Starta testet", labelButtonCancel = "Avbryt", pos = (900,800))
    input_box.addText(u'Tryck "Starta testet" för att starta det riktiga testet')
    input_box.show()
    if not input_box.OK:
        return

    text_stim_instr.setText(u'Nu börjar det riktiga testet!')
    text_stim_instr.draw()
    
    win.flip()
    core.wait(waiting_time*5)

    ##########################
    # Prepare the trials  #
    #########################

    n_trials = 24
    # n_trials = 3
    trials = range(0,n_trials)
    
    # Retrieve trial texts from python file
    texts = S2_trial_texts.texts

    # Randomize which trials will have test and which control.
    # 1 is test and 0 is control
    test_or_control = y = [1] * 12 + [0] * 12
    rand.shuffle(test_or_control)

    # If pretest, two different orders should be used.
    if pretest:
        test_or_control = [1,1,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0]
        if pretest_order == 2:
            # Invert order:
            test_or_control = [(i -1) * -1 for i in test_or_control]


    ###################################################
    # Prepare for storing test input from participant #
    ###################################################

    # Input_data_file:
    input_data_pretest_ratings_file_name = "S2_pretest_ratings_" + participant_ID + ".json"
    input_data_pretest_ratings_file = data_path +  input_data_pretest_ratings_file_name
    input_data_pretest_freetext_file_name = "S2_pretest_freetext_" + participant_ID + ".json"
    input_data_pretest_freetext_file = data_path +  input_data_pretest_freetext_file_name

    # Formats:

    # Test input from participant is saved as S2_recording_<trial_nr>_test_trial.wav or
    # S2_recording_<trial_nr>_control_trial.wav

    # user_input_pretest_ratings =  [{'certainty': 5, 0, 'difficulty': 0}, {'certainty': 3, 'difficulty': 0}...
    # user_input_pretest_freetext = [u'Bla bla bla', u'Blo blo blo', ...]}

    #The index of the trials list is the trial index (trial number - 1)

    # Trial info and user input.
    user_input_pretest_ratings = n_trials * [-1]
    user_input_pretest_freetext = n_trials * [-1]


    #############################################################################################################


    #############################
    # Test loop over trials
    #############################


    for trial_ind in trials:
        
        trial_nr = trial_ind + 1
        
        print "trial nr ", trial_nr
        
        trial_type = test_or_control[trial_ind]

        trial_nr_text = u'Försök ' + str(trial_nr)
        text_stim.setText(trial_nr_text)
        text_stim.bold = True

        text_stim.draw()

        win.flip()
        core.wait(waiting_time*2)

        # Trial text to show
        text = texts[trial_ind]

        #================================

        S2_trial.S2_test_trial(win, text, data_path, trial_type, trial_nr, participant_ID, request_user_input = 1)

        #================================

        if pretest:
            
            # 2 questions with rating options
            questions =  [u'Hur lätt var det att låta tydlig i om du ville ha respons eller inte?', u'Hur lätt var det att låta naturlig?']
            
            user_input_certainty = ""
            user_input_difficulty = ""
            
            scales = ['difficulty', 'certainty']

            for (i,scale) in zip([0,1],scales):
               
                text_stim_q = visual.TextStim(win, height = 35, wrapWidth = 1000)
                text_stim_q.color = "black"
                text_stim_q.pos = (0,0)
                text_stim_q.setText(questions[i])
                
                text_stim_p = visual.TextStim(win, height = 25, wrapWidth = 1000)
                text_stim_p.pos = (0,-100)
                text_stim_p.color = "black"
                text_stim_p.setText("Skriv in en siffra 1 - 5 och tryck sedan ENTER")
                if scale == 'certainty':
                    ratingScale = visual.RatingScale(win, low=1, high=5, scale = None,  labels=[u"1 = Mycket svårt", u"5 = Mycket lätt"])
                else:
                    ratingScale = visual.RatingScale(win, low=1, high=5, scale = None,  labels=[u"1 = Mycket svårt", u"5 = Mycket lätt"])
                
                while ratingScale.noResponse:
                    text_stim_q.draw()
                    text_stim_p.draw()
                    ratingScale.draw()
                    win.flip()
                
                rating = ratingScale.getRating()
                if scale == 'certainty':
                    user_input_certainty = rating
                else:
                    user_input_difficulty = rating

                #decisionTime = ratingScale.getRT()
                #choiceHistory = ratingScale.getHistory()
                
            ######################
            # Save user input    #
            ######################
                
                user_input_pretest_ratings[trial_ind] = {'user_input_certainty': user_input_certainty, 'user_input_difficulty': user_input_difficulty}

    #################################################################################################################################################

    ##############################
    # Write user input to file   #
    ##############################
    
    f = open(input_data_pretest_ratings_file, 'wb+')
    json.dump(user_input_pretest_ratings, f)
    f.close()
    

    #########################################
    # Communicate that the test is over    #
    #########################################

    text = u"Nu är testet klart!"
    text_stim_instr.setText(text)
        
    # Draw the text
    text_stim_instr.draw()
    win.flip()
    # Hold the image
    core.wait(waiting_time_2*2)

    #################################################################################################################################################
        

    #If pretest: another loop with the trials followed by a questionnaire where they can write freely.
    
    if pretest:
        
        # Pretest instructions
        text = u"Nu kommer alla försöken igen och efter varje försök kommer du att få fylla i vad du tyckte om dem."
        text_stim_instr.setText(text)
        
        text_stim_instr.draw()
        win.flip()
        core.wait(waiting_time_2*2)
        
        input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
        input_box.show()
        if not input_box.OK:
            return
    
        #############################
        # Pretest loop over trials
        #############################
        
        for trial_ind in trials:
            
            trial_nr = trial_ind + 1
            
            trial_type = test_or_control[trial_ind]
            
            # Trial texts
            text = texts[trial_ind]
            
            #================================
            
            S2_trial.S2_test_trial(win, text, data_path, trial_type, trial_nr, participant_ID, request_user_input = 0)
            
            #================================
            
            win.flip()
            
            #input_box = gui.Dlg(title="", pos = QPoint(800,500))
            input_box = gui.Dlg(title="", pos = (800,500))
            input_box.addField(u'Hur gick dina tankar kring detta försök?  (byt "å","ä" och "ö" mot "a" och "o")')
            user_input = input_box.show()
            
            if input_box.OK:
                user_input = user_input[0]
            else:
                user_input = ""
            
            ######################
            # Save user input    #
            ######################

            # Save user input
            user_input_pretest_freetext[trial_ind] = user_input

        ##############################
        # Write user input to file   #
        ##############################

        f = open(input_data_pretest_freetext_file, 'wb+')
        json.dump(user_input_pretest_freetext, f)
        f.close()

    #################################################################################################################################################


    text = u"Tack för att du deltog!"
    text_stim_instr.setText(text)

    
    text_stim_instr.draw()
    win.flip()
    # Hold the image
    core.wait(waiting_time_2)
    win.close()

    # Cleanup
    core.quit()




