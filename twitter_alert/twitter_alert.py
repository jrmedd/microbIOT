import microbit

#create fade in and out FRAMES
FRAMES = [] #array of FRAMES
for brightness in range(10): #iterate over 10 brightness levels
    frame = "" #create a blank frame variable
    for row in range(5): #iterate over each row of LEDs
        frame += str(brightness) * 5 + ":" #set all 5 LEDs to the same brightness
    FRAMES.append(frame[0:-1]) #append frame to frame array, taking off the last colon
FRAMES += FRAMES[::-1] #put a reversed set of FRAMES on the end of that array
FRAMES = [microbit.Image(frame) for frame in FRAMES] #convert FRAMES to micro:bit images

def pulse(num_pulses):
    for i in range(num_pulses):
        microbit.display.show(FRAMES, delay=20)
    return True
