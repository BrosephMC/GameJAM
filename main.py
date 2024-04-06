import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 500, 700
GRID_WIDTH, GRID_HEIGHT = 6, 7
GRID_SIZE = min((WIDTH - 100) // GRID_WIDTH, (HEIGHT - 100) // GRID_HEIGHT)
BORDER_SIZE = 4
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Movement Game")

#initialize background image
background_image = pygame.image.load("images/grass.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#Rendering settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKRED = (144, 11, 10)
GRAY = (68,68,68)
GREY = (200, 200, 200)
RED = (212, 14, 0)
ORANGE = (212, 106, 0)
YELLOW = (212, 187, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
BROWN = (59, 55, 54)
FONT = pygame.font.SysFont(None, 30)
font = pygame.font.Font(None, 20)  # Adjusted font size
GIANT_FONT = pygame.font.SysFont(None, 100)

# Bubble properties
bubble_width = int(100 * 0.9)  # Decreased width by 10%
bubble_height = int(50 * 0.9)  # Decreased height by 10%
bubble_offset = 8  # Reduced offset

# Load player and opponent images
player_image = pygame.image.load('images/player1.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (GRID_SIZE, GRID_SIZE))
opponent_image = pygame.image.load('images/player2.png').convert_alpha()
opponent_image = pygame.transform.scale(opponent_image, (GRID_SIZE, GRID_SIZE))

# Global variables
player_turn = 1
turn_state = 0  # 0 - Idle | 1 - Attack | 2 - Rotate (first) | 3 - Move (second optional)
start_time = 0  # sets to real start time when game starts
move_speed = 1  # Number of squares the player moves at a time
highlighted_bubble = None
move_list = []
time_multiplier = 0

# Load player number images
one_image = pygame.image.load('images/1.png').convert_alpha()
one_image = pygame.transform.scale(one_image, (30, 40))
two_image = pygame.image.load('images/2.png').convert_alpha()
two_image = pygame.transform.scale(two_image, (30, 40))

# Load floor image
floor_image = pygame.image.load('images/stone_floor.jpg').convert_alpha()
floor_image = pygame.transform.scale(floor_image,  (GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))

# Rotate player images
player_images = [pygame.transform.rotate(player_image, angle) for angle in (0, 90, 180, 270)]
opponent_images = [pygame.transform.rotate(opponent_image, angle) for angle in (0, 90, 180, 270)]

#=============================================================================================

def generate_random_number():
    return random.randint(0, 37)
    #return 9

def handle_random_outcome(player, other_player, random_number):
    global time_multiplier

    outcome_function = outcome_functions.get(random_number+1)
    if outcome_function:
        player.attack(other_player, outcome_function(), time_multiplier)
    else:
        print("Invalid random number:", random_number)

def fire_ball():
    return ["fire ball", [-5, 0, 1], [-10, 0, 2], [-15, 0, 3], [-20, 0, 4], [-15, 1, 4], [-15, 0, 5], [-15, -1, 4]]
    
def punch():
    #print("punch")
    #[damage, left, forward]
    return ["punch", [-5, 0, 1]]
    
def bishop():
    return ["bishop", [-10, 1, 1], [-10, 2, 2],  [-10, 3, 3], [-10, -1, 1], [-10, -2, 2],  [-10, -3, 3]]

def energy_drink():
    print("energy_drink")

def smelly():
    return ["smelly", [-10, 0, 1], [-10, 1, 1], [-10, 1, 0], [-10, -1, 1], [-10, 1, -1], [-10, -1, -1], [-10, -1, 0], [-10, 0, -1]]

def acid_rain():
    print("acid_rain")

def gun():
    return ["gun", [-20, 0, 1], [-20, 0, 2], [-20, 0, 3], [-20, 0, 4], [-20, 0, 5], [-20, 0, 6]]

def zoom():
    return ["zoom"]

def cleave():
    return ["cleave", [-12, 0, 1, ], [-12, 1, 1, ], [-12, -1, 1, ]]

def arm_day():
    print("arm_day")

def prayer():
    return ["prayer", [15, 0, 0], [15, 0, 1], [15, 1, 1], [15, 1, 0], [15, -1, 1], [15, 1, -1], [15, -1, -1], [15, -1, 0], [15, 0, -1]]

def souls_like():
    print("souls_like")

def backflip():
    return ["backflip", [-10, 0, -1]]
    #not done

def cocaine():
    return ["cocaine", [-10, 0, 0]]

def flame_thrower():
    return ["flame thrower", [-10, 0, 1, ], [-10, 1, 1, ], [-10, -1, 1, ], [-10, 0, 2, ], [-10, 1, 2, ], [-10, -1, 2, ]]

def taco_bell():
    return ["taco bell", [10, 0, 0]]

def home_cookin():
    return ["home cookin", [25, 0, 0]]

def grenade():
    return ["grenade", [-15, 0, 2, ], [-15, 1, 2, ], [-15, -1, 2, ], [-15, 0, 3, ], [-15, 1, 3, ], [-15, -1, 3, ], [-15, 0, 4], [-15, 1, 4], [-15, -1, 4]]

def wario_steam():
    return ["wario steam", [-10, 0, 1, ], [-10, 1, 2, ], [-10, -1, 2, ], [-10, 0, 2, ]]

def tipper():
    return ["tipper", [-5, 0, 1], [-20, 0, 2]]
    
def bair():
    return ["bair", [-15, 0, -1]]

def cannibal():
    return ["cannibal", [-15, 0, 1], [15, 0, 0]]

def split_kick():
    return ["split kick", [-12, 1, 0], [-12, -1, 0]]

def blue_shirt():
    return["blue_shirt"]

def red_shirt():
    print("red_shirt")

def broke():
    print("broke")

def paper_cut():
    print("paper_cut")

def dehydrated():
    return ["dehydrated", [-10, 0, 0]]

def need_a_hand():
    return ["need a hand", [-10, 0, 1], [-10, 0, 2]]

def lazy():
    print("lazy")

def kaklanck():
    print("kaklanck")

def charm():
    return["charm", []]

def kind_hearted():
     return["kind hearted"]

def but_y():
    return["but y"]

def band_member():
    print("band_member")

def scared():
    print("scared")

def dizzy():
    print("dizzy")

def fleshy():
    return ["fleshy"]

outcome_functions = {
    1: fire_ball,
    2: punch,
    3: bishop,
    4: energy_drink,
    5: smelly,
    6: acid_rain,
    7: gun,
    8: zoom,
    9: cleave,
    10: arm_day,
    11: prayer,
    12: souls_like,
    13: backflip,
    14: cocaine,
    15: flame_thrower,
    16: taco_bell,
    17: home_cookin,
    18: grenade,
    19: wario_steam,
    20: tipper,
    21: bair,
    22: cannibal,
    23: split_kick,
    24: blue_shirt,
    25: red_shirt,
    26: broke,
    27: paper_cut,
    28: dehydrated,
    29: need_a_hand,
    30: lazy,
    31: kaklanck,
    32: charm,
    33: kind_hearted,
    34: but_y,
    35: band_member,
    36: scared,
    37: dizzy,
    38: fleshy
}

#==========================================================

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
        self.health = 100
        self.attack_multiplier = 1

    def health_change(self, x):
        self.health += x
        

    def attack(self, other_player, input_code, time_multiplier):
        global turn_state, start_time
        turn_state = 1
        start_time = pygame.time.get_ticks()

        #Special cases
        if input_code[0] == "zoom":
            self.x = random.randint(0, GRID_WIDTH-1)
            self.y = random.randint(0, GRID_HEIGHT-1)
        elif input_code[0] == "arm day":
            self.attack_multiplier *= 1.25 * time_multiplier
        elif input_code[0] == "cocaine":
            self.attack_multiplier *= 1.40 * time_multiplier
        elif input_code[0] == "fleshy":
            other_player.attack_multiplier *= 1.3 * time_multiplier
        elif input_code[0] == "kind hearted":
            other_player.health += 20 * time_multiplier
        elif input_code[0] == "but y":
            other_player.health += 100 * time_multiplier
        elif input_code[0] == "need a hand":
                self.health /= 2 * time_multiplier
        elif input_code[0] == "dehydrated":
            self.attack_multiplier /= 1.5 * time_multiplier
        # elif input_code[0] == "wario steam":  

        #     if 0 <= self.x + dx < GRID_WIDTH and 0 <= self.y + dy < GRID_HEIGHT and not (self.x + dx == other_player.x and self.y + dy == other_player.y):
        #         self.x += dx
        #         self.y += dy
        #     if 0 <= self.x + dx < GRID_WIDTH and 0 <= self.y + dy < GRID_HEIGHT and not (self.x + dx == other_player.x and self.y + dy == other_player.y):
        #         self.x += dx
        #         self.y += dy          

        for i in range(1, len(input_code)):
            coords = calculate_direction([input_code[i][1], input_code[i][2]], self.direction)
            if self.x + coords[0] == other_player.x and self.y + coords[1] == other_player.y:
                other_player.health_change(input_code[i][0] * time_multiplier * self.attack_multiplier)
            if self.x + coords[0] == self.x and self.y + coords[1] == self.y:
                self.health_change(input_code[i][0] * time_multiplier * self.attack_multiplier)
            

    def set_rotation(self, dx, dy):
        if dx > 0:
            self.direction = 1
        elif dx < 0:
            self.direction = 3
        elif dy > 0:
            self.direction = 0
        elif dy < 0:
            self.direction = 2

    def move(self, dx, dy, other_player):
        global turn_state, start_time
        if turn_state == 0:
            turn_state = 2
            self.set_rotation(dx, dy)
            start_time = pygame.time.get_ticks()

        elif turn_state == 2:
            if 0 <= self.x + dx < GRID_WIDTH and 0 <= self.y + dy < GRID_HEIGHT and not (self.x + dx == other_player.x and self.y + dy == other_player.y):
                self.x += dx
                self.y += dy
                finish_turn()

def finish_turn():
    global player_turn, turn_state, start_time
    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1
    turn_state = 0
    start_time = pygame.time.get_ticks()

    for i in range(4):
        move_list[i] = generate_random_number()

def calculate_direction(pair, direction):
    if direction == 0:
        return [-pair[0], pair[1]]
    elif direction == 1:
        return [pair[1], pair[0]]
    elif direction == 2:
        return [pair[0], -pair[1]]
    elif direction == 3:
        return [-pair[1], -pair[0]]

#======================================================================

def player_control(key, player, other_player, left_key, right_key, up_key, down_key, move_key):
    global move_speed, highlighted_bubble

    if key == left_key and pygame.key.get_mods() & move_key:
        player.move(-move_speed, 0, other_player)
    elif key == right_key and pygame.key.get_mods() & move_key:
        player.move(move_speed, 0, other_player)
    elif key == up_key and pygame.key.get_mods() & move_key:
        player.move(0, -move_speed, other_player)
    elif key == down_key and pygame.key.get_mods() & move_key:
        player.move(0, move_speed, other_player)

    elif turn_state == 0:
        if key == left_key:
            highlighted_bubble = 1
            handle_random_outcome(player, other_player, move_list[0])
        elif key == right_key:
            highlighted_bubble = 3
            handle_random_outcome(player, other_player, move_list[2])
        elif key == up_key:
            highlighted_bubble = 4
            handle_random_outcome(player, other_player, move_list[3])
        elif key == down_key:
            highlighted_bubble = 2
            handle_random_outcome(player, other_player, move_list[1])

#====================================================================

# Main game loop
def main():
    player1 = Player(0, 0)
    player2 = Player(GRID_WIDTH - 1, GRID_HEIGHT - 1)

    global start_time, turn_state, player_turn, highlighted_bubble, move_list, time_multiplier
    start_time = pygame.time.get_ticks()  # Get the time when the program starts
    for i in range(4):
        move_list.append(generate_random_number())
    
    running = True

    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                # Player 1 movement with WASD
                if player_turn == 1:
                    player_control(event.key, player1, player2, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.KMOD_LSHIFT)

                elif player_turn == 2:
                    player_control(event.key, player2, player1, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.KMOD_RCTRL)

        #==============================================================

        # Draw background
        WINDOW.blit(background_image, (0, 0))
        
        #insert stage background
        WINDOW.blit(floor_image, (50, 50))
        
        # Draw grid border
        pygame.draw.rect(WINDOW, GRAY, (50, 50, GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE), BORDER_SIZE)

        #health bar player 1
        pygame.draw.rect(WINDOW, WHITE, (10, 530, 100 * 1.5, 30), border_radius= 0)
        pygame.draw.rect(WINDOW, RED, (10, 530, player1.health * 1.5, 30), border_radius= 0)

        #health bear player 2
        pygame.draw.rect(WINDOW, WHITE, (WIDTH - 162, 530, 100 * 1.5, 30), border_radius= 0)
        pygame.draw.rect(WINDOW, RED, (WIDTH - 162, 530, player2.health * 1.5, 30), border_radius= 0)

        # Draw grid
        for x in range(50 + GRID_SIZE, 50 + GRID_WIDTH * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(WINDOW, GRAY, (x, 50), (x, 50 + GRID_HEIGHT * GRID_SIZE - 1), BORDER_SIZE)
        for y in range(50 + GRID_SIZE, 50 + GRID_HEIGHT * GRID_SIZE, GRID_SIZE):
            pygame.draw.line(WINDOW, GRAY, (50, y), (50 + GRID_WIDTH * GRID_SIZE - 1, y), BORDER_SIZE)
        
        # Draw players with rotation
        WINDOW.blit(player_images[player1.direction], (player1.x * GRID_SIZE + 50, player1.y * GRID_SIZE + 50))
        WINDOW.blit(opponent_images[player2.direction], (player2.x * GRID_SIZE + 50, player2.y * GRID_SIZE + 50))

        #highlight hits
        attack_text_surface = GIANT_FONT.render("", True, WHITE)

        if highlighted_bubble and turn_state == 1:
            input_code = outcome_functions.get(move_list[highlighted_bubble-1]+1)

            player = player1 if player_turn == 1 else player2

            for i in range(1, len(input_code())):
                coords = calculate_direction([input_code()[i][1], input_code()[i][2]], player.direction)
                pygame.draw.rect(WINDOW, RED, ((player.x + coords[0]) * GRID_SIZE + 50 + 10, (player.y + coords[1]) * GRID_SIZE + 50 + 10, GRID_SIZE - 20, GRID_SIZE - 20), border_radius=10)

            attack_text_surface = GIANT_FONT.render(str(input_code()[0]), True, WHITE)  # Render the text with variable value

        # Draw text bubbles
        bubble_positions = [
            (50 + GRID_WIDTH * GRID_SIZE // 4 - bubble_width // 2, HEIGHT - 50 - bubble_height - 20), # A bubble
            (50 + 2 * GRID_WIDTH * GRID_SIZE // 4 - bubble_width // 2, HEIGHT - 50 - bubble_height - 20), # W bubble
            (50 + 3 * GRID_WIDTH * GRID_SIZE // 4 - bubble_width // 2, HEIGHT - 50 - bubble_height - 20), # S bubble
            (50 + GRID_WIDTH * GRID_SIZE // 2 - bubble_width // 2, HEIGHT - 50 - 2 * bubble_height - 40), # D bubble
        ]

        for i, (x, y) in enumerate(bubble_positions):
            # Check if bubble should be highlighted
            if i + 1 == highlighted_bubble:
                pygame.draw.rect(WINDOW, RED, (x, y, bubble_width, bubble_height), border_radius=20)
            else:
                pygame.draw.rect(WINDOW, GREY, (x, y, bubble_width, bubble_height), border_radius=20)

            # Draw text
            text_surface = font.render(list(outcome_functions.items())[move_list[i]][1].__name__, True, BLACK)  # Render the text with variable value
            text_rect = text_surface.get_rect(center=(x + bubble_width // 2, y + bubble_height // 2))
            WINDOW.blit(text_surface, text_rect)

        if player_turn == 1:
            WINDOW.blit(one_image, (450, 5))
        else:
            WINDOW.blit(two_image, (450, 5))

        # Clock - Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time)
        #timer_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        #timer_text = FONT.render(f"Time: {elapsed_time}ms", True, BLACK)

       # timer_surface.blit(timer_text, (5, 5))
        #WINDOW.blit(timer_surface, (5, 5))  # Position the timer overlay

        #text_surface = FONT.render("Player Turn: " + str(player_turn), True, WHITE)  # Render the text with variable value
        #WINDOW.blit(text_surface, (300, 10))  # Blit the text surface onto the window

        # Progress Bar
        if turn_state == 0:
            time_window = 5 * 1000
            progress_bar_color = GREEN
        elif turn_state == 1:
            time_window = 1.5 * 1000
            progress_bar_color = RED
        elif turn_state == 2:
            time_window = 1 * 1000
            progress_bar_color = BLUE
            
        progress_width = (time_window - elapsed_time) / time_window * WIDTH  # Calculate width of progress bar
        pygame.draw.rect(WINDOW, progress_bar_color, (0, HEIGHT - 20, progress_width, 20))

        if progress_width <= 0:
            finish_turn()

        # Time multiplier
        if turn_state == 0:
            time_multiplier = (((time_window - elapsed_time) / time_window) ** 4) + 1

        #WINDOW.blit(FONT.render("Time Multiplier: " + str(round(time_multiplier, 3)), True, WHITE), (200, HEIGHT - 50))
        WINDOW.blit(FONT.render("x2", True, WHITE), (360, HEIGHT - 55))
        WINDOW.blit(FONT.render("x1", True, WHITE), (120, HEIGHT - 55))
        pygame.draw.rect(WINDOW, WHITE, (150, HEIGHT-50, 200, 10), border_radius = 10)
        pygame.draw.rect(WINDOW, YELLOW, (150, HEIGHT-50, (time_multiplier-1)*200, 10), border_radius = 10)

        # Attack Multiplier
        WINDOW.blit(FONT.render("x" + str(player1.attack_multiplier), True, WHITE), (10, HEIGHT - 135))
        WINDOW.blit(FONT.render("x" + str(player2.attack_multiplier), True, WHITE), (460, HEIGHT - 135))

        # Attack text
        WINDOW.blit(attack_text_surface, (-200 + progress_width * 1.5, 240))

        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()