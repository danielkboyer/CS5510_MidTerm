import sys
import gym
# from gym.envs.classic_control.cartpole import CartPoleEnv
from cartpole import CartPoleEnv

import numpy as np
# from simple_plotter import Plotter
import matplotlib.pyplot as plt


class SingleValuePID():
    def __init__(self, expect_value, kp, ki, kd):
        self.expect_value = expect_value
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_delta = 0
        self.integral_delta = 0

    def output(self, actual_value):
        delta = self.expect_value - actual_value

        p_comp = delta * self.kp
        self.integral_delta += delta
        i_comp = self.integral_delta * self.ki
        d_comp = (delta - self.prev_delta) * self.kd
        self.prev_delta = delta
        output = p_comp + i_comp + d_comp
        return output


class SolverPID():
    def __init__(self, expect_position, expect_angle,
            kp_position, ki_position, kd_position,
            kp_angle, ki_angle, kd_angle):
        self.position_pid = SingleValuePID(expect_position,
            kp_position, ki_position, kd_position)
        self.angle_pid = SingleValuePID(expect_angle,
            kp_angle, ki_angle, kd_angle)

    def choose(self, state):
        position = state[0]
        velocity = state[1]
        angle = state[2]
        pole_velocity = state[3]

        print(("position", position))
        print(("velocity", velocity))
        print(("angle", angle))
        print(("pole_velocity", pole_velocity))

        #action = np.random.randint(2)
        
        pos_output = self.position_pid.output(position)
        angle_output = self.angle_pid.output(angle)
        action = 1 if (angle_output + pos_output) < 0 else 0
        
        print(action)
        return action


if __name__ == "__main__":
    '''
    https://github.com/openai/gym/blob/master/gym/envs/__init__.py
    register(
        id='CartPole-v1',
        entry_point='gym.envs.classic_control:CartPoleEnv',
        max_episode_steps=500,
        reward_threshold=475.0,
    )
    '''
    # env = gym.make("CartPole-v1")
    env = CartPoleEnv()

    print(env.action_space)
    print(env.observation_space)
    print(env.observation_space.low)
    print(env.observation_space.high)

    state = env.reset()
    done = False
    total_reward = 0

    input_value = float(1000)#100)#sys.argv[1])
    print(input_value)

    # (2, 0, 50)
    kp_position = 0
    ki_position = 0
    kd_position = 0
    
    # (-8, 0, -100)
    kp_angle = 5
    ki_angle = 0
    kd_angle = input_value

    algo = SolverPID(0, 0,
        kp_position, ki_position, kd_position,
        kp_angle, ki_angle, kd_angle)

    # plotter = Plotter()
    data = [[],[],[],[]]
    time_steps = []
    time = 0
    while (not done):
        env.render()

        action = algo.choose(state)
        data[0].append(state[0])
        data[1].append(state[1])
        data[2].append(state[2])
        data[3].append(state[3])
        time_steps.append(time)
        time += 1
        new_state, reward, done, _ = env.step(action)

        state = new_state
        total_reward += reward


    env.close()
    
    # plt.figure(figsize=(14,6))
    figure, axis = plt.subplots(2, 1)
    axis[0].plot(time_steps, data[0][:], "b")
    axis[0].plot(time_steps, data[1][:], "r")
    axis[1].plot(time_steps, data[2][:], "g")
    axis[1].plot(time_steps, data[2][:], "y")
    
    axis[0].legend(['position','velocity'])
    
    axis[1].legend(['angle', 'pole_velocity'])


    plt.plot()
    print(("total reward = ", total_reward))