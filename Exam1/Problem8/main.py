"""

A* grid planning

author: Atsushi Sakai(@Atsushi_twi)
        Nikos Kanargias (nkana@tee.gr)

See Wikipedia article (https://en.wikipedia.org/wiki/A*_search_algorithm)

"""

show_animation = True

import AStarPlanner as AStar
import DichjstraPlanner as Dichjstra
import RRTPlanner as RRT

import time

import math

import matplotlib.pyplot as plt

# this function takes a float and returns a string with the number rounded to 3 decimal places
def round_to_3_decimal_places(num):
    return "{:.3f}".format(num)


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
    start = time.time()
    a_star = AStar.AStarPlanner(ox, oy, grid_size, robot_radius)
    rx, ry = a_star.planning(sx, sy, gx, gy)
    end = time.time()
    time_a_star = end - start  
    
    # Dichjstra Planner
        # time the execution of the algorithm
    start = time.time()
    dich_star = Dichjstra.Dijkstra(ox, oy, grid_size, robot_radius)
    rx2, ry2 = dich_star.planning(sx, sy, gx, gy)
    end = time.time()
    time_dichj = end - start  
    
    # RRT* Planner
    # pair x y into a obstacleList of tuples
    obstacleList =[]
    for i in range(len(ox)):
        obstacleList.append((ox[i], oy[i],5))

    # time the execution of the algorithm
    start = time.time()
    rrt_star = RRT.RRT(
        start=[sx, sy],
        goal=[gx, gy],
        rand_area=[-10, 60],
        obstacle_list=obstacleList,
        # play_area=[0, 10, 0, 14]
        )
    path = rrt_star.planning(False)
    end = time.time()
    time_rrt = end - start  
    
    # brake up path array into x and y arrays
    rx3 ,ry3 = [], []
    for i in range(len(path)):
        rx3.append(path[i][0]) 
        ry3.append(path[i][1])

    if show_animation:  # pragma: no cover
        plt.clf()
        
        plt.plot(ox, oy, ".k")
        plt.plot(sx, sy, "og")
        plt.plot(gx, gy, "xb")
        
        plt.plot(rx, ry, "-r")
        plt.plot(rx2, ry2, "-b")
        plt.plot(rx3, ry3, "-g")
        plt.legend(['walls','Start Point','End Point',("A*: ",round_to_3_decimal_places(time_a_star), ' sec'),("Dijkstra: ",round_to_3_decimal_places(time_dichj), ' sec'),("RRT*: ",round_to_3_decimal_places(time_rrt), ' sec')], loc='lower right')
        
        plt.grid(True)
        plt.axis("equal")

        plt.title("A* vs Dijkstra vs RRT*")
        plt.pause(0.001)
        plt.show()
        


if __name__ == '__main__':
    main()