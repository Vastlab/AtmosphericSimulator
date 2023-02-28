from VASTsimulator.sim_wrapper import SimWrapper
import matplotlib.pyplot as plt


data_path = 'add data path'
sim = SimWrapper(data_path)
x = plt.imread('./sample.jpg')
li = sim.simulate(x)
sim.save()
