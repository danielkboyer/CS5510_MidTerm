# https://pythonspot.com/maze-in-pygame/
# https://stackoverflow.com/a/37789923/9555123


# import os
# # get CWD
# cwd = os.getcwd()
# import sys
# # insert at position 1 in the path, as 0 is the path of this file.
# sys.path.insert(1,cwd)

# import AStarPlanner as AStar
from numpy.core.fromnumeric import product
import DichjstraPlanner as Dijkstra

from matplotlib.pyplot import draw
from pygame.locals import *
import pygame
import numpy as np
 
GRID_SIZE = 44 
 
class Robot:
    def __init__(self, path,start, goal):
        self.robot_radius = GRID_SIZE/2
        # curreent goal
        self.x = start[0]
        self.y = start[1]
        self.goal = goal
        self.path = path
        self.curr_goal = 0
        self.width = 33
        self.long = 40
        self.alpha = -np.pi/6
        self.R = 4/np.tan(self.alpha)
        self.Vf = 1
        self.Vs = 0
        # self.Psi_dot = (self.V * np.tan(self.alpha)) / self.L
        self.psi = 0
        self.history = []
        
    # def angle_between(self, p1, p2):
    #     ang1 = np.arctan2(*p1[::-1])
    #     ang2 = np.arctan2(*p2[::-1])
    #     return (ang1 - ang2) % (2 * np.pi)
    
    def draw(self, display_surf):
        # psi =  self.psi + self.Psi_dot 
        # self.x +=  -self.V  *np.sin(psi) 
        # self.y +=  self.V * np.cos(psi) 
        
        pygame.draw.line(display_surf, (0,0,255), (self.x, self.y), (self.goal[0], self.goal[1]))
        
        line_scale = 5000
        pygame.draw.line(display_surf, (0,255,0), (self.x, self.y), (self.x + line_scale*np.cos(self.psi), self.y + line_scale*np.sin(self.psi)))
        
        
        # update alpha to turn twards the goal point
        alpha = np.arctan2(self.goal[1] - self.y, self.goal[0] - self.x) 

        line_scale = 500
        pygame.draw.line(display_surf, (255,255,0), (self.x, self.y), (self.x + line_scale*np.cos(alpha), self.y + line_scale*np.sin(alpha)))

        Psi_dot =(alpha - self.psi ) # (self.Vf * np.tan(alpha)) / self.width
        
        self.psi += Psi_dot* 1.0001 #*(1/60)

        # if the distance to the goal is less than the radius of the robot
        if np.sqrt((self.goal[0] - self.x)**2 + (self.goal[1] - self.y)**2) < self.robot_radius:
            # if the current goal is the last goal
            if self.curr_goal == ((len(self.path[0])-1)): 
                # self.curr_goal = len(self.path) - 1
                self.x =  0
                self.y =  0
                self.curr_goal = -1
                self.history = []
                self.goal = (self.path[0][self.curr_goal], self.path[1][self.curr_goal] )
                return
            else:
                self.curr_goal += 1
                self.goal = (self.path[0][self.curr_goal], self.path[1][self.curr_goal] )

        # # this model is from http://wseas.us/e-library/conferences/2008/uk/ISPRA/ispra-08.pdf
        # # x&=VF cosφ−VS sinφ
        # # y&=VF sinφ+VS cosφ
        self.x +=  self.Vf * np.cos(self.psi) 
        self.y +=  self.Vf * np.sin(self.psi)
        
        self.history.append((self.x, self.y))    
        # draw your history line path
        for i in range(len(self.history) - 1):
            pygame.draw.line(display_surf, (255,255,255), self.history[i], self.history[i+1])
        
        # print('[',self.x,self.y,']')

        # # draw goal
        pygame.draw.circle(display_surf, (255, 0, 0), (int(self.goal[0]), int(self.goal[1])), self.robot_radius/2)
        
        # create a triangle serface
        pygame.draw.polygon(display_surf, (255,255,255), (
            (int(self.x + self.robot_radius*np.cos(self.psi)), int(self.y + self.robot_radius*np.sin(self.psi))), 
            (int(self.x + self.robot_radius*np.cos(self.psi + np.pi/2)), int(self.y + self.robot_radius*np.sin(self.psi + np.pi/2))),
            (int(self.x + self.robot_radius*np.cos(self.psi - np.pi/2)), int(self.y + self.robot_radius*np.sin(self.psi - np.pi/2))),
            # (int(self.x), int(self.y)), 
            ))
        
        
        # # draw path
    
        
    
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed
 
class Maze:
    def __init__(self):
       self.M = 49
       self.N = 17
       self.map_mat = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,
                    1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,
                    1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,
                    1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,
                    1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,
                    1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,
                    1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,
                    1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,
                    1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,
                    1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,
                    1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,
                    1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,
                    1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,
                    1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,
                    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
       


    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
            if self.map_mat[ bx + (by*self.M) ] == 1:
                display_surf.blit(image_surf,( bx * GRID_SIZE , by * GRID_SIZE))
        
            bx = bx + 1
            if bx > self.M-1:
                bx = 0 
                by = by + 1

