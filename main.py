import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60

# Initialize global variables
WIN, LOST = 0, 0

# Hangman Images
hangman_images = [pygame.image.load(f'images/{i}.png') for i in range(1, 8)]

# Load words from file
def load_words():
    with open('words.txt', 'r') as file:
        words = [word.strip().lower() for word in file]
    return words

# Select a random word
def get_random_word():
    return random.choice(load_words()).upper()

# Render the score text
def render_score_text(screen, font):
    score_text = font.render(f"{WIN} - {LOST}", True, WHITE)
    screen.blit(score_text, ((WIDTH - score_text.get_width()) // 2, 50))

# Draw hangman images
def draw_hangman(screen, wrong_attempts):
    if wrong_attempts < len(hangman_images) - 1:
        current_image_url = f'images/{wrong_attempts + 1}.png'
    else:
        current_image_url = 'images/7.png'

    scaled_image = pygame.transform.scale(pygame.image.load(current_image_url), (WIDTH, HEIGHT))
    screen.blit(scaled_image, (0, 0))

# Display game over message
def game_over(screen, message, color):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render(message, True, color)
    screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)

# Main game loop
def whole_game():
    global WIN, LOST

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman | A group 6 original")
    clock = pygame.time.Clock()

    word = get_random_word().upper()
    guessed_letters = set()
    wrong_attempts = 0
    font = pygame.font.Font(None, 36)

    while True:
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

        screen.fill(WHITE)
        draw_hangman(screen, wrong_attempts)

        # Display the word
        word_text = font.render(display_word(word, guessed_letters), True, GREEN)
        screen.blit(word_text, (WIDTH // 2 - 100, HEIGHT - 100))

        # Check game conditions
        if set(word) <= guessed_letters:
            game_over(screen, "YOU WON!", GREEN)
            WIN += 1
            render_score_text(screen, font)
            return

        if wrong_attempts >= 6:
            game_over(screen, "YOU LOST.", RED)
            LOST += 1
            render_score_text(screen, font)
            return

        render_score_text(screen, font)
        pygame.display.flip()
        clock.tick(FPS)

# Display the word with guessed letters
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_ " for letter in word)

while True:
    whole_game()