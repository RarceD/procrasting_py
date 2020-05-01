# BOX2D #

## MODULES ##
The phisics engene that I use here is *pybox2d*, this library has three types of modules:
- Common: Alocation, math and settings
- Collision: Define shapes and colisions
- Dynamics: Joins and fixtures (binds a shape to a body and adds material properties such as density or friction)

## Movement and units ##
There are 3 freedom movements: 
 - X
 - Y
 - Rotation

## Memmoy and optimation ##
MKS: meter, kilometer, second -> for better performance moving objects between 0.1 and 10 meters.

RADIANS for angle, not degress
```python
    world = b2World() #alocate memmory 
    body = world.CreateBody(b2BodyDef(...)) #dynamic body or static
    joint = world.CreateJoint(b2JointDef(...))

    fixture = body.CreateFixture(b2FixtureDef(...), density)

    world.DestroyBody(body) #The destructor of the function, free() heap
    world.DestroyJoint(joint)
``` 
## Example Ground Box
1. First I have to create the world object:
```python
    world = world(gravity=(0, -9.8), doSleep=True)
```
    I set the gravity and the ability to sleep the objects that are not doing to move more.
2. Define a body with a position and use the world object to create the body.
```python
    # Define the ground body.
    groundBodyDef = b2BodyDef()
    groundBodyDef.position = (0, -10)
# Make a body fitting this definition in the world.
    groundBody = world.CreateBody(groundBodyDef)
    groundBody = b2PolygonShape(box=(50,10)) #width: 2x50, lenght: 2x10
```
3. Define fixtures with a shape, friction, density and create fixtures on the body.
```python
    # And create a fixture definition to hold the shape
    groundBoxFixture = b2FixtureDef(shape=groundBox)
    # Add the ground shape to the ground body.
    groundBody.CreateFixture(groundBoxFixture)
```
## Example Dinamic Body
1. Create the body to hold, it must be dinamic, by default they are static.
```python
    body = world.CreateDynamicBody(position=(0,4))
```
2. Create the fixture, by default density is 0
```python
    box = body.CreatePolygonFixture(box=(1,1), density=1, friction=0.3)
```
## Example Simulate Movement
1. Set the simulation timeStep = 1.0 / 60(Hz) and the number of iterations per second: vel_iters, pos_iters = 6, 2
    ```python
    world.Step(timeStep, vel_iters, pos_iters)
    ```
