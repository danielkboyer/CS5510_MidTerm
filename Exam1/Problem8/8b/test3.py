# this will by a matplot lib program simulating a robot folling an A* path

import matplotlib.pyplot as plt
import numpy as np

import DichjstraPlanner as Dijkstra

show_animation =True


def main():
    print(__file__ + " start!!")

    # start and goal position
    sx = 10.0  # [m]
    sy = 10.0  # [m]
    gx = 50.0  # [m]
    gy = 50.0  # [m]
    grid_size = 2.0  # [m]
    robot_radius = 1.0  # [m]

    # set obstacle positions
    ox, oy = [], []
    for i in range(-10, 60):
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60):
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 61):
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 61):
        ox.append(-10.0)
        oy.append(i)
    for i in range(-10, 40):
        ox.append(20.0)
        oy.append(i)
    for i in range(0, 40):
        ox.append(40.0)
        oy.append(60.0 - i)

    if show_animation:  # pragma: no cover
        plt.plot(ox, oy, ".k")
        plt.plot(sx, sy, "og")
        plt.plot(gx, gy, "xb")
        plt.grid(True)
        plt.axis("equal")


    # A star planner
    # time the execution of the algorithm

    # a_star = AStar.AStarPlanner(ox, oy, grid_size, robot_radius)
    # rx, ry = a_star.planning(sx, sy, gx, gy)
    
    
    dijk_star = Dijkstra.Dijkstra(ox, oy, grid_size, robot_radius)
    rx, ry = dijk_star.planning(sx, sy, gx, gy)


    if show_animation:  # pragma: no cover
        plt.clf()
        
        plt.plot(ox, oy, ".k")
        plt.plot(sx, sy, "og")
        plt.plot(gx, gy, "xb")
        
        plt.plot(rx, ry, "-r")
   
        # plt.legend(['walls','Start Point','End Point',("A*: ",round_to_3_decimal_places(time_a_star), ' sec'),("Dijkstra: ",round_to_3_decimal_places(time_dichj), ' sec'),("RRT*: ",round_to_3_decimal_places(time_rrt), ' sec')], loc='lower right')
        
        plt.grid(True)
        plt.axis("equal")

        plt.title("A* vs Dijkstra vs RRT*")
        plt.pause(0.001)
        plt.show()
        
    
        
    plt.show()
        

if __name__ == '__main__':
    main()