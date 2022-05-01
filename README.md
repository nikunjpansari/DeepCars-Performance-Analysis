# DeepCars-Performance-Analysis
DeepCars is a highway-based simulation environment designed by [Majid Moghadam](https://github.com/MajidMoghadam2006) using pygame with the aim of analysing the effect of Deep reinforcement based learning algorithms like [DQN (Deep Q- learning)](https://arxiv.org/abs/1312.5602) & [DDQN (Double Q-learning)](https://arxiv.org/abs/1509.06461) on the DeepCars environment.<br/>

- Main objective is to minimise the no of collisons due to changing lanes.<br/>
- It was designed keep in view the grid-world scenario of reward-penalty criteria for maximising the long-term expected reward.<br/>

## State & Action Space
Discrete state and action space are required to effectively formalise the problem into an MDP.Three actions are defined namely left,stay or right i.e. be in the same lane or change the lane. While states represent the occupancy grid of the environment at an instant of time.

## Implementation
If there is a collison due to lane change then *Cars hit* score will increment by 1 everytime.While *Cars passed* score denote the no of cars paased while execution in DeepCars environment for a certain no of episodes.

## Performance Analysis
The *DeepCars* pygame environment was being tested against **DQN** & **DDQN** on different two different Intel processors (CPU environment) namely [Intel Core i7 - 11700](https://ark.intel.com/content/www/us/en/ark/products/212279/intel-core-i711700-processor-16m-cache-up-to-4-90-ghz.html) & [Intel Core i7 - 6500U](https://ark.intel.com/content/www/us/en/ark/products/88194/intel-core-i76500u-processor-4m-cache-up-to-3-10-ghz.html) to analyse its performance on the following metric :

-> Power Dissipation [(*Core Power*)](https://github.com/nanley/powertop) <br/>
-> Energy Consumption [(*CPU Energy - Core,Uncore*)](https://github.com/sosy-lab/cpu-energy-meter) <br/>
-> Temperature [(*Core temperature*)](https://github.com/openhardwaremonitor) <br/>


## Inference of performance analysis
DDQN was better than DQN in terms of performance metrics like energy consumption, and power dissipation in most of the cases, but in terms of temperature,DQN performed better than DDQN since DDQN consists of two neural networks thus it leads to an increase in temperature of the core in the processors.


### Acknowledgement
[*A Hierarchical Architecture for Sequential Decision-Making in Autonomous Driving using Deep Reinforcement Learning*](https://arxiv.org/abs/1906.08464)
