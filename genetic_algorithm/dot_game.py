import pygame
import random
import neat
import os
import time

WIN_WIDTH = 600
WIN_HEIGHT = 700
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 50)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Dot dead game")
generation = 0


class Dot():
    def __init__(self, x, y, end):
        self.x = x
        self.y = y
        self.vel = 8
        self.end = end

    def draw(self, win):
        if not self.end:
            pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 5)
            pygame.draw.circle(win, (255, 200, 250), (self.x, self.y), 4)

        else:
            pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), 10)
            pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), 8)

    def move_up(self):
        self.y -= self.vel

    def move_down(self):
        self.y += self.vel

    def move_left(self):
        self.x -= self.vel

    def move_right(self):
        self.x += self.vel


class Obstacle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lenght = WIN_WIDTH-200
        self.width = 30

    def draw(self, win):
        pygame.draw.rect(win, (17, 18, 92),
                         (self.x, self.y, self.lenght, self.width))


def manual_movement(keys, dot, obstacle):
    if (keys[pygame.K_DOWN] and dot.y < WIN_HEIGHT):
        if not (dot.y > obstacle.y - 15 and dot.y < obstacle.y + obstacle.width and dot.x < obstacle.x+obstacle.lenght):
            dot.y += dot.vel
    if (keys[pygame.K_UP] and dot.y > 0):
        if not (dot.y < obstacle.y + obstacle.width + 15 and dot.y > obstacle.y and dot.x < obstacle.x+obstacle.lenght):
            dot.y -= dot.vel
    if (keys[pygame.K_RIGHT] and dot.x < WIN_WIDTH):
        dot.x += dot.vel
    if (keys[pygame.K_LEFT]and dot.x > 0):
        dot.x -= dot.vel


def draw_all(win, dots, dot_end, obstacle, number_dots, generation):
    win.fill([105, 167, 209])
    text = FONT.render("Dot Game", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 6))
    text_dots = FONT.render("Nº: " + str(number_dots), 1, (255, 0, 0))
    win.blit(text_dots, (WIN_WIDTH - 10 - text.get_width(), 50))
    text_gen = FONT.render("Gen: " + str(generation), 1, (255, 120, 20))
    win.blit(text_gen, (WIN_WIDTH - 10 - text.get_width(), 100))
    for dot in dots:
        dot.draw(win)
    dot_end.draw(win)
    obstacle.draw(win)
    pygame.display.update()


def eval_genomes(genomes, config):
    # get the global variables to store the generation number and pygame win
    global win, generation
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
    number_dots = 0

    # I create all the dots to train:
    for genome_id, genome in genomes:
        genome.fitness = 0  # Start the fitnes functions in 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        dots.append(Dot(120, 120, False))
        gen.append(genome)
        number_dots += 1

    # The end of the game is reach dot_end:
    dot_end = Dot(300, 600, True)
    # Aboiding the obstacle
    obstacle = Obstacle(0,  WIN_HEIGHT/2)
    # I start the game to train the generations:
    clock = pygame.time.Clock()
    # If they speend to much time I kill them
    start_time = time.time()
    run = True
    while (run and len(dots)):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
        # keys = pygame.key.get_pressed()  # check the diferent letters of the key board
        # If I want to move it manually:
        # manual_movement (keys, dots[1], obstacle)

        # First I give fitness for been alive:
        # give each bird a fitness of 0.1 for each frame it stays alive
        zones = WIN_HEIGHT/7

        for index, dot in enumerate(dots):
            reward = int(dot.y/zones)
            gen[index].fitness += 0.1*reward
            # send dot x,y and dot_end location and determine from network whether to jump or not
            output_1 = nets[dots.index(dot)].activate(
                (dot.x, dot.y, dot_end.y))
            output_2 = nets[dots.index(dot)].activate(
                (dot.x, dot.y, dot_end.x))

            # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
            if not output_1[0] > 0.5:
                dot.move_down()
            if output_2[0] > 0.5:
                dot.move_left()
            else:
                dot.move_right()

            # if output[1] > 0.5:
            #    dot.move_down()
            # if output[2] > 0.5:
            #    dot.move_left()
            # if output[3] > 0.5:
            #    dot.move_right()

        corner_x = obstacle.x + obstacle.lenght
        # corner_y=obstacle
        # Check for colisions:
        for index, dot in enumerate(dots):
            kill_dot = False
            # Chech the limits of the screen:
            if (dot.y > WIN_HEIGHT or dot.y < 0 or dot.x > WIN_WIDTH):
                kill_dot = True
            if (dot.y > obstacle.y and dot.y < obstacle.y + obstacle.width +15 and dot.x < obstacle.x+obstacle.lenght):
                kill_dot = True

            # if (dot.y < obstacle.y + obstacle.width + 15 and dot.y > obstacle.y and dot.x < obstacle.x+obstacle.lenght):

            if (time.time()-start_time >= 3):
                gen[dots.index(dot)].fitness -= 40
                kill_dot = True
            if kill_dot:
                gen[dots.index(dot)].fitness -= 10
                nets.pop(dots.index(dot))
                gen.pop(dots.index(dot))
                dots.pop(dots.index(dot))
                number_dots -= 1
            # If there is any collision I kill the birds
        draw_all(win, dots, dot_end, obstacle, number_dots, generation)


def run(config_file):
    """
    runs the NEAT algorithm to train a neural network.
    :param config_file: location of config file
    :return: None
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
    winner = p.run(eval_genomes, 200)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
