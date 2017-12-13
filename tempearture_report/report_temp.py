import microbit

temperature_offset = 4 #offset in degress C

def report_temperature():
    temperature_reading = microbit.temperature() - temperature_offset
    print("%s°C" % (str(temperature_reading)))
