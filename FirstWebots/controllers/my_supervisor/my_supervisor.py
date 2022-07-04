"""my_supervisor controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Supervisor

# create the Robot instance.
# robot = Robot()
supervisor = Supervisor()

# get the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())

# a node
obstacle = supervisor.getFromDef("Obstacle")
# a field
obstacle_pos = obstacle.getField("translation")

obs_centre_pos = [-2.68744,  0.199608, -0.831638]
obs_en_router = [-2.719, 0.152944, 0.397579]
# light node
light = supervisor.getFromDef("light")
light_intensity = light.getField("pointLightIntensity")

# keyboard
keyboard = supervisor.getKeyboard()
keyboard.enable(timestep)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
obstacle_pos.setSFVec3f(obs_centre_pos)

loop_counter = 0
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    key = keyboard.getKey()
    if key == keyboard.UP:
        # 调亮灯光
        intensity = light_intensity.getSFFloat()
        light_intensity.setSFFloat(intensity + 0.1)
    elif key == keyboard.DOWN:
        # 调暗灯光
        intensity = light_intensity.getSFFloat()
        light_intensity.setSFFloat(intensity - 0.1)
    else:
        pass
    # Process sensor data here.
    
    supervisor.setLabel(1, 'Key {}'.format(key), 0.8, 0.2, 0.1, 0x00ffff, 0.4)
    
    supervisor.setLabel(2, 'Frame: {}th'.format(loop_counter),
                        0.8,0.1,0.1,0xff0000, 0.2)
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    loop_counter += 1
    
    if loop_counter == 300:
        obstacle_pos.setSFVec3f(obs_en_router)
     
# Enter here exit cleanup code.
