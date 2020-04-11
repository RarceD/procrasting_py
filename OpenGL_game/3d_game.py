import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)
colors = (
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
    (0, 0, 1)
)


def return_points(i):
    points = (
        (i, -i, -i),
        (i, i, -i),
        (-i, i, -i),
        (-i, -i, -i),
        (i, -i, i),
        (i, i, i),
        (-i, -i, i),
        (-i, i, i),
    )
    return points


def Cube():
    glBegin(GL_QUADS)  # the surfaces
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])  # change the color to green
            glVertex3fv(verticies[vertex])
    glEnd()  # the surfaces

    glBegin(GL_LINES)  # define that I am going to print a line
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])  # define a vertex as it is
        for i in range(2, 4):
            for vertex in edge:
                # define a vertex as it is
                glVertex3fv(return_points(i)[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1000, 800)
    # add opengl to pygame
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # 45 degres poitn of view, 0.1 one means that the objects do not dissapear if I go far
    #the third element is the near plane and the fourth is the far plane
    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0) 
    # for visualize the cube
    glTranslatef(0, 0, -20)  # can change the perspective
    # for degrees coordenates
    glRotatef(20, 0, 0, 0)
    while True:
        # for closing the game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN):
                # Every time I press a key I change the rotation 20º in certain position
                if (event.key == pygame.K_LEFT):
                    glRotatef(20, 1, 0, 0)
                if (event.key == pygame.K_RIGHT):
                    glRotatef(20, 0, 1, 0)
                if (event.key == pygame.K_UP):
                    glRotatef(20, 0, 0, 1)
                if (event.key == pygame.K_DOWN):
                    glRotatef(20, 0, 0, -1)
                if (event.key == pygame.K_d):
                    glTranslatef(1, 0, 0)
                if (event.key == pygame.K_a):
                    glTranslatef(-1, 0, 0)
                if (event.key == pygame.K_w):
                    glTranslatef(0, 1, 0)
                if (event.key == pygame.K_s):
                    glTranslatef(0, -1, 0)
            if (event.type == pygame.MOUSEBUTTONDOWN): #catch the mouse to modified the zoom
                if (event.button == 4):
                    glTranslatef(0, 0, 1.0)
                if (event.button == 5):
                    glTranslatef(0, 0, -1.0)

        # Every frame I clear the last frame and I print new
        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
