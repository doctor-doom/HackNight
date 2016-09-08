# Sense Hat
from sense_hat import SenseHat
import time
sense = SenseHat()
sense.set_rotation(180) # Rotate LED matrix 
blue = (0,0,255) # RGB Color
# Scrolling Text 
try:
    while True:
        temp = sense.get_temperature_from_humidity()
        temp = (temp * 1.8) + 20
        temp = round(temp, 1)
        temp1 = str(temp)
        mytime = time.ctime()
        sense.show_message(+mytime + ' and ' + temp1 + '*F', text_colour=blue)
        time.sleep(30)
    except KeyboardInterrupt:
# When user escapes (ctrl-c) it clears screen and exits    
        sense.clear()
        pass
