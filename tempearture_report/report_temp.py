import microbit

def report_temperature():
    print("%s°C" % (str(microbit.temperature())))