class Planner:
    def __init__(self,maze, robot_radius):
        self.m_maze = maze
        self.m_robot_radius = robot_radius
        self.start = []
        self.goal = [self.m_maze.M-2,self.m_maze.N-2]
        self.get_path([1,1],self.goal)
        
    def get_path(self,start,goal):

        bx = 0
        by = 0
        ox = []
        oy = []
        for i in range(0,self.m_maze.M * self.m_maze.N):
            # print("i: ",i," bx: ",bx," by: ",by)
            if self.m_maze.map_mat[ bx + (by*self.m_maze.M) ] == 1:
               ox.append(bx * GRID_SIZE)
               oy.append(by * GRID_SIZE)
            
            bx = bx + 1
            # bx = bx % self.m_maze.M
            
            if bx > self.m_maze.M-1:
               bx = 0 
               by = by + 1
               
            
            #    display_surf.blit(image_surf,( bx * 44 , by * 44))
        self.start = start   
        # a_star = AStar.AStarPlanner(ox, oy, GRID_SIZE, 1) #self.m_robot_radius)
        # self.rx, self.ry = a_star.planning(start[0],start[1], goal[0]*GRID_SIZE, goal[1]*GRID_SIZE)
        dijk_star = Dijkstra.Dijkstra(ox, oy, GRID_SIZE, self.m_robot_radius)
        self.rx, self.ry = dijk_star.planning(start[0],start[1], goal[0]*GRID_SIZE, goal[1]*GRID_SIZE)
        # print('self.rx',self.rx)
        # print('self.ry',self.ry)
        return [self.rx, self.ry]

    def draw(self,display_surf,path_surf):

        for i in range(0,len(self.rx)):
            display_surf.blit(path_surf,( self.rx[i] , self.ry[i]))
        


class App:
 
    
    windowWidth = 49*GRID_SIZE
    windowHeight = 17*GRID_SIZE
    robot = 0
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.maze = Maze()
        self.planner = Planner(self.maze, 1)
        self.robot = Robot(self.planner.get_path([1,1],self.planner.goal),self.planner.start,self.planner.goal)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        # make a greem serface
        self._image_surf = pygame.Surface((GRID_SIZE,GRID_SIZE),pygame.SRCALPHA)
        self._image_surf.fill((0,255,0))
        
        self._block_surf = pygame.Surface((GRID_SIZE,GRID_SIZE),pygame.SRCALPHA)
        self._block_surf.fill((255,0,0))
        
        self._path_surf = pygame.Surface((GRID_SIZE/2,GRID_SIZE/2),pygame.SRCALPHA)
        self._path_surf.fill((0,0,255))
        
        
        # self._robot_surf = pygame.Surface((GRID_SIZE,GRID_SIZE),pygame.SRCALPHA)
        # self._robot_surf.fill((0,255,250))
        
        # create a triangle serface
        # triangle  = pygame.draw.polygon(self._display_surf, color=(255, 0, 0),points=[(50, 100), (100, 50), (150, 100)])
        
        
        # self._image_surf = pygame.image.load("player.png").convert()
        # self._block_surf = pygame.image.load("block.png").convert()
 

        # if event.type == QUIT:
        #     self._running = False
        
        # # if the user clicks the mouse at a location on the screen set that to the new goal
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     # draw mouse position
        #     pygame.draw.circle(self._display_surf, (0,255,0), pos, 5)
        #     self.planner.goal = [int(pos[0]/GRID_SIZE),int(pos[1]/GRID_SIZE)]
        #     self.planner.get_path(self.robot.start,self.planner.goal)
        #     self.robot.path = self.planner.get_path(self.robot.start,self.planner.goal)
 
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.maze.draw(self._display_surf, self._block_surf)
        self.planner.draw(self._display_surf,self._path_surf)
        
        self.robot.draw(self._display_surf)
        # self._display_surf.blit(self._robot_surf,(self.robot.x,self.robot.y))
        
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            # on mouse move event draw the mouse position
            pos =pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1,0,0):
                print(pos)
                if pos[0] < 49*GRID_SIZE and pos[1] < 17*GRID_SIZE:
                    pygame.draw.circle(self._display_surf, (0,255,0), pos, 10)
                    self.planner.goal = [int(pos[0]/GRID_SIZE),int(pos[1]/GRID_SIZE)]
                    # self.planner.get_path((self.robot.x,self.robot.y),self.planner.goal)
                    self.robot.curr_goal =0
                    self.robot.path = self.planner.get_path((self.robot.x,self.robot.y),self.planner.goal)
                    
            # check if the mouse is in the maze
            if pos[0] < 49*GRID_SIZE and pos[1] < 17*GRID_SIZE:
                # draw mouse position
                pygame.draw.circle(self._display_surf, (0,255,0), pos, 5)
        
            
            if (keys[K_RIGHT]):
                self.robot.moveRight()
 
            if (keys[K_LEFT]):
                self.robot.moveLeft()
 
            if (keys[K_UP]):
                self.robot.moveUp()
 
            if (keys[K_DOWN]):
                self.robot.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
