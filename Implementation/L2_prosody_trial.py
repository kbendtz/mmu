#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import visual, core, event
from psychopy import gui
from playsound import playsound

def L2_prosody_test_trial(window, text, sound_path, trial_type, trial_nr, n_yes_inputs, request_user_input):
    
    waiting_time = 1

    # Trial text
    text_stim = visual.TextStim(window, height = 40, wrapWidth = 1000)
    text_stim.setText(text)
    
    text_stim.pos = (0,0)
    text_stim.color = "black"
    text_stim.bold = False
    
    text_stim.draw()
    window.flip()
    
    # Hold the text
    core.wait(waiting_time*1.5)
    
    # Trial sound
    sound_file_1_name = ""

    
    if trial_type == 1:
        sound_file_1_name = "L2_prosody_" + str(trial_nr) + "_test.aiff"
    else:
        sound_file_1_name = "L2_prosody_" + str(trial_nr) + "_control.aiff"

    # Play the sound
    playsound(sound_path + sound_file_1_name)

    if request_user_input:

        window.flip()
        # Input from user: response-seeking or not
        n_yes_inputs_left = 6 - n_yes_inputs
        n_trials_left = 12 - trial_nr
        
        text_stim_instr = visual.TextStim(window, text, height = 25, wrapWidth = 1000, font="Times")
        text_stim_instr.pos = (0,0)
        text_stim_instr.color = "black"
        
        text_instr = u'Du har svarat "Ja" ' + str(n_yes_inputs) + u' gånger. Du kan svara "Ja" ' + str(n_yes_inputs_left) + u' gånger till. \n \n Du har ' + str(n_trials_left) + u' försök kvar.'
        text_stim_instr.setText(text_instr)
        text_stim_instr.draw()
        window.flip()
        
        input_box = gui.Dlg(title="", labelButtonOK = "ja", labelButtonCancel = "nej", pos = (900,800))
        input_box.addText(u'Söker talaren respons från lyssnaren?')
        user_input = -1
        input_box.show()
        if input_box.OK:
            user_input = 1
        else:
            user_input = 0

        output = {'trial_type': trial_type, 'user_input': user_input}

        return output

#################################################################################

def L2_prosody_instruction_trial(window, sound_path):
    
    waiting_time = 1.5
    
    text = u'- Äsch, om det händer så händer det.'
    text_stim_instr = visual.TextStim(window, text, height = 25, wrapWidth = 1000, font="Times")
    text_stim_instr.pos = (0,0)
    text_stim_instr.color = "black"
    text_stim_instr.setText(u'Du kommer nu att få höra en person som söker respons.')
    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*2)
    
    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
    input_box.show()
    if not input_box.OK:
        return
    
    ################################
    # Test trial
    ################################
    
    # Trial text
    text_stim = visual.TextStim(window, height = 40, wrapWidth = 1000)
    text_stim.setText(text)
    
    text_stim.pos = (0,0)
    text_stim.color = "black"
    text_stim.bold = False
    
    text_stim.draw()
    window.flip()
    
    # Hold the text
    core.wait(waiting_time)
    
    # Sound
    sound_file_1_name = "L2_prosody_instruction_test.wav"
    # Play the sound
    playsound(sound_path + sound_file_1_name)
    
    ################################
    # Control trial
    ################################
    
    text_stim_instr.setText(u'Såhär låter personen när den inte söker respons.')
    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*2)

    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
    input_box.show()
    if not input_box.OK:
        return
    
    
    # Draw the text again
    text_stim.draw()
    window.flip()
    
    core.wait(waiting_time)
    
    sound_file_2_name = "L2_prosody_instruction_control.wav"
    playsound(sound_path + sound_file_2_name)
    
    window.flip()
    

    ################################
    
    #text_stim_instr.setText(u'I det riktiga testet kommer du att bara att få höra antingen en person som söker respons eller inte söker respons. Efter varje ljuduppspelning kommer du att få frågan om du tror att personen söker respons eller ej.')
   
#    text_stim_instr.draw()
#    window.flip()
#    core.wait(waiting_time*5)


