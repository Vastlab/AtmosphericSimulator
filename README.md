# VAST Atmospheric Simulation Module
This code is adopted from https://github.com/Riponcs/TurbulenceSimulatorPython

This repository contains the code for the following paper:

Zhiyuan Mao, Nicholas Chimitt, and Stanley H. Chan, ‘‘Accelerating Atmospheric Turbulence Simulation via Learned Phase-to-Space Transform’’, accepted to ICCV 2021

Arxiv: 
https://arxiv.org/abs/2107.11627


# Usage
```
pip install git+https://github.com/Vastlab/AtmosphericSimulator
```

```
from VASTsimulator.sim_wrapper import SimWrapper
x = plt.imread('./sample.jpg')

# init class
simclass = SimWrapper(data_path)

# simulate and return image (expects numpy of shape (112,112,3) with unnormalized pixel values from 0-255)
simulated_img_list = simclass.simulate(x)

# (OPTIONAL) save iamges
simclass.save()
```

