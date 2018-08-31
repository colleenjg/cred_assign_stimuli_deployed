"""
This is code to generate and run a 70-minute stimulus for 2P recordings
for mouse II
order is: bricks, gabors, bricks, gabors

Mismatches are included. These are every 30-90 seconds, and last 2-4 seconds
for the bricks, and 3-6 seconds for the Gabors

Everything is randomized for each animal, except for: ordering of stim types (gabors vs bricks), and positions and sizes of Gabors
Gabor positions and sizes are permanently hard-coded (same for all animals, forever)
Stim type ordering is the same for all animals on a given day, but can vary between days
"""

import Tkinter as tk
import tkSimpleDialog
from psychopy import monitors

# camstim is the Allen Institute stimulus package built on psychopy
from camstim import SweepStim
from camstim import Window, Warp

import stim_params_2p as stim_params

    
if __name__ == "__main__":
    
    dist = 15.0
    wid = 52.0
    
    # load and record parameters. Leave False.
    promptID = False
    # Save an extra copy of parameters under ./config
    extrasave = False
    
    # Record orientations of gabors at each sweep (LEAVE AS TRUE)
    recordOris = True

    # Record positions of squares at all times (LEAVE AS TRUE)
    recordPos = True
            
    # create a monitor
    monitor = monitors.Monitor("testMonitor", distance=dist, width=wid)

    # get animal ID and session ID
    if promptID == True: # using a prompt
        myDlg = tk.Tk()
        myDlg.withdraw()
        subj_id = tkSimpleDialog.askstring("Input", 
                                           "Subject ID (only nbrs, letters, _ ): ", 
                                           parent=myDlg)
        sess_id = tkSimpleDialog.askstring("Input", 
                                           "Session ID (only nbrs, letters, _ ): ", 
                                           parent=myDlg)
        
        if subj_id is None or sess_id is None:
            raise ValueError('No Subject and/or Session ID entered.')
    
    else: # Could also just enter it here.
        # if subj_id is left as None, will skip loading subj config.
        subj_id = None
        sess_id = None
    
    # alternatively to using animal ID, use a seed per animal.
    # Note, animal ID will override seed IF there is a config file for the animal!
    seed = 103
    
    
    # Create display window
    window = Window(fullscr=True, # Will return an error due to default size. Ignore.
                    monitor=monitor,  # Will be set to a gamma calibrated profile by MPE
                    screen=0,
                    warp=Warp.Spherical
                    )

    # initialize the simuli
    gb = stim_params.init_run_gabors(window, subj_id, sess_id, seed, extrasave, recordOris)
    sq = stim_params.init_run_squares(window, subj_id, sess_id, seed, extrasave, recordPos)

    gb_ds = [(1050, 1950), (3150, 4050)] #1 x block length for each chunk here
    sq_ds = [(0, 901), (2100,3001)] #2x block length + 1 here
    
    gb.set_display_sequence(gb_ds);
    sq.set_display_sequence(sq_ds);
        
    ss = SweepStim(window,
                   stimuli=[sq, gb],
                   pre_blank_sec=1,
                   post_blank_sec=1,
                   params={},  # will be set by MPE to work on the rig
                   )
    
    # run it
    ss.run()