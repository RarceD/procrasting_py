import pygame
import time
import math
import random
import neat
import os
import pymunk

WIN_HEIGHT = 600
WIN_WIDTH = 400
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Try to Balance")
generation = 0


class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lenght = 80
        self.width = 30

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0),
                         (self.x, self.y, self.lenght, self.width))
        pygame.draw.rect(win, (24, 111, 217),
                         (self.x+5, self.y+5, self.lenght-10, self.width-10))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y  # current position
        self.vel = 8
        self.jump_counter = 20
        self.num = 1
        self.direction = 1
        self.see_platform = 2

    def move(self, platforms):
        self.y += self.vel * self.direction
        self.jump_counter -= 1
        # If is in the bottom of the screen it jumps and reestart
        if (self.y > WIN_HEIGHT-20 or self.colision(platforms)):
            self.direction = -1
            self.jump_counter = 20
        if (self.jump_counter < 0):  # If is on the
            self.direction = 1
            self.jump_counter = 20
        if (self.y < 0):
            self.y = WIN_HEIGHT

    def colision(self, platforms):
        for platform in platforms:
            if (self.x > platform.x and self.x < platform.x+platform.lenght):
                if (self.y > platform.y-platform.width and self.y < platform.y+50):
                    return True
        return False

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (int(self.x), int(self.y)), 20)
        pygame.draw.circle(win, (150, 17, 133), (int(self.x), int(self.y)), 15)

    def move_right(self):
        if (self.x < WIN_WIDTH-20):
            self.x += self.vel

    def move_left(self):
        if (self.x > 20):
            self.x += -self.vel


def draw_all(win,  balls, platforms, time, max_height, generation):
    win.fill([105, 167, 209])
    text = FONT.render("Pole Play - RarceD", 1, (11, 0, 107))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    text_time = FONT.render("Time: " + str(time) + "s", 1, (11, 0, 107))
    win.blit(text_time, (10, 5))
    text_height = FONT.render(
        str(WIN_HEIGHT-max_height) + " m", 1, (11, 0, 107))
    win.blit(text_height, (10, 25))
    text_gen = FONT.render("Gen: " + str(generation), 1, (221, 0, 107))
    win.blit(text_gen, (10, 45))

    for ball in balls:
        ball.draw(win)
        pygame.draw.line(win, (0, 0, 0), (ball.x, ball.y),
                         (platforms[ball.see_platform ].x, platforms[ball.see_platform ].y), 2)

    for platform in platforms:
        platform.draw(win)
    pygame.display.update()


def manual_movement(keys, ball):
    if (keys[pygame.K_RIGHT]):
        ball.move_right()
    if (keys[pygame.K_LEFT]):
        ball.move_left()


def eval_genomes(genomes, config):
    # get the global variables to store the generation number and pygame win
    global WIN, generation
    generation += 1
    """
    I create the list holding:
        Genomes gen[]
        Neural Network asociate nets[]
        Dot to play dots[]
    """
    gen = []
    nets = []
    dots = []
    balls = []

    # I create all the balls to train:
    for genome_id, genome in genomes:
        genome.fitness = 0  # Start the fitnes functions in 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        # generate the balls in random places
        balls.append(Ball(random.randint(WIN_WIDTH/2, WIN_WIDTH-50),
                          random.randint(WIN_HEIGHT - 50 - 20, WIN_HEIGHT - 50)))
        gen.append(genome)

    # I create the platforms:
    plat_pos_y = WIN_HEIGHT/3
    platforms = []
    platforms.append(Platform(50, plat_pos_y))
    platforms.append(Platform(WIN_WIDTH/2+10, plat_pos_y * 2-50))
    platforms.append(Platform(50, plat_pos_y * 3 - 100))
    # A variable to measure the max jump
    max_height = WIN_HEIGHT
    # I start the game to train the generations:
    clock = pygame.time.Clock()
    # If they spend to much time I kill them
    start_time = time.time()

    run = True
    time_check_fitness = 1
    while (run):
        clock.tick(30)  # Every second it run 30 times
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        for index, ball in enumerate(balls):
            reward_platform = False
            if (ball.x < WIN_WIDTH/2 - 100):
                reward_platform = True
                ball.see_platform = 1
            else:
                ball.see_platform = 2

            # There are 4 inputs, distances to the nearest platform and their own x and y
            distance_x = abs(platforms[ball.see_platform].x-ball.x)
            distance_y = abs(platforms[ball.see_platform].y-ball.y)
            output = nets[index].activate(
                (distance_x, distance_y))
            # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
            if (output[0] > 0.5):
                ball.move_left()
            if (output[1] > 0.5):
                ball.move_right()
            ball.move(platforms)
            if (max_height > ball.y):
                max_height = ball.y
            # I fitness every second
            if (time.time()-start_time >= time_check_fitness):
                gen[index].fitness += max_height/1000.0
                if (reward_platform):
                    gen[index].fitness += 10.0
                time_check_fitness += 1
            if (time.time()-start_time >= 4):
                run = False
        draw_all(WIN, balls, platforms, ' %.2f' %
                 (time.time() - start_time), max_height, generation)


def run(config_file):
    """
    runs the NEAT algorithm to train a neural network to move a fucking dot
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)
    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5))
    # Run for up to 50 generations.
    winner = p.run(eval_genomes, 50)
    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))
    print("HOLA")


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
    print("HOLA")
    print("HOLA")
