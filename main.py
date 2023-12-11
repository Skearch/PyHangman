#Imports
import pygame
import random
import sys

pygame.init()

#Resolution
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FPS = 60

#Hangman Images
hangman_images = [pygame.image.load(f'images/{i}.png') for i in range(1, 8)]

#Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman | A group 6 original")
clock = pygame.time.Clock()

#Words
def loadwords():
    with open('words.txt', 'r') as file:
        words = file.readlines()
        words = [word.strip().lower() for word in words]
    return words
word = random.choice(loadwords()).upper()
guessed_letters = set()
wrong_attempts = 0

#Font
font = pygame.font.Font(None, 36)

#Word Display
def display_word():
    displayed_word = ""
    for letter in word:
        displayed_word += letter + " " if letter in guessed_letters else "_ "
    return displayed_word

#Game Finish
def game_over(message):
    game_over_text = font.render(message, True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

#Drawing Hangman
def draw_hangman():
    if wrong_attempts < len(hangman_images) - 1:
        current_image_url = f'images/{wrong_attempts + 1}.png'
    else:
        current_image_url = 'images/7.png'

    scaled_image = pygame.transform.scale(pygame.image.load(current_image_url), (WIDTH, HEIGHT))
    screen.blit(scaled_image, (0, 0))

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                letter = event.unicode.upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter not in word:
                        wrong_attempts += 1

    draw_hangman()
    word_text = font.render(display_word(), True, GREEN)
    screen.blit(word_text, (WIDTH // 2 - 100, HEIGHT - 100))

#Game Codition
    if set(word) <= guessed_letters:
        game_over("You won!")

    if wrong_attempts >= 6:
        game_over("Game Over! The word was: " + word)

    pygame.display.flip()
    clock.tick(FPS)