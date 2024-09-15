import random
import os
import sys
from midiutil import MIDIFile

def display_ascii_art():
    """
    Displays the ASCII art before the user input.
    """
    ascii_art = r'''
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
    '''
    print(ascii_art)

def get_scale_for_mood(mood):
    """
    Maps the input mood to a corresponding musical scale.
    """
    mood_to_scale = {
        'happy': 'C Major',
        'joyful': 'C Major',
        'upbeat': 'C Major',
        'sad': 'A Minor',
        'melancholic': 'A Minor',
        'emotional': 'A Minor',
        'mysterious': 'D Dorian',
        'exotic': 'E Phrygian',
        'relaxed': 'F Lydian',
        'dreamy': 'G Mixolydian',
        'tense': 'B Locrian',
        'suspenseful': 'B Locrian',
        'dark and ominous': 'A Minor',
        # Add more moods and scales as needed
    }
    # Default to C Major if mood not found
    return mood_to_scale.get(mood.lower(), 'C Major')

def get_chords_for_scale(scale):
    """
    Provides a list of chords for the given scale.
    """
    scale_chords = {
        'C Major': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim', 'Cmaj7', 'D7', 'E7', 'Fmaj7', 'G7', 'Am7', 'Bm7b5'],
        'A Minor': ['Am', 'Bdim', 'C', 'Dm', 'Em', 'F', 'G', 'Am7', 'Bm7b5', 'Cmaj7', 'Dm7', 'Em7', 'Fmaj7', 'G7'],
        'D Dorian': ['Dm', 'Em', 'F', 'G', 'Am', 'Bdim', 'C', 'Dm7', 'Em7', 'Fmaj7', 'G7', 'Am7', 'Bm7b5', 'Cmaj7'],
        'E Phrygian': ['Em', 'F', 'G', 'Am', 'Bdim', 'C', 'Dm', 'Em7', 'Fmaj7', 'G7', 'Am7', 'Bm7b5', 'Cmaj7', 'Dm7'],
        'F Lydian': ['F', 'G', 'Am', 'Bdim', 'C', 'Dm', 'Em', 'Fmaj7', 'G7', 'Am7', 'Bm7b5', 'Cmaj7', 'Dm7', 'Em7'],
        'G Mixolydian': ['G', 'Am', 'Bdim', 'C', 'Dm', 'Em', 'F', 'G7', 'Am7', 'Bm7b5', 'Cmaj7', 'Dm7', 'Em7', 'Fmaj7'],
        'B Locrian': ['Bdim', 'C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bm7b5', 'Cmaj7', 'Dm7', 'Em7', 'Fmaj7', 'G7', 'Am7'],
        # Add more scales and chords as needed
    }
    return scale_chords.get(scale, scale_chords['C Major'])

# Expanded chord MIDI mapping
chord_midi = {
    # Triads
    'C': [60, 64, 67],
    'Cm': [60, 63, 67],
    'Cdim': [60, 63, 66],
    'D': [62, 66, 69],
    'Dm': [62, 65, 69],
    'Ddim': [62, 65, 68],
    'E': [64, 68, 71],
    'Em': [64, 67, 71],
    'Edim': [64, 67, 70],
    'F': [65, 69, 72],
    'Fm': [65, 68, 72],
    'Fdim': [65, 68, 71],
    'G': [67, 71, 74],
    'Gm': [67, 70, 74],
    'Gdim': [67, 70, 73],
    'A': [69, 73, 76],
    'Am': [69, 72, 76],
    'Adim': [69, 72, 75],
    'B': [71, 75, 78],
    'Bm': [71, 74, 78],
    'Bdim': [71, 74, 77],
    # Seventh Chords
    'Cmaj7': [60, 64, 67, 71],
    'Cm7': [60, 63, 67, 70],
    'C7': [60, 64, 67, 70],
    'Cdim7': [60, 63, 66, 69],
    'Cm7b5': [60, 63, 66, 70],
    'Dmaj7': [62, 66, 69, 73],
    'Dm7': [62, 65, 69, 72],
    'D7': [62, 66, 69, 72],
    'Ddim7': [62, 65, 68, 71],
    'Dm7b5': [62, 65, 68, 72],
    'Emaj7': [64, 68, 71, 75],
    'Em7': [64, 67, 71, 74],
    'E7': [64, 68, 71, 74],
    'Edim7': [64, 67, 70, 73],
    'Em7b5': [64, 67, 70, 74],
    'Fmaj7': [65, 69, 72, 76],
    'Fm7': [65, 68, 72, 75],
    'F7': [65, 69, 72, 75],
    'Fdim7': [65, 68, 71, 74],
    'Fm7b5': [65, 68, 71, 75],
    'Gmaj7': [67, 71, 74, 78],
    'Gm7': [67, 70, 74, 77],
    'G7': [67, 71, 74, 77],
    'Gdim7': [67, 70, 73, 76],
    'Gm7b5': [67, 70, 73, 77],
    'Amaj7': [69, 73, 76, 80],
    'Am7': [69, 72, 76, 79],
    'A7': [69, 73, 76, 79],
    'Adim7': [69, 72, 75, 78],
    'Am7b5': [69, 72, 75, 79],
    'Bmaj7': [71, 75, 78, 82],
    'Bm7': [71, 74, 78, 81],
    'B7': [71, 75, 78, 81],
    'Bdim7': [71, 74, 77, 80],
    'Bm7b5': [71, 74, 77, 81],
    # Extended Chords
    'C9': [60, 64, 67, 70, 74],
    'Cm9': [60, 63, 67, 70, 73],
    'Cmaj9': [60, 64, 67, 71, 74],
    'Cadd9': [60, 64, 67, 74],
    'Csus4': [60, 65, 67],
    'Csus2': [60, 62, 67],
    # You can add similar chords for other root notes
    # ...
}

