import microbit

while True:
    if microbit.button_a.was_pressed():
        print("BUTTON A")
    elif microbit.button_b.was_pressed():
        print("BUTTON B")
