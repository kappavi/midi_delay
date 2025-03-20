import mido
import threading

# 0) Use these to check the available port names if needed:
# print(mido.get_input_names())
# print(mido.get_output_names())

# 1) open your MIDI ports and replace strings with your port names returned from above 
input_port = mido.open_input('Roland Digital Piano')
output_port = mido.open_output('Roland Digital Piano')

# 2) set the delay time (in seconds) and number of repeats
DELAY_TIME = 0.3 
NUMBER_OF_REPEATS = 1

print("MIDI delay script running. Press Ctrl+C to stop.")

def schedule_repeat(msg, delay, repeat_count):
    """
    Schedule a repeated send of msg after 'delay' seconds.
    repeat_count indicates how many times to repeat.
    """
    if repeat_count <= 0:
        return

    def send_msg():
        output_port.send(msg)
        # recrusively schedule the next repeat if any are keft
        schedule_repeat(msg, delay, repeat_count - 1)

    # need to thread these so that chords aren't processed sequentially
    timer = threading.Timer(delay, send_msg)
    timer.start()

try:
    # 3) continuously read incoming MIDI messages
    for msg in input_port:
        if msg.type in ('note_on', 'note_off'):
            # send the original message immediately
            output_port.send(msg)
            # schedule two additional repeats without blocking
            schedule_repeat(msg, DELAY_TIME, NUMBER_OF_REPEATS)

except KeyboardInterrupt:
    print("\nExiting MIDI delay script...")