# SuperGrids
Algorithmic drum sequencer built on droid eurorack platform


## What is it
SuperGrids is an 8-track algorithmic sequencer focused on crafting humanized beats, through improvisation. 

What is the Droid eurorack platform? See [here](https://shop.dermannmitdermaschine.de/pages/droid-universal-cv-processor) and [here](https://www.modulargrid.net/e/der-mann-mit-der-maschine-droid) for more information. It is HIGHLY recommended that you understand what Droid is and even have read through a bit of the manual before moving forward.  


## What you need

Droid Master eurorack module + the following controllers:

- 4x p2b8 controllers
- G8 gate expander
- X7 midi expander


## How to run

- Copy this patch onto your droid sd card and title it "droid.ini" and press the only button on the Droid Master module to load the patch. You will see a bunch of colors flicker, until the patch has fully loaded.
- Press play! (the upper left-most button on the p2b8 controllers)

Note: when first running this patch, the default values for some of the underlying code (which is out of my control) are set to send out all triggers on all channels. A longpress on the "reset" button will clear this. More on this later.  


## How it works!

/Users/johnsloan/Music/droid-patches/supergrids/Screen Shot 2022-09-06 at 9.30.10 PM.png

The main idea, is that you use the selectors on the upper right side (marked select1...8) to pick which tracks you want to edit, and then use the knobs up top to change different parameters for those tracks. The parameters that the knobs up top represent change based on which mode you are in. The list of modes is as follows:

- Gates.
- Alt Gates.
- CV.
- Project.
- Groove.
- Performance.

### Transport Buttons

- Play/stop button is upper left-most button of p2b8 controllers
- Reset button is just below the play button and will always reset all 8 tracks, as well as the groove pattern, to the first beat.
- A long press on the reset button will fully clear all gates and initialize all parameters to their default values. When you want to start fresh on a new beat, this is where you start. 

### Selectors

The selectors are used to choose which tracks are currently being edited. These buttons are the 8 buttons in the upper right corner of the p2b8 controllers. When you press any single button, it will switch automatically to selecting only that track. To select multiple tracks, you can press other buttons while still holding down your initial button press. In this way, you can select any combination of the 8 tracks for simultaneous editing. 

Tip: there is a handy shortcut for selecting ALL 8 tracks with a single finger. Simply double tap any one of the 8 selector buttons.

(Tricky Tip: with a bit of practice, you can also double tap to select all but hold your finger down before releasing after the second tap, and then press other buttons. When you finally let go, your selection will invert. This will be more clear with a video demo, but is very handy for quick selections!)

When multiple tracks are selected, you will only see the values displayed for the highest track number selected. For example, the step button leds showing the current pattern will only be showing the pattern for track 6 if you have track 3,4 and 6 selected simultaneously. HOWEVER, moving pots and pressing step buttons WILL effect all selected channels. For step buttons that means it will toggle whatever state the button was in on each selected track. For pots, the values are moved relative to the current pot from where the value was previously, and it will "catch up" intelligently rather than jumping immediately to the value of the highest track number. 

### Gates Mode

This probably could be considered the "main" mode. It is where you create all of the gate patterns for each track. In this mode, the 16 bottom-half buttons of the p2b8 controllers show the step buttons for your sequence. Pressing these buttons toggles a gate at the corresponding step for any selected tracks. 

The knobs up top control the following parameters in this mode (in order of upper left to bottom right, as though you are reading a book):

#### Activity 
    Algorithmically add or subtract beats to/from your defined gate pattern.  
#### Variation
    Keeps the number of beats the same but reorders them
#### Offbeats % 
    As you turn clockwise any beats added/moved through dejavu, activity, or variation, will tend towards offbeats. As you turn counterclockwise, the beats will tend towards on beats. This will do nothing if you are not using any one of activity/variation/dejavu.  
#### Rolls 
    As you turn clockwise, more and more beats will get rolled (aka racheted).
#### Dejavu 
    As you turn clockwise, more and more beats will be moved somewhere else at random. When you return to fully CCW, it will return to the original pattern that was playing before you turned this knob.
#### Alternate bars
    Sets the number of bars before enabling the alternate steps page. The default value is 4, meaning that steps toggled in alternate steps mode will be enabled every 4 bars. 
#### Groove Attenuator / Humanization
    From fully CCW to midnight, the pot controls how much of the global groove pattern will effect the selected tracks. From midnight to fully CW, the groove will continue to be randomized more and more, adding some humanization to the tracks. By default the groove pattern will be fully engaged on all tracks.  
#### Gate Length
    Changes the length of the gate output by each selected track.

For more information on many of these parameters, check out the official Droid manual, which has more in-depth examples. Some parameters like "groove/humanization" will not be found in the Droid manual, since that was created using several underlying circuits. 

### Alternate Gates Mode

This mode is nearly identical to the "Gates Mode". The only difference is that the step buttons (i.e. the 16 bottom most buttons of the p2b8 controllers) will now be showing the alternate page. In the alternate page, pressing the step buttons toggles the value of that step every "Alternate Bars". By default "Alternate Bars" is set to 4, meaning that any toggles you add in the alternate page will occur every 4 bars. All parameters on the upper pots are the same as when in "Gates Mode".   

### CV Mode

Even though the focus of this sequencer is on drum patterns, it is actually an incredible melody sequencer as well! 



// TODO: still in progress!
