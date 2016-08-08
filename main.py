import ugfx
import buttons
import pyb

ugfx.init()
ugfx.text(5, 5, 'Hello world!', ugfx.RED)
accel = pyb.Accel()

while(True):
    x = accel.x()
    y = accel.y()
    z = accel.z()
    ugfx.text(5, 5, str(x), ugfx.RED)
    ugfx.text(100, 5, str(y), ugfx.GREEN)
    ugfx.text(200, 5, str(z), ugfx.BLUE)