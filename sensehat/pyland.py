from sense_hat import SenseHat
import time
sense = SenseHat()
sense.set_rotation(180)
red = (255,0,0)
blue = (0,0,255)
try:
    while True:
        temp = sense.get_temperature_from_humidity()
        temp = (temp * 1.8) + 20
        temp = round(temp, 1)
        temp1 = str(temp)
        textscroll="Welcome to PyLand   :) "
        mytime = time.ctime()
        sense.show_message(textscroll, text_colour=blue)
        #sense.show_message('temp', text_colour=red)
        sense.show_message(temp1+'*F '+mytime)
        time.sleep(30)
    except KeyboardInterrupt:
        #sense.show_message("")
        sense.clear()
        pass