def chord_to_midi_notes(chord):
    """
    Converts a chord name to a list of MIDI note numbers.
    """
    return chord_midi.get(chord, [])

def generate_chord_progression(chords, random_progression=False):
    """
    Generates an 8-bar chord progression using chords from the scale.
    If random_progression is True, chords are selected randomly from all available chords.
    """
    progression = []
    if random_progression:
        all_chords = list(chord_midi.keys())
        for _ in range(8):
            chord = random.choice(all_chords)
            progression.append(chord)
    else:
        for _ in range(8):
            chord = random.choice(chords)
            progression.append(chord)
    return progression

def sanitize_filename(filename):
    """
    Removes or replaces characters in the filename that are invalid for the file system.
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename

def save_chord_progression_as_midi(progression, filename, arpeggiated=False, include_passing_tones=False):
    """
    Saves the chord progression as a MIDI file.
    If arpeggiated is True, chords are played as arpeggios.
    If include_passing_tones is True, adds passing tones between chords.
    """
    midi = MIDIFile(1)  # One track
    track = 0
    time = 0  # Start at the beginning
    tempo = 120  # Beats per minute
    volume = 100  # Max volume

    midi.addTempo(track, time, tempo)

    for i, chord in enumerate(progression):
        notes = chord_to_midi_notes(chord)
        if arpeggiated == 'yes':
            # Play notes sequentially within the bar
            note_duration = 1.0 / len(notes)
            for j, note in enumerate(notes):
                midi.addNote(track, 0, note, time + j * note_duration, note_duration, volume)
        else:
            # Play chord as block chord
            for note in notes:
                midi.addNote(track, 0, note, time, 1, volume)
        if include_passing_tones == 'yes' and i < len(progression) -1:
            # Add passing tone between this chord and next chord
            next_chord_notes = chord_to_midi_notes(progression[i+1])
            # Simple passing tone: choose a note that connects current chord to next chord
            if notes and next_chord_notes:
                passing_note = (notes[-1] + next_chord_notes[0]) // 2
                midi.addNote(track, 0, passing_note, time + 0.5, 0.5, volume)
        time += 1  # Move to the next bar

    with open(filename, 'wb') as output_file:
        midi.writeFile(output_file)

def main():
    display_ascii_art()
    mood = input("Enter a mood for your chord progression: ")
    # Ask the user for options
    arpeggiated = input("Do you want the chords to be arpeggiated? (yes/no): ").strip().lower()
    include_passing_tones = input("Do you want to include passing tones between chords? (yes/no): ").strip().lower()
    random_progression = input("Do you want a random chord progression? (yes/no): ").strip().lower()

    if random_progression == 'yes':
        chords = list(chord_midi.keys())
        progression = generate_chord_progression(chords, random_progression=True)
    else:
        scale = get_scale_for_mood(mood)
        chords = get_chords_for_scale(scale)
        progression = generate_chord_progression(chords)

    print(f"\nMood: {mood.capitalize()}")
    if random_progression == 'yes':
        print("Scale: Random")
    else:
        print(f"Scale: {scale}")
    print("8-Bar Chord Progression:")
    for i, chord in enumerate(progression, 1):
        print(f"Bar {i}: {chord}")

    # Define the folder path
    folder_path = r'C:\Users\joshf\OneDrive\Desktop\CHORD GENERATOR SCRIPT\chords created'

    # Check if the folder exists, create it if it doesn't
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)

    # Sanitize the mood to create a valid filename
    sanitized_mood = sanitize_filename(mood)

    midi_filename = os.path.join(folder_path, f"{sanitized_mood}_chord_progression.mid")

    save_chord_progression_as_midi(progression, midi_filename, arpeggiated, include_passing_tones)
    print(f"\nMIDI file saved to {midi_filename}")

if __name__ == "__main__":
    main()

