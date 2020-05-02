import pygame
import Box2D  # The main library
from Box2D.b2 import (world, polygonShape, staticBody, dynamicBody)

PPM = 20.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
PI = 3.141592
# --- pygame setup ---
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pole Balance')
clock = pygame.time.Clock()

# --- pybox2d world setup ---
# Create the world
world = world(gravity=(0, -9.8), doSleep=True)
# Create static body to hold the ground shape
ground_body = world.CreateStaticBody(
    position=(0, 1), shapes=polygonShape(box=(50, 5)))
# Create a dynamic body
body_1 = world.CreateDynamicBody(position=(10, 15), angle=PI/3)
body_2 = world.CreateDynamicBody(position=(10, 15), angle=PI/3)
rj = world.CreateRevoluteJoint(
    bodyA=body_1,
    bodyB=body_2,
    anchor=body_1.worldCenter,
    lowerAngle=-PI,  # -90 degrees
    upperAngle=PI,  # 45 degrees
    enableLimit=True,
    maxMotorTorque=10.0,
    motorSpeed=0.0,
    enableMotor=True,
)
# And add a box fixture onto it (with a nonzero density, so it will move)
box = body_1.CreatePolygonFixture(box=(2, 1), density=1, friction=0.3)
box2 = body_2.CreatePolygonFixture(box=(0.5, 3), density=1, friction=0.3)

colors = {
    staticBody: (3, 37, 173, 0),
    dynamicBody: (140, 7, 47, 0)
}
running = True
move_x = False
while running:
    # Check the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The user closed the window or pressed escape
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                print("zoom in")
            elif event.button == 5:
                print("zoom out")

    win.fill((138, 193, 227, 50))

    """
    for body in world.bodies:  # loop in all the bodies from the world
        for fixture in body.fixtures:
            shape = fixture.shape
            # The body gives us the position and angle of its shapes
            # I have to change the oprientation of the axes: pygame!=box2D
            vertices = [(body.transform * v) * PPM for v in shape.vertices]
            vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
            pygame.draw.polygon(win, colors[body.type], (vertices))
    """
    vertices = [(body_1.transform * v) * PPM for v in box.shape.vertices]
    vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
    pygame.draw.polygon(win,(255,0,0), (vertices))

    vertices = [(body_2.transform * v) * PPM for v in box2.shape.vertices]
    vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]
    pygame.draw.polygon(win,(0,255,0), (vertices))

    # for moving the box
    if move_x:
        body_1.position += (0.1, 0)
        move_x = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            move_x = True
    # this quantity is the times/second I get the physics calculations, fix value better
    world.Step(TIME_STEP, 10, 10)
    # Flip the screen and try to keep at the target FPS
    pygame.display.flip()
    clock.tick(TARGET_FPS)
pygame.quit()
