# MIdi-Girlfriend
The Chord Progression Generator is a Python tool that creates 8-bar chord progressions based on user moods, matching scales and chords to emotions. Options include arpeggiated chords, passing tones, and random sequences. With a vast chord library, it saves progressions as MIDI files, ideal for musicians seeking inspiration.


Thought for a couple of seconds

Chord Progression Generator
A versatile Python tool that creates 8-bar chord progressions based on user-input moods, matching scales and chords to emotions. Customize options like arpeggiated chords, passing tones, and random sequences. With a vast chord library, it saves progressions as MIDI files, ideal for musicians seeking inspiration.

Features
Mood-Based Progressions: Generates chord progressions tailored to specific moods.
Extensive Chord Library: Includes triads, seventh chords, extended chords, and more.
Customization Options:
Arpeggiated Chords: Play chords as arpeggios.
Passing Tones: Add passing tones between chords for smoother transitions.
Random Progressions: Generate random chord sequences.
MIDI File Export: Saves generated progressions as MIDI files for use in DAWs.
User-Friendly Interface: Simple command-line prompts with engaging ASCII art.
Installation
Prerequisites
Python 3.x
pip (Python package installer)
Dependencies
Install the required Python library:

bash
Copy code
pip install midiutil
Download the Script
Clone the repository or download the chord_progression_generator.py script directly.

Usage
Navigate to the Script Directory:

bash
Copy code
cd path/to/script/directory
Run the Script:

bash
Copy code
python chord_progression_generator.py
Follow the Prompts:

Enter a Mood: Input the desired mood (e.g., happy, sad, mysterious).
Customization Options:
Arpeggiation: Choose whether to arpeggiate chords (yes or no).
Passing Tones: Decide if you want passing tones between chords (yes or no).
Random Progression: Opt for a random chord progression (yes or no).
Output:

The script displays the generated 8-bar chord progression.
A MIDI file is saved to the specified folder.
Configuration
Set the Output Folder
By default, the MIDI files are saved to:

python
Copy code
folder_path = r'C:\Users\joshf\OneDrive\Desktop\CHORD GENERATOR SCRIPT\chords created'
To change the output folder, modify the folder_path variable in the script:

python
Copy code
folder_path = r'path\to\your\desired\folder'
Expand the Chord Library
You can add more chords to the chord_midi dictionary:

python
Copy code
chord_midi = {
    # Existing chords...
    'Caug': [60, 64, 68],  # Example of adding C augmented chord
    # Add more chords as needed
}
Add More Moods and Scales
Update the mood_to_scale dictionary to include more moods:

python
Copy code
mood_to_scale = {
    # Existing moods...
    'energetic': 'E Major',
    'calm': 'D Major',
    # Add more moods and corresponding scales
}
Example
plaintext
Copy code
   ___
o|* *|o
o|* *|o
o|* *|o
 \===/
  |||
  |||
  |||
  |||
___|||___
/   |||   \
/    |||    \
|     |||     |
 \   (|||)   /
  |   |||   |
/    |||    \
/     |||     \
/      |||      \
|     [===]     |
 \             /
  '.         .'
    '-------'

Enter a mood for your chord progression: happy
Do you want the chords to be arpeggiated? (yes/no): yes
Do you want to include passing tones between chords? (yes/no): yes
Do you want a random chord progression? (yes/no): no

Mood: Happy
Scale: C Major
8-Bar Chord Progression:
Bar 1: G
Bar 2: Dm
Bar 3: Em
Bar 4: Am
Bar 5: F
Bar 6: Bdim
Bar 7: C
Bar 8: Em

MIDI file saved to C:\Users\joshf\OneDrive\Desktop\CHORD GENERATOR SCRIPT\chords created\happy_chord_progression.mid
License
This project is open-source and available under the MIT License.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
