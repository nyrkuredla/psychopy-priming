#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), June 10, 2016, at 09:19
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'priming_test'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'G:\\Compounding\\priming_test.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions_ENG"
instructions_ENGClock = core.Clock()
instruct_ENG1 = visual.TextStim(win=win, ori=0, name='instruct_ENG1',
    text='Hello! Thank you for agreeing to participate in this study.\n\nThe experiment will begin with a practice session and trials in English, followed by practice and trials in Polish. If you have any questions during the practice sessions, please feel free to ask.\n\nOn the screen, you will see a series of hash marks ("########"), followed by a series of letters. Please use the LEFT and RIGHT arrow keys to indicate whether the letters form a real word in English. \nIf it is a word, press LEFT <-. If it is not a word, press RIGHT ->.\n\nIf you are ready to continue, please press SPACE.',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "mask"
maskClock = core.Clock()
masking1 = visual.TextStim(win=win, ori=0, name='masking1',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
primeENG = visual.TextStim(win=win, ori=0, name='primeENG',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
masking2 = visual.TextStim(win=win, ori=0, name='masking2',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "practice_ENG"
practice_ENGClock = core.Clock()
prac_quesENG = visual.TextStim(win=win, ori=0, name='prac_quesENG',
    text='           Is it a word?\n\n<- YES                     NO -> ',    font='Arial',
    pos=[0, -0.4], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
prac_targetENG = visual.TextStim(win=win, ori=0, name='prac_targetENG',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instructions_ENG_trial"
instructions_ENG_trialClock = core.Clock()
instructions_ENG2 = visual.TextStim(win=win, ori=0, name='instructions_ENG2',
    text='The practice session is over. We will now begin the experiment.\n\nIf you have any questions at this time, please feel free to ask.\n\nOtherwise, if you are ready, please press SPACE to continue.',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "mask_trial_ENG"
mask_trial_ENGClock = core.Clock()
masking1_2 = visual.TextStim(win=win, ori=0, name='masking1_2',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
primeENG_trial = visual.TextStim(win=win, ori=0, name='primeENG_trial',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
masking2_2 = visual.TextStim(win=win, ori=0, name='masking2_2',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial_ENG"
trial_ENGClock = core.Clock()
trial_quesENG = visual.TextStim(win=win, ori=0, name='trial_quesENG',
    text='           Is it a word?\n\n<- YES                     NO -> ',    font='Arial',
    pos=[0, -0.4], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
trial_targetENG = visual.TextStim(win=win, ori=0, name='trial_targetENG',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instructions_POL"
instructions_POLClock = core.Clock()
instruct_POL1 = visual.TextStim(win=win, ori=0, name='instruct_POL1',
    text=u'Cz\u0119\u015b\u0107 angielska eksperymentu dobieg\u0142a ko\u0144ca. Dzi\u0119kujemy!\n\nTak jak poprzednio w\u0142a\u015bciwy eksperyment poprzedzi kr\xf3tka sesja treningowa. \nNa ekranie pojawi si\u0119 seria znak\xf3w ("########"), a nast\u0119pnie ci\u0105g liter. Przy pomocy strza\u0142ek w LEWO oraz PRAWO prosimy zdecydowa\u0107, czy litery tworz\u0105 s\u0142owo w j\u0119zyku polskim. \nJe\u015bli tak, prosimy nacisn\u0105\u0107 strza\u0142k\u0119 w lewo <-. \nJe\u015bli nie, prosimy nacisn\u0105\u0107 strza\u0142k\u0119 w prawo. ->.\n\nAby przej\u015b\u0107 do sesji treningowej, prosimy nacisn\u0105\u0107 spacj\u0119.\n',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "mask_prac_POL"
mask_prac_POLClock = core.Clock()
masking1_3 = visual.TextStim(win=win, ori=0, name='masking1_3',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
primePOL = visual.TextStim(win=win, ori=0, name='primePOL',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
masking2_3 = visual.TextStim(win=win, ori=0, name='masking2_3',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "practice_POL"
practice_POLClock = core.Clock()
prac_quesPOL = visual.TextStim(win=win, ori=0, name='prac_quesPOL',
    text='           Is it a word?\n\n<- YES                     NO -> ',    font='Arial',
    pos=[0, -0.4], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
prac_targetPOL = visual.TextStim(win=win, ori=0, name='prac_targetPOL',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instructions_POL_trial"
instructions_POL_trialClock = core.Clock()
instructions_POL_exp = visual.TextStim(win=win, ori=0, name='instructions_POL_exp',
    text=u'Sesja treningowa dobieg\u0142a ko\u0144ca.\n\nW przypadku jakichkolwiek w\u0105tpliwo\u015bci, zach\u0119camy do zadawania pyta\u0144.\n\nJe\u017celi wszystko jest jasne, prosimy nacisn\u0105\u0107 spacj\u0119 w celu rozpocz\u0119cia eksperymentu.\n',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "mask_trial_POL"
mask_trial_POLClock = core.Clock()
masking1_4 = visual.TextStim(win=win, ori=0, name='masking1_4',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
primePOLexp = visual.TextStim(win=win, ori=0, name='primePOLexp',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
masking2_4 = visual.TextStim(win=win, ori=0, name='masking2_4',
    text='##########',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial_POL"
trial_POLClock = core.Clock()
trial_quesPOL = visual.TextStim(win=win, ori=0, name='trial_quesPOL',
    text='           Is it a word?\n\n<- YES                     NO -> ',    font='Arial',
    pos=[0, -0.4], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
trial_targetPOL = visual.TextStim(win=win, ori=0, name='trial_targetPOL',
    text='default text',    font='Arial',
    pos=[0, 0.2], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thankyou = visual.TextStim(win=win, ori=0, name='thankyou',
    text=u'Thank you! The experiment is over. \n\nBardzo dzi\u0119kujemy za udzia\u0142 w eksperymencie!\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions_ENG"-------
t = 0
instructions_ENGClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructions_ENGComponents = []
instructions_ENGComponents.append(instruct_ENG1)
instructions_ENGComponents.append(key_resp_2)
for thisComponent in instructions_ENGComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_ENG"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_ENGClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_ENG1* updates
    if t >= 0.0 and instruct_ENG1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_ENG1.tStart = t  # underestimates by a little under one frame
        instruct_ENG1.frameNStart = frameN  # exact frame index
        instruct_ENG1.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
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
    for thisComponent in instructions_ENGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_ENG"-------
for thisComponent in instructions_ENGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_ENG" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_EN = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('priming_practice.csv'),
    seed=None, name='practice_EN')
thisExp.addLoop(practice_EN)  # add the loop to the experiment
thisPractice_EN = practice_EN.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPractice_EN.rgb)
if thisPractice_EN != None:
    for paramName in thisPractice_EN.keys():
        exec(paramName + '= thisPractice_EN.' + paramName)

for thisPractice_EN in practice_EN:
    currentLoop = practice_EN
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_EN.rgb)
    if thisPractice_EN != None:
        for paramName in thisPractice_EN.keys():
            exec(paramName + '= thisPractice_EN.' + paramName)
    
    #------Prepare to start Routine "mask"-------
    t = 0
    maskClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.050000)
    # update component parameters for each repeat
    primeENG.setText(prime_exp_ENG_prac)
    # keep track of which components have finished
    maskComponents = []
    maskComponents.append(masking1)
    maskComponents.append(primeENG)
    maskComponents.append(masking2)
    for thisComponent in maskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "mask"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *masking1* updates
        if t >= 0.0 and masking1.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking1.tStart = t  # underestimates by a little under one frame
            masking1.frameNStart = frameN  # exact frame index
            masking1.setAutoDraw(True)
        if masking1.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking1.setAutoDraw(False)
        
        # *primeENG* updates
        if t >= 1.0 and primeENG.status == NOT_STARTED:
            # keep track of start time/frame for later
            primeENG.tStart = t  # underestimates by a little under one frame
            primeENG.frameNStart = frameN  # exact frame index
            primeENG.setAutoDraw(True)
        if primeENG.status == STARTED and t >= (1.0 + (0.05-win.monitorFramePeriod*0.75)): #most of one frame period left
            primeENG.setAutoDraw(False)
        
        # *masking2* updates
        if t >= 1.05 and masking2.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking2.tStart = t  # underestimates by a little under one frame
            masking2.frameNStart = frameN  # exact frame index
            masking2.setAutoDraw(True)
        if masking2.status == STARTED and t >= (1.05 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "practice_ENG"-------
    t = 0
    practice_ENGClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    prac_targetENG.setText(comp_ENG_prac)
    prac_ansENG = event.BuilderKeyResponse()  # create an object of type KeyResponse
    prac_ansENG.status = NOT_STARTED
    # keep track of which components have finished
    practice_ENGComponents = []
    practice_ENGComponents.append(prac_quesENG)
    practice_ENGComponents.append(prac_targetENG)
    practice_ENGComponents.append(prac_ansENG)
    for thisComponent in practice_ENGComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice_ENG"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = practice_ENGClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_quesENG* updates
        if t >= 0.0 and prac_quesENG.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_quesENG.tStart = t  # underestimates by a little under one frame
            prac_quesENG.frameNStart = frameN  # exact frame index
            prac_quesENG.setAutoDraw(True)
        
        # *prac_targetENG* updates
        if t >= 0.0 and prac_targetENG.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_targetENG.tStart = t  # underestimates by a little under one frame
            prac_targetENG.frameNStart = frameN  # exact frame index
            prac_targetENG.setAutoDraw(True)
        
        # *prac_ansENG* updates
        if t >= 0.0 and prac_ansENG.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_ansENG.tStart = t  # underestimates by a little under one frame
            prac_ansENG.frameNStart = frameN  # exact frame index
            prac_ansENG.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(prac_ansENG.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if prac_ansENG.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                prac_ansENG.keys = theseKeys[-1]  # just the last key pressed
                prac_ansENG.rt = prac_ansENG.clock.getTime()
                # was this 'correct'?
                if (prac_ansENG.keys == str(ans_ENG_prac)) or (prac_ansENG.keys == ans_ENG_prac):
                    prac_ansENG.corr = 1
                else:
                    prac_ansENG.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_ENGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practice_ENG"-------
    for thisComponent in practice_ENGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_ansENG.keys in ['', [], None]:  # No response was made
       prac_ansENG.keys=None
       # was no response the correct answer?!
       if str(ans_ENG_prac).lower() == 'none': prac_ansENG.corr = 1  # correct non-response
       else: prac_ansENG.corr = 0  # failed to respond (incorrectly)
    # store data for practice_EN (TrialHandler)
    practice_EN.addData('prac_ansENG.keys',prac_ansENG.keys)
    practice_EN.addData('prac_ansENG.corr', prac_ansENG.corr)
    if prac_ansENG.keys != None:  # we had a response
        practice_EN.addData('prac_ansENG.rt', prac_ansENG.rt)
    # the Routine "practice_ENG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_EN'


#------Prepare to start Routine "instructions_ENG_trial"-------
t = 0
instructions_ENG_trialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instructions_ENG_trialComponents = []
instructions_ENG_trialComponents.append(instructions_ENG2)
instructions_ENG_trialComponents.append(key_resp_3)
for thisComponent in instructions_ENG_trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_ENG_trial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_ENG_trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_ENG2* updates
    if t >= 0.0 and instructions_ENG2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_ENG2.tStart = t  # underestimates by a little under one frame
        instructions_ENG2.frameNStart = frameN  # exact frame index
        instructions_ENG2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
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
    for thisComponent in instructions_ENG_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_ENG_trial"-------
for thisComponent in instructions_ENG_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_ENG_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial_EN = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'priming_list.csv'),
    seed=None, name='trial_EN')
thisExp.addLoop(trial_EN)  # add the loop to the experiment
thisTrial_EN = trial_EN.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_EN.rgb)
if thisTrial_EN != None:
    for paramName in thisTrial_EN.keys():
        exec(paramName + '= thisTrial_EN.' + paramName)

for thisTrial_EN in trial_EN:
    currentLoop = trial_EN
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_EN.rgb)
    if thisTrial_EN != None:
        for paramName in thisTrial_EN.keys():
            exec(paramName + '= thisTrial_EN.' + paramName)
    
    #------Prepare to start Routine "mask_trial_ENG"-------
    t = 0
    mask_trial_ENGClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.050000)
    # update component parameters for each repeat
    primeENG_trial.setText(prime_exp_ENG)
    # keep track of which components have finished
    mask_trial_ENGComponents = []
    mask_trial_ENGComponents.append(masking1_2)
    mask_trial_ENGComponents.append(primeENG_trial)
    mask_trial_ENGComponents.append(masking2_2)
    for thisComponent in mask_trial_ENGComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "mask_trial_ENG"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mask_trial_ENGClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *masking1_2* updates
        if t >= 0.0 and masking1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking1_2.tStart = t  # underestimates by a little under one frame
            masking1_2.frameNStart = frameN  # exact frame index
            masking1_2.setAutoDraw(True)
        if masking1_2.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking1_2.setAutoDraw(False)
        
        # *primeENG_trial* updates
        if t >= 1.0 and primeENG_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            primeENG_trial.tStart = t  # underestimates by a little under one frame
            primeENG_trial.frameNStart = frameN  # exact frame index
            primeENG_trial.setAutoDraw(True)
        if primeENG_trial.status == STARTED and t >= (1.0 + (0.05-win.monitorFramePeriod*0.75)): #most of one frame period left
            primeENG_trial.setAutoDraw(False)
        
        # *masking2_2* updates
        if t >= 1.05 and masking2_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking2_2.tStart = t  # underestimates by a little under one frame
            masking2_2.frameNStart = frameN  # exact frame index
            masking2_2.setAutoDraw(True)
        if masking2_2.status == STARTED and t >= (1.05 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking2_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mask_trial_ENGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "mask_trial_ENG"-------
    for thisComponent in mask_trial_ENGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial_ENG"-------
    t = 0
    trial_ENGClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    trial_targetENG.setText(compFull_ENG)
    trial_ansENG = event.BuilderKeyResponse()  # create an object of type KeyResponse
    trial_ansENG.status = NOT_STARTED
    # keep track of which components have finished
    trial_ENGComponents = []
    trial_ENGComponents.append(trial_quesENG)
    trial_ENGComponents.append(trial_targetENG)
    trial_ENGComponents.append(trial_ansENG)
    for thisComponent in trial_ENGComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_ENG"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trial_ENGClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_quesENG* updates
        if t >= 0.0 and trial_quesENG.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_quesENG.tStart = t  # underestimates by a little under one frame
            trial_quesENG.frameNStart = frameN  # exact frame index
            trial_quesENG.setAutoDraw(True)
        
        # *trial_targetENG* updates
        if t >= 0.0 and trial_targetENG.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_targetENG.tStart = t  # underestimates by a little under one frame
            trial_targetENG.frameNStart = frameN  # exact frame index
            trial_targetENG.setAutoDraw(True)
        
        # *trial_ansENG* updates
        if t >= 0.0 and trial_ansENG.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_ansENG.tStart = t  # underestimates by a little under one frame
            trial_ansENG.frameNStart = frameN  # exact frame index
            trial_ansENG.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trial_ansENG.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if trial_ansENG.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_ansENG.keys = theseKeys[-1]  # just the last key pressed
                trial_ansENG.rt = trial_ansENG.clock.getTime()
                # was this 'correct'?
                if (trial_ansENG.keys == str(ans_ENG)) or (trial_ansENG.keys == ans_ENG):
                    trial_ansENG.corr = 1
                else:
                    trial_ansENG.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_ENGComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_ENG"-------
    for thisComponent in trial_ENGComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trial_ansENG.keys in ['', [], None]:  # No response was made
       trial_ansENG.keys=None
       # was no response the correct answer?!
       if str(ans_ENG).lower() == 'none': trial_ansENG.corr = 1  # correct non-response
       else: trial_ansENG.corr = 0  # failed to respond (incorrectly)
    # store data for trial_EN (TrialHandler)
    trial_EN.addData('trial_ansENG.keys',trial_ansENG.keys)
    trial_EN.addData('trial_ansENG.corr', trial_ansENG.corr)
    if trial_ansENG.keys != None:  # we had a response
        trial_EN.addData('trial_ansENG.rt', trial_ansENG.rt)
    # the Routine "trial_ENG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial_EN'


#------Prepare to start Routine "instructions_POL"-------
t = 0
instructions_POLClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
instructions_POLComponents = []
instructions_POLComponents.append(instruct_POL1)
instructions_POLComponents.append(key_resp_4)
for thisComponent in instructions_POLComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_POL"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_POLClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_POL1* updates
    if t >= 0.0 and instruct_POL1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_POL1.tStart = t  # underestimates by a little under one frame
        instruct_POL1.frameNStart = frameN  # exact frame index
        instruct_POL1.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
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
    for thisComponent in instructions_POLComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_POL"-------
for thisComponent in instructions_POLComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_POL" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_PL = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'priming_practice.csv'),
    seed=None, name='prac_PL')
thisExp.addLoop(prac_PL)  # add the loop to the experiment
thisPrac_PL = prac_PL.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPrac_PL.rgb)
if thisPrac_PL != None:
    for paramName in thisPrac_PL.keys():
        exec(paramName + '= thisPrac_PL.' + paramName)

for thisPrac_PL in prac_PL:
    currentLoop = prac_PL
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_PL.rgb)
    if thisPrac_PL != None:
        for paramName in thisPrac_PL.keys():
            exec(paramName + '= thisPrac_PL.' + paramName)
    
    #------Prepare to start Routine "mask_prac_POL"-------
    t = 0
    mask_prac_POLClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.050000)
    # update component parameters for each repeat
    primePOL.setText(prime_exp_POL_prac)
    # keep track of which components have finished
    mask_prac_POLComponents = []
    mask_prac_POLComponents.append(masking1_3)
    mask_prac_POLComponents.append(primePOL)
    mask_prac_POLComponents.append(masking2_3)
    for thisComponent in mask_prac_POLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "mask_prac_POL"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mask_prac_POLClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *masking1_3* updates
        if t >= 0.0 and masking1_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking1_3.tStart = t  # underestimates by a little under one frame
            masking1_3.frameNStart = frameN  # exact frame index
            masking1_3.setAutoDraw(True)
        if masking1_3.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking1_3.setAutoDraw(False)
        
        # *primePOL* updates
        if t >= 1.0 and primePOL.status == NOT_STARTED:
            # keep track of start time/frame for later
            primePOL.tStart = t  # underestimates by a little under one frame
            primePOL.frameNStart = frameN  # exact frame index
            primePOL.setAutoDraw(True)
        if primePOL.status == STARTED and t >= (1.0 + (0.05-win.monitorFramePeriod*0.75)): #most of one frame period left
            primePOL.setAutoDraw(False)
        
        # *masking2_3* updates
        if t >= 1.05 and masking2_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking2_3.tStart = t  # underestimates by a little under one frame
            masking2_3.frameNStart = frameN  # exact frame index
            masking2_3.setAutoDraw(True)
        if masking2_3.status == STARTED and t >= (1.05 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking2_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mask_prac_POLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "mask_prac_POL"-------
    for thisComponent in mask_prac_POLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "practice_POL"-------
    t = 0
    practice_POLClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    prac_targetPOL.setText(comp_POL_prac)
    prac_ansPOL = event.BuilderKeyResponse()  # create an object of type KeyResponse
    prac_ansPOL.status = NOT_STARTED
    # keep track of which components have finished
    practice_POLComponents = []
    practice_POLComponents.append(prac_quesPOL)
    practice_POLComponents.append(prac_targetPOL)
    practice_POLComponents.append(prac_ansPOL)
    for thisComponent in practice_POLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "practice_POL"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = practice_POLClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_quesPOL* updates
        if t >= 0.0 and prac_quesPOL.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_quesPOL.tStart = t  # underestimates by a little under one frame
            prac_quesPOL.frameNStart = frameN  # exact frame index
            prac_quesPOL.setAutoDraw(True)
        
        # *prac_targetPOL* updates
        if t >= 0.0 and prac_targetPOL.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_targetPOL.tStart = t  # underestimates by a little under one frame
            prac_targetPOL.frameNStart = frameN  # exact frame index
            prac_targetPOL.setAutoDraw(True)
        
        # *prac_ansPOL* updates
        if t >= 0.0 and prac_ansPOL.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_ansPOL.tStart = t  # underestimates by a little under one frame
            prac_ansPOL.frameNStart = frameN  # exact frame index
            prac_ansPOL.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(prac_ansPOL.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if prac_ansPOL.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                prac_ansPOL.keys = theseKeys[-1]  # just the last key pressed
                prac_ansPOL.rt = prac_ansPOL.clock.getTime()
                # was this 'correct'?
                if (prac_ansPOL.keys == str(ans_POL_prac)) or (prac_ansPOL.keys == ans_POL_prac):
                    prac_ansPOL.corr = 1
                else:
                    prac_ansPOL.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_POLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "practice_POL"-------
    for thisComponent in practice_POLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_ansPOL.keys in ['', [], None]:  # No response was made
       prac_ansPOL.keys=None
       # was no response the correct answer?!
       if str(ans_POL_prac).lower() == 'none': prac_ansPOL.corr = 1  # correct non-response
       else: prac_ansPOL.corr = 0  # failed to respond (incorrectly)
    # store data for prac_PL (TrialHandler)
    prac_PL.addData('prac_ansPOL.keys',prac_ansPOL.keys)
    prac_PL.addData('prac_ansPOL.corr', prac_ansPOL.corr)
    if prac_ansPOL.keys != None:  # we had a response
        prac_PL.addData('prac_ansPOL.rt', prac_ansPOL.rt)
    # the Routine "practice_POL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_PL'


#------Prepare to start Routine "instructions_POL_trial"-------
t = 0
instructions_POL_trialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instructions_POL_trialComponents = []
instructions_POL_trialComponents.append(instructions_POL_exp)
instructions_POL_trialComponents.append(key_resp_5)
for thisComponent in instructions_POL_trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_POL_trial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_POL_trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_POL_exp* updates
    if t >= 0.0 and instructions_POL_exp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_POL_exp.tStart = t  # underestimates by a little under one frame
        instructions_POL_exp.frameNStart = frameN  # exact frame index
        instructions_POL_exp.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
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
    for thisComponent in instructions_POL_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions_POL_trial"-------
for thisComponent in instructions_POL_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_POL_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_PL = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'priming_list.csv'),
    seed=None, name='trials_PL')
thisExp.addLoop(trials_PL)  # add the loop to the experiment
thisTrials_PL = trials_PL.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrials_PL.rgb)
if thisTrials_PL != None:
    for paramName in thisTrials_PL.keys():
        exec(paramName + '= thisTrials_PL.' + paramName)

for thisTrials_PL in trials_PL:
    currentLoop = trials_PL
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_PL.rgb)
    if thisTrials_PL != None:
        for paramName in thisTrials_PL.keys():
            exec(paramName + '= thisTrials_PL.' + paramName)
    
    #------Prepare to start Routine "mask_trial_POL"-------
    t = 0
    mask_trial_POLClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.050000)
    # update component parameters for each repeat
    primePOLexp.setText(prime_exp_POL)
    # keep track of which components have finished
    mask_trial_POLComponents = []
    mask_trial_POLComponents.append(masking1_4)
    mask_trial_POLComponents.append(primePOLexp)
    mask_trial_POLComponents.append(masking2_4)
    for thisComponent in mask_trial_POLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "mask_trial_POL"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = mask_trial_POLClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *masking1_4* updates
        if t >= 0.0 and masking1_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking1_4.tStart = t  # underestimates by a little under one frame
            masking1_4.frameNStart = frameN  # exact frame index
            masking1_4.setAutoDraw(True)
        if masking1_4.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking1_4.setAutoDraw(False)
        
        # *primePOLexp* updates
        if t >= 1.0 and primePOLexp.status == NOT_STARTED:
            # keep track of start time/frame for later
            primePOLexp.tStart = t  # underestimates by a little under one frame
            primePOLexp.frameNStart = frameN  # exact frame index
            primePOLexp.setAutoDraw(True)
        if primePOLexp.status == STARTED and t >= (1.0 + (0.05-win.monitorFramePeriod*0.75)): #most of one frame period left
            primePOLexp.setAutoDraw(False)
        
        # *masking2_4* updates
        if t >= 1.05 and masking2_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            masking2_4.tStart = t  # underestimates by a little under one frame
            masking2_4.frameNStart = frameN  # exact frame index
            masking2_4.setAutoDraw(True)
        if masking2_4.status == STARTED and t >= (1.05 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            masking2_4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mask_trial_POLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "mask_trial_POL"-------
    for thisComponent in mask_trial_POLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial_POL"-------
    t = 0
    trial_POLClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    trial_targetPOL.setText(compFull_POL)
    trial_ansPOL = event.BuilderKeyResponse()  # create an object of type KeyResponse
    trial_ansPOL.status = NOT_STARTED
    # keep track of which components have finished
    trial_POLComponents = []
    trial_POLComponents.append(trial_quesPOL)
    trial_POLComponents.append(trial_targetPOL)
    trial_POLComponents.append(trial_ansPOL)
    for thisComponent in trial_POLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial_POL"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trial_POLClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_quesPOL* updates
        if t >= 0.0 and trial_quesPOL.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_quesPOL.tStart = t  # underestimates by a little under one frame
            trial_quesPOL.frameNStart = frameN  # exact frame index
            trial_quesPOL.setAutoDraw(True)
        
        # *trial_targetPOL* updates
        if t >= 0.0 and trial_targetPOL.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_targetPOL.tStart = t  # underestimates by a little under one frame
            trial_targetPOL.frameNStart = frameN  # exact frame index
            trial_targetPOL.setAutoDraw(True)
        
        # *trial_ansPOL* updates
        if t >= 0.0 and trial_ansPOL.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_ansPOL.tStart = t  # underestimates by a little under one frame
            trial_ansPOL.frameNStart = frameN  # exact frame index
            trial_ansPOL.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trial_ansPOL.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if trial_ansPOL.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_ansPOL.keys = theseKeys[-1]  # just the last key pressed
                trial_ansPOL.rt = trial_ansPOL.clock.getTime()
                # was this 'correct'?
                if (trial_ansPOL.keys == str(ans_POL)) or (trial_ansPOL.keys == ans_POL):
                    trial_ansPOL.corr = 1
                else:
                    trial_ansPOL.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_POLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial_POL"-------
    for thisComponent in trial_POLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trial_ansPOL.keys in ['', [], None]:  # No response was made
       trial_ansPOL.keys=None
       # was no response the correct answer?!
       if str(ans_POL).lower() == 'none': trial_ansPOL.corr = 1  # correct non-response
       else: trial_ansPOL.corr = 0  # failed to respond (incorrectly)
    # store data for trials_PL (TrialHandler)
    trials_PL.addData('trial_ansPOL.keys',trial_ansPOL.keys)
    trials_PL.addData('trial_ansPOL.corr', trial_ansPOL.corr)
    if trial_ansPOL.keys != None:  # we had a response
        trials_PL.addData('trial_ansPOL.rt', trial_ansPOL.rt)
    # the Routine "trial_POL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_PL'


#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(thankyou)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyou* updates
    if t >= 0.0 and thankyou.status == NOT_STARTED:
        # keep track of start time/frame for later
        thankyou.tStart = t  # underestimates by a little under one frame
        thankyou.frameNStart = frameN  # exact frame index
        thankyou.setAutoDraw(True)
    if thankyou.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        thankyou.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
