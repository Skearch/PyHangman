import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FPS = 60

hangman_images = [pygame.image.load(f'images/{i}.png') for i in range(1, 8)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman | A group 6 original")
clock = pygame.time.Clock()

word_list = ["qwertyuiop"]
word = random.choice(word_list).upper()
guessed_letters = set()
wrong_attempts = 0

font = pygame.font.Font(None, 36)

def display_word():
    displayed_word = ""
    for letter in word:
        displayed_word += letter + " " if letter in guessed_letters else "_ "
    return displayed_word

def game_over(message):
    game_over_text = font.render(message, True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def draw_hangman():
    current_image_url = f'images/{wrong_attempts + 1}.png' if wrong_attempts < len(hangman_images) - 1 else 'images/7.png'
    scaled_image = pygame.transform.scale(hangman_images[wrong_attempts], (WIDTH, HEIGHT))
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

    if set(word) <= guessed_letters:
        game_over("You won!")

    if wrong_attempts >= 6:
        game_over("Game Over! The word was: " + word)

    pygame.display.flip()
    clock.tick(FPS)
