# MIDI Delay

## Intro 
Inspired by Alfonso Peduto's delayed piano programming, I wanted to try to do it myself. 

It's overall pretty simple -- basically each note from the piano is sent to the computer, $n$ number of repeats are generated and sent back for the piano to play. Each repeat has to be put on a separate thread to make sure chords still work.

Even though creating the delay is not too complicated, learning how to play with it is much more difficult 🤣

## How It Works

1. **MIDI Input**: The program listens for MIDI input from a connected piano or keyboard.
2. **Note Processing**: Each note is captured and processed to generate delayed repetitions.
3. **Threading**: Each delayed note is assigned to a separate thread to ensure chords and overall polyphony is preserved.
4. **MIDI Output**: The delayed notes are sent back to the piano for playback.

## Features

- Configurable delay time and number of repeats.
- Supports polyphonic playback with accurate timing.
- Lightweight and efficient threading model.

## Requirements

- A MIDI-compatible piano or keyboard.
- Python 3.x installed on your system.
- `mido` and `python-rtmidi` libraries for MIDI handling.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/midi_delay.git
    cd midi_delay
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the program with:
```bash
python midi_delay.py
```

Adjust the delay settings in the configuration file or directly in the script.

# TODO

Intending on adding a few more files and delay types, like one that has a infinite loop after you play a note to model some canon-like piece. 

## Acknowledgments

Special thanks to Alfonso Peduto for the inspiration behind this project.
