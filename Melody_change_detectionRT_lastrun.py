#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Wed Jan 31 18:01:13 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Melody_change_detectionRT'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/tysendauer/NeuroMusic/Behavioral/MelodyChange/Melody_change_detectionRT.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
Inst_text = visual.TextStim(win=win, name='Inst_text',
    text='Welcome to the experiment "Melody Change Detection"! \n\nYou will be listening to a continuous melody that is made up of repeating melodic units.\n\nAs you listen to the melody, hit the space bar as soon as you hear the melodic unit change.\n\nIf you can predict the melody change, hit the space bar at the time you expect the melody to change.\n\nAfter the practice trial there are 8 blocks, each less than 2 minutes.\n\nHit the space bar to start a practice trial.',
    font='Georgia',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practice_trial"
practice_trialClock = core.Clock()
practice_trial_text = visual.TextStim(win=win, name='practice_trial_text',
    text='Hit the space bar every time you hear the melody change.\n\nIf you can predict the melody change, hit the space bar at the time you expect the melody to change.\n\nWhen you are ready to go to the actual test, hit the down cursor key.',
    font='Georgia',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
practice_sound = sound.Sound('A', secs=-1)
practice_sound.setVolume(1)

# Initialize components for Routine "Ready_for_test"
Ready_for_testClock = core.Clock()
Ready_text = visual.TextStim(win=win, name='Ready_text',
    text='If you are ready, hit the space bar to start the next block.',
    font='Georgia',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
During_trial_text = visual.TextStim(win=win, name='During_trial_text',
    text='Hit the space bar every time you hear the melody change.\n\nIf you can predict the melody change, hit the space bar at the time you expect the melody to change.',
    font='Georgia',
    pos=[0, 0.5], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
go_next_text = visual.TextStim(win=win, name='go_next_text',
    text='Ready to start the next trial?\n\nHit the space bar.',
    font='Georgia',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "good_bye"
good_byeClock = core.Clock()
bye_text = visual.TextStim(win=win, name='bye_text',
    text='Many thanks for participating in the "Melody Change Detection" experiment!\n',
    font='Georgia',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_1 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionComponents = [Inst_text, key_resp_1]
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Inst_text* updates
    if t >= 0.0 and Inst_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Inst_text.tStart = t
        Inst_text.frameNStart = frameN  # exact frame index
        Inst_text.setAutoDraw(True)
    
    # *key_resp_1* updates
    if t >= 0.0 and key_resp_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_1.tStart = t
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.status = STARTED
        # keyboard checking is just starting
    if key_resp_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_practice.csv'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial.keys():
        exec(paramName + '= thisPractice_trial.' + paramName)

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial.keys():
            exec(paramName + '= thisPractice_trial.' + paramName)
    
    # ------Prepare to start Routine "practice_trial"-------
    t = 0
    practice_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    practice_sound.setSound(snd, secs=-1)
    go_test_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    practice_trialComponents = [practice_trial_text, practice_sound, go_test_resp]
    for thisComponent in practice_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice_trial"-------
    while continueRoutine:
        # get current time
        t = practice_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_trial_text* updates
        if t >= 0.0 and practice_trial_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_trial_text.tStart = t
            practice_trial_text.frameNStart = frameN  # exact frame index
            practice_trial_text.setAutoDraw(True)
        # start/stop practice_sound
        if t >= 5.0 and practice_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_sound.tStart = t
            practice_sound.frameNStart = frameN  # exact frame index
            practice_sound.play()  # start the sound (it finishes automatically)
        
        # *go_test_resp* updates
        if t >= 5.0 and go_test_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            go_test_resp.tStart = t
            go_test_resp.frameNStart = frameN  # exact frame index
            go_test_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if go_test_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['down'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_trial"-------
    for thisComponent in practice_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_sound.stop()  # ensure sound has stopped at end of routine
    # the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials'


# ------Prepare to start Routine "Ready_for_test"-------
t = 0
Ready_for_testClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
go_test = event.BuilderKeyResponse()
# keep track of which components have finished
Ready_for_testComponents = [Ready_text, go_test]
for thisComponent in Ready_for_testComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Ready_for_test"-------
while continueRoutine:
    # get current time
    t = Ready_for_testClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ready_text* updates
    if t >= 0.0 and Ready_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Ready_text.tStart = t
        Ready_text.frameNStart = frameN  # exact frame index
        Ready_text.setAutoDraw(True)
    
    # *go_test* updates
    if t >= 0.0 and go_test.status == NOT_STARTED:
        # keep track of start time/frame for later
        go_test.tStart = t
        go_test.frameNStart = frameN  # exact frame index
        go_test.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if go_test.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ready_for_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready_for_test"-------
for thisComponent in Ready_for_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Ready_for_test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_loop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='trials_loop')
thisExp.addLoop(trials_loop)  # add the loop to the experiment
thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
if thisTrials_loop != None:
    for paramName in thisTrials_loop.keys():
        exec(paramName + '= thisTrials_loop.' + paramName)

for thisTrials_loop in trials_loop:
    currentLoop = trials_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop.keys():
            exec(paramName + '= thisTrials_loop.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    sound_1.setSound(snd, secs=100.0)
    detection_resp = event.BuilderKeyResponse()
    go_next_resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [ISI, During_trial_text, sound_1, detection_resp, go_next_text, go_next_resp]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *During_trial_text* updates
        if t >= 1.0 and During_trial_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            During_trial_text.tStart = t
            During_trial_text.frameNStart = frameN  # exact frame index
            During_trial_text.setAutoDraw(True)
        frameRemains = 105.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if During_trial_text.status == STARTED and t >= frameRemains:
            During_trial_text.setAutoDraw(False)
        # start/stop sound_1
        if t >= 5.0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        frameRemains = 5.0 + 100.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sound_1.status == STARTED and t >= frameRemains:
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *detection_resp* updates
        if t >= 5.0 and detection_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            detection_resp.tStart = t
            detection_resp.frameNStart = frameN  # exact frame index
            detection_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(detection_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 5.0 + 100.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if detection_resp.status == STARTED and t >= frameRemains:
            detection_resp.status = STOPPED
        if detection_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                detection_resp.keys.extend(theseKeys)  # storing all keys
                detection_resp.rt.append(detection_resp.clock.getTime())
        
        # *go_next_text* updates
        if t >= 105.5 and go_next_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            go_next_text.tStart = t
            go_next_text.frameNStart = frameN  # exact frame index
            go_next_text.setAutoDraw(True)
        
        # *go_next_resp* updates
        if t >= 105.5 and go_next_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            go_next_resp.tStart = t
            go_next_resp.frameNStart = frameN  # exact frame index
            go_next_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if go_next_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if t >= 0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1.0)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # check responses
    if detection_resp.keys in ['', [], None]:  # No response was made
        detection_resp.keys=None
    trials_loop.addData('detection_resp.keys',detection_resp.keys)
    if detection_resp.keys != None:  # we had a response
        trials_loop.addData('detection_resp.rt', detection_resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials_loop'


# ------Prepare to start Routine "good_bye"-------
t = 0
good_byeClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
good_byeComponents = [bye_text]
for thisComponent in good_byeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "good_bye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = good_byeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bye_text* updates
    if t >= 0.0 and bye_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        bye_text.tStart = t
        bye_text.frameNStart = frameN  # exact frame index
        bye_text.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if bye_text.status == STARTED and t >= frameRemains:
        bye_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in good_byeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "good_bye"-------
for thisComponent in good_byeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
