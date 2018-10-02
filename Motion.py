from gpiozero import MotionSensor
pir = MotionSensor(4)

# Takes an input to the 4th GPIO pinout on the PI when the PIR is triggered
while True:
    pir.wait_for_motion()
    print("you moved")
    pir.wait_for_no_motion()