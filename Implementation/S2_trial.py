#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import visual, core, event
from psychopy import gui
from playsound import playsound
import sounddevice as sd
import pyaudio
import wave

def S2_test_trial(window, text, data_path, trial_type, trial_nr, participant_ID, request_user_input):
    
    waiting_time = 1

    # Trial text
    text_stim = visual.TextStim(window, height = 40, wrapWidth = 1000)
    text_stim.setText(text)
    
    text_stim.pos = (0,0)
    text_stim.color = "black"
    text_stim.bold = False
    
    # Instructions:
    
    text_stim_instr = visual.TextStim(window, height = 25, wrapWidth = 1000, font="Times")
    text_stim_instr.pos = (0,0)
    text_stim_instr.color = "black"
    text_instr_test = (u'Läs texten som följer på ett sätt som att du VILL ha respons på det du säger från den tänkta lyssnaren.')
    text_instr_control = (u'Läs texten som följer på ett sätt som att du INTE behöver ha respons på det du säger från den tänkta lyssnaren.')
    
    if trial_type == 1:
            text_stim_instr.setText(text_instr_test)
    else:
            text_stim_instr.setText(text_instr_control)

    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*2)

    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
    user_input = -1
    input_box.show()
    if not input_box.OK:
        return
    
    # Draw trial text
    text_stim.draw()
    window.flip()

    if request_user_input:
        core.wait(waiting_time)
    else:
        core.wait(waiting_time*5)
    
    # Prepare for recording
    
    ##################
    # pyaudio:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 48000
    RECORD_SECONDS = 10
    if trial_type == 1:
        WAVE_OUTPUT_FILENAME = data_path + "S2_recording_" + str(trial_nr) + "_test_trial_" + participant_ID + ".wav"
    else:
        WAVE_OUTPUT_FILENAME = data_path + "S2_recording_" + str(trial_nr) + "_control_trial_" + participant_ID + ".wav"

    if request_user_input:
    
        p = pyaudio.PyAudio()
        ##################

        input_box = gui.Dlg(title="", labelButtonOK = "Spela in", labelButtonCancel = "Avbryt", pos = (900,800))
        input_box.addText(u'Tryck på "spela in" när du är redo att läsa upp texten. Texten blir röd/grön under inspelningen.')
        user_input = -1
        input_box.show()
        
        
        if input_box.OK:
            
            # Draw the text again
            if trial_type == 1:
                text_stim.color = "green"
            else:
                text_stim.color = "red"
            text_stim.draw()
            window.flip()
            ##################
            # pyaudio
            
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
                
            print("* recording")

            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("* done recording")
            text_stim_instr.setText(u'Slut på inspelning')
            text_stim_instr.draw()
            window.flip()
            core.wait(2)

            stream.stop_stream()
            stream.close()
            p.terminate()
    
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

   

#################################################################################

def S2_instruction_trial(window, data_path):
    
    waiting_time = 1.5
    
    text_stim_instr = visual.TextStim(window, height = 25, wrapWidth = 1000, font="Times")
    text_stim_instr.pos = (0,0)
    text_stim_instr.color = "black"
    text_stim_instr.setText(u'\n Du kommer att få trycka på en knapp när du är redo att spela in. Inspelningen sker sedan under 10 sekunder och när inspelningen är slut visas orden "Slut på inspelning". \n \n Texten du ska läsa byter färg när inspelningen är igång. Den är grön om du fått instruktionen att låta som du vill ha respons, och röd om du inte ska låta som du vill ha respons. \n \n Om du börjar direkt när du tryckt på knappen har du gott om tid.')
    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*10)
    
    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
    user_input = -1
    input_box.show()
    if not input_box.OK:
        return
    
    ################################
    # Test trial
    ################################
    
    text_stim_instr.setText(u'Läs texten som följer på ett sätt som att du VILL ha respons på det du säger från den tänkta lyssnaren.')
    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*5)

    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,800))
    user_input = -1
    input_box.show()
    if not input_box.OK:
        return
    
    # Trial text
    text = u'- Men den trappan har ovanligt höga trappsteg.'
    text_stim = visual.TextStim(window, height = 40, wrapWidth = 1000)
    text_stim.setText(text)
    
    text_stim.pos = (0,0)
    text_stim.color = "black"
    text_stim.bold = False
    
    text_stim.draw()
    window.flip()
    
    # Hold the text
    core.wait(waiting_time)
    
    # Prepare for recording
    
    ##################
    # pyaudio:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 48000
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = data_path + "instrucrion_yes.wav"

    p = pyaudio.PyAudio()
    ##################
    
    input_box = gui.Dlg(title="", labelButtonOK = "Spela in", labelButtonCancel = "Avbryt", pos = (900,800))
    input_box.addText(u'Tryck på "spela in" när du är redo att läsa upp texten.')
    user_input = -1
    input_box.show()
    
    if input_box.OK:
        
        # Draw the text again
        text_stim.color = "green"
        text_stim.draw()
        window.flip()
        ##################
        # pyaudio
        
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
                        
        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")
        text_stim_instr.setText(u'Slut på inspelning')
        text_stim_instr.draw()
        window.flip()
        core.wait(2)
            
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
            

    ################################
    # Control trial
    ################################
    
    text_stim_instr.setText(u'Läs texten som följer på ett sätt som att du INTE behöver ha respons på det du säger från den tänkta lyssnaren.')
    text_stim_instr.draw()
    window.flip()
    core.wait(waiting_time*5)

    input_box = gui.Dlg(title="", labelButtonOK = u"Fortsätt", labelButtonCancel = "Avbryt", pos = (900,900))
    user_input = -1
    input_box.show()
    if not input_box.OK:
        return

    # Trial text
    text_stim.color = "black"
    text_stim.draw()
    window.flip()
    
    # Hold the text
    core.wait(waiting_time)
    
    # Prepare for recording
    
    ##################
    WAVE_OUTPUT_FILENAME = data_path + "instruction_no.wav"
    
    p = pyaudio.PyAudio()
    ##################
    
    input_box = gui.Dlg(title="", labelButtonOK = "Spela in", labelButtonCancel = "Avbryt", pos = (900,900))
    input_box.addText(u'Tryck på "spela in" när du är redo att läsa upp texten.')
    user_input = -1
    input_box.show()

    if input_box.OK:
        
        # Draw the text again
        text_stim.color = "red"
        text_stim.draw()
        window.flip()
        ##################
        # pyaudio
        
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
            
        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")
        text_stim_instr.setText(u'Slut på inspelning')
        text_stim_instr.draw()
        window.flip()
        core.wait(2)

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()




    ################################
    
#    text_stim_instr.setText(u'I det riktiga testet kommer du att bara att få instruktionen antingen att säga meningen som att du vill ha respons eller som om du inte behövde respons.')
#
#    text_stim_instr.draw()
#    window.flip()
#    core.wait(waiting_time*5)


