import pygame
import random
from player.segment import Segment
from entities.food import Food

def main():
    pygame.init()
    screen = pygame.display.set_mode((725, 725))
    pygame.display.set_caption("Hello Snake")
    clock = pygame.time.Clock()
    running = True
    movement_delay = 10

    player = []
    food = []
    centre = (screen.get_width() / 2, screen.get_height() / 2)
    head = Segment(0, centre, "H", True)
    player.append(head)
    counter = 0
    font = pygame.font.SysFont(None, 48)
    goal = "Hello World!"
    
    current_index = 1
    key_detected = False
    food_exists = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction = (0, -1)
            key_detected = True
        elif keys[pygame.K_s]:
            direction = (0, 1)
            key_detected = True
        elif keys[pygame.K_a]:
            direction = (-1, 0)
            key_detected = True
        elif keys[pygame.K_d]:
            direction = (1, 0)
            key_detected = True

        # Update game objects
        if current_index == len(goal):
            invalid_seg = 0
            for _ in player:
                if _.get_vel()[0] == -35 and _.get_vel()[1] == 0:
                    pass
                else:
                    invalid_seg += 1
            if invalid_seg == 0:
                running = False

        counter += 1
        if counter == movement_delay:
            counter = 0
            if key_detected:
                player[0].turn(direction)
                key_detected = False
            for _ in range(1, len(player)):
                player[_].follow(player[_ - 1].echo())
            for _ in player:
                _.move()

        if not food_exists:
            if current_index != len(goal):
                new_food = Food(goal[current_index], player)
                food.append(new_food)
                food_exists = True
            else:
                pass
        if food_exists:
            if player[0].get_pos() == food[0].get_pos():
                food.clear()
                food_exists = False
                tail_pos = player[len(player) - 1].get_pos()
                tail_vel = player[len(player) - 1].get_vel()
                new_tail_pos = (tail_pos[0] - tail_vel[0], tail_pos[1] - tail_vel[1])
                new_tail = Segment(current_index, new_tail_pos, goal[current_index])
                player.append(new_tail)
                current_index += 1
        
        die = False
        for _ in range(1, len(player)):
            if player[0].get_pos() == player[_].get_pos():
                    die = True
        if player[0].get_pos()[0] < 12 or player[0].get_pos()[0] > 702:
                    die = True
        elif player[0].get_pos()[1] < 12 or player[0].get_pos()[1] > 702:
                    die = True

        if die:
            player = []
            food = []
            head = Segment(0, centre, "H", True)
            player.append(head)
            counter = 0
            
            current_index = 1
            key_detected = False
            food_exists = False
            die = False

        # Draw game objects
        screen.fill("black")
        for _ in player:
            current_seg = pygame.draw.rect(screen, "white", _.get_rect())
            char = font.render(_.get_char(), True, "black")
            screen.blit(char, current_seg)
        
        for _ in food:
            current_food = pygame.draw.rect(screen, "green", _.get_rect())
            char = font.render(_.get_char(), True, "black")
            screen.blit(char, current_food)

        # Display
        pygame.display.flip()

        clock.tick(60)

    game_over = True
    colours = ["white", "blue", "red", "green", "yellow"]
    counter = 0
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False

        counter += 1
        if counter  == 20:
            counter = 0
            for _ in player:
                seg_colour = random.choice(colours)
                current_seg = pygame.draw.rect(screen, seg_colour, _.get_rect())
                if seg_colour == "white":
                    char_colour = "black"
                elif seg_colour == "blue":
                    char_colour = "green"
                elif seg_colour == "red":
                    char_colour = "yellow"
                elif seg_colour == "green":
                    char_colour = "red"
                elif seg_colour == "yellow":
                    char_colour = "blue"
                char = font.render(_.get_char(), True, char_colour)
                screen.blit(char, current_seg)

        pygame.display.flip()
        clock.tick(60)

    def eat(player):
        tail = Segment(len(player), player[len(player) - 1].echo())
        player.append(tail)  

if __name__ == "__main__":
    main()