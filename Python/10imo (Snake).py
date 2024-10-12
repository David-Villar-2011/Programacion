import pygame, sys, time, random

pygame.init()

play_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("EL JUEGO DE LA SNAKE")

font = pygame.font.Font(None,30)

fps = pygame.time.Clock()

def food():
    random_pos = random.randint(0,49)*10
    food_pos = [random_pos, random_pos]
    return food_pos

def main():

    snake_pos = [100, 50]
    snake_body = [[100,50], [90,50], [80,50]]
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0
    level = 1
    Tlevel = "Level"
    Tscore = "Score"


    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        if change == "RIGHT":
            snake_pos[0] += 10
        if change == "LEFT":
            snake_pos[0] -= 10
        if change == "UP":
            snake_pos[1] -= 10
        if change == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0,list(snake_pos))
        if snake_pos == food_pos:
            food_pos = food()
            score +=1
        else:
            snake_body.pop()
        

        play_surface.fill(("cadetblue4"))
        for pos in snake_body:
            pygame.draw.rect(play_surface,("chartreuse1"), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (169,6,6), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        text = font.render(str(score),0,("black"))

        text2 = font.render(str(level),0,("black"))
        play_surface.blit(text2, (100,30))

        text3 = font.render(str(Tlevel),0,("black"))
        play_surface.blit(text3, (30,30))

        text4 = font.render(str(Tscore),0,("black"))
        play_surface.blit(text4, (380,30))

        play_surface.blit(text, (450,30))

        if score < 10:
            fps.tick(10)

        if score >= 10:
            fps.tick(20)
            level = 2
            score = 0
            

        pygame.display.flip()
        
main()

pygame.quit()
