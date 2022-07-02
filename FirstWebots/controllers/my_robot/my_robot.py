"""my_robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
right_motor = robot.getDevice('MotorRight')
left_motor = robot.getDevice('MotorLeft')

right_motor.setPosition(float('inf'))
left_motor.setPosition(float('inf'))

led = robot.getDevice('led')


right_motor.setVelocity(1.0)
left_motor.setVelocity(1.0)
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
ds_front = robot.getDevice('DisSensFront')
ds_front.enable(timestep)

ds_left = robot.getDevice('DisSensLeft')
ds_left.enable(timestep)

ds_right = robot.getDevice('DisSensRight')
ds_right.enable(timestep)

camera_left = robot.getDevice('CameraLeft')
camera_left.enable(timestep)

camera_right = robot.getDevice('CameraRight')
camera_right.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
loop_counter = 0
robot_state = 'run'

while robot.step(timestep) != -1:
    ds_front_value = ds_front.getValue()
    ds_right_value = ds_right.getValue()
    ds_left_value = ds_left.getValue()
    if ds_front_value < 850:
        right_motor.setVelocity(0.0)
        left_motor.setVelocity(0.0)
        led.set(1)
        if robot_state == 'run':
            camera_left.saveImage('left_img.png', quality=50)
            camera_right.saveImage('right_img.png', quality=50)
        robot_state = 'stop'
    else:
        robot_state = 'run'
        if loop_counter % 10 == 0:
            led_value = 1 if led.get() == 0 else 0
            led.set(led_value)
        if (ds_right_value - ds_left_value) > 5:
            right_motor.setVelocity(0.0)
            left_motor.setVelocity(0.5)
        elif (ds_right_value - ds_left_value) < -5:
            right_motor.setVelocity(0.5)
            left_motor.setVelocity(0.0)
        else:
            right_motor.setVelocity(1.0)
            left_motor.setVelocity(1.0)
        # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    # print('ds_front={}, ds_left={}, ds_right={}'.format(ds_front.getValue(), ds_left.getValue(), ds_right.getValue()))
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    loop_counter += 1
    pass

# Enter here exit cleanup code.
