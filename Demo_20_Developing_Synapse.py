from pyrosim import PYROSIM
import math

ARM_LENGTH = 0.5

ARM_RADIUS = ARM_LENGTH / 10.0

sim = PYROSIM(playPaused = True , evalTime = 1000, debug=False)

sim.Send_Cylinder(objectID = 0 , x=0, y=0, z=ARM_LENGTH/2.0 + 2*ARM_RADIUS, r1=0, r2=0, r3=1, length=ARM_LENGTH, radius=ARM_RADIUS)

sim.Send_Cylinder(objectID = 1 , x=0, y=ARM_LENGTH/2.0, z=ARM_LENGTH + 2*ARM_RADIUS , r1=0, r2=1, r3=0, length=ARM_LENGTH, radius=ARM_RADIUS)

sim.Send_Joint(jointID = 0, firstObjectID=0, secondObjectID=1, x=0, y=0, z=ARM_LENGTH + 2*ARM_RADIUS , n1=1, n2=0, n3=0, lo=-3.14159/4.0, hi=+3.14159/4.0)

sim.Send_Joint(jointID = 1 , firstObjectID=0, secondObjectID=-1, x=0, y=0, z=ARM_LENGTH/2.0 + 2*ARM_RADIUS)

sim.Send_Function_Neuron(neuronID=0, function=math.sin) 
sim.Send_Motor_Neuron(neuronID=1, jointID=0)

#sim.Send_Synapse(sourceNeuronID=0,targetNeuronID=1,weight=1.0)
sim.Send_Developing_Synapse(sourceNeuronID=0,targetNeuronID=1,
							startWeight=1.0, endWeight=-1.0,
							startTime=0, endTime=1.0)
sim.Start()

sim.Wait_To_Finish()
