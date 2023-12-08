import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 55)

word_list = ["hangman"]
selected_word = random.choice(word_list)
guessed_letters = set()

images = [pygame.image.load(f"images/{i}.png") for i in range(7)]
current_image = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in range(97, 123):
                letter = chr(event.key)
                guessed_letters.add(letter)

    win.fill(WHITE)
    win.blit(images[current_image], (50, 50))

    display_word = ""
    for char in selected_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "

    text = font.render(display_word, True, BLACK)
    win.blit(text, (250, 400))

    if all(letter in guessed_letters for letter in set(selected_word)):
        font_win = pygame.font.SysFont(None, 70)
        text_win = font_win.render("You won", True, BLACK)
        win.blit(text_win, (250, 500))
    elif current_image == 6:
        font_lose = pygame.font.SysFont(None, 70)
        text_lose = font_lose.render("You lost", True, RED)
        win.blit(text_lose, (250, 500))
    else:
        if any(letter not in selected_word for letter in guessed_letters):
            current_image += 1

    pygame.display.flip()
    pygame.time.Clock().tick(30)