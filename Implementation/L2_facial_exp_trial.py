#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import visual, core, event
from psychopy import gui
from PyQt4.QtCore import QPoint

def L2_facial_exp_test_trial(window, text, image_path, trial_type, trial_nr, n_yes_inputs, request_user_input):
    
    waiting_time = 2
    
    text_stim = visual.TextStim(window, height = 50, wrapWidth = 1200)
    text_stim.setText(text)

    text_stim.pos = (50,-300)
    if trial_nr == 6:
        text_stim.color = "grey"
    else:
        text_stim.color = "white"
    text_stim.bold = True
    
  
    # Define images to draw

    img_1_stim = visual.ImageStim(window)
    img_1_file_name = "L2_facial_exp_" + str(trial_nr) + ".png"
    img_1_stim.setImage(image_path + img_1_file_name)
    img_1_stim.size = img_1_stim.size*0.40

    # Draw the first image and the text
    img_1_stim.draw()
    text_stim.draw()

    window.flip()

    core.wait(waiting_time*2.5)

    img_2_stim = visual.ImageStim(window)
    img_2_file_name = ""
    
    if trial_type == 1:
        img_2_file_name = "L2_facial_exp_" + str(trial_nr) + "_test.png"
    else:
        img_2_file_name = "L2_facial_exp_" + str(trial_nr) + "_control.png"
    img_2_stim.setImage(image_path + img_2_file_name)
    img_2_stim.size = img_2_stim.size*0.40
    
    # Draw the second image and the text again
    img_2_stim.draw()
    text_stim.draw()
    window.flip()

    core.wait(waiting_time*1.5)


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

def L2_facial_exp_instruction_trial(window, image_path):
    
    waiting_time = 2
    
    text = u'- För jag vill ju se hur färgen såg ut när den målades.'
    
    text_stim_instr = visual.TextStim(window, text, height = 25, wrapWidth = 1000, font="Times")
    text_stim_instr.pos = (0,0)
    text_stim_instr.color = "black"
    text_stim_instr.setText(u'Du kommer nu att få se en person som söker respons.')
    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*2)
    
    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
    user_input = -1
    input_box.show()
    if not input_box.OK:
        return
    
    ################################
    # Test trial
    ################################
    
    # Trial text
    text_stim = visual.TextStim(window, height = 40, wrapWidth = 1000)
    text_stim.setText(text)
    
    text_stim.pos = (50,-300)
    text_stim.color = "white"
    text_stim.bold = True
    

    # Define images to draw
    img_1_stim = visual.ImageStim(window)
    img_1_file_name = "L2_facial_exp_instruction.png"
    img_1_stim.setImage(image_path + img_1_file_name)
    img_1_stim.size = img_1_stim.size*0.40
    
    # Draw the first image and the text
    img_1_stim.draw()
    text_stim.draw()
    window.flip()
    
    # Hold the image
    core.wait(waiting_time*2)
    
    img_2_stim = visual.ImageStim(window)
    img_2_file_name = ""
    

    img_2_file_name = "L2_facial_exp_instruction_test.png"
    img_2_stim.setImage(image_path + img_2_file_name)
    img_2_stim.size = img_2_stim.size*0.40
    
    # Draw the second image and the text again
    img_2_stim.draw()
    text_stim.draw()
    window.flip()
    
    core.wait(waiting_time*1.5)

    
    # Input from user: response-seeking or not
    
    window.flip()
    
#    input_box = gui.Dlg(title="MMU", labelButtonOK = "ja", labelButtonCancel = "nej", pos = QPoint(800,500))
#    input_box.addText(u'Söker talaren respons från lyssnaren?')
#    #input_box.addField('Soker talaren respons fran lyssnaren?', choices=["Ja", "Nej"])
#    user_input = -1
#    input_box.show()
#    if input_box.OK:
#        user_input = 1


    ################################

    text_stim_instr.setText(u'Såhär ser personen ut när den inte söker respons.')
    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*2)
    
    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
    input_box.show()
    if not input_box.OK:
        return

    ################################
    # Control trial
    ################################


    # Draw the first image and the text
    img_1_stim.draw()
    text_stim.draw()
    window.flip()
    
    # Hold the image
    core.wait(waiting_time*2)
    
    img_3_stim = visual.ImageStim(window)
    img_3_file_name = "L2_facial_exp_instruction_control.png"
    img_3_stim.setImage(image_path + img_3_file_name)
    img_3_stim.size = img_3_stim.size*0.40
    
    # Draw the second image and the text again
    img_3_stim.draw()
    text_stim.draw()
    window.flip()
    
    #TODO# Different waiting times for different trials
    core.wait(waiting_time*1.5)



