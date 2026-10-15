import random
import time
from vex import *

# Initialize VEX Brain & Motors
brain = Brain()
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_5 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)

# --- BROADCAST EVENTS ---
FWD = Event()
LT = Event()
RT = Event()

# --- HARDWARE CALLBACK FUNCTIONS ---
def motor1_move_forward():
    motor_1.spin_for(FORWARD, 360, DEGREES)

def motor5_move_forward():
    motor_5.spin_for(REVERSE, 360, DEGREES)

def motor1_turn_right():
    motor_1.spin_for(FORWARD, 220, DEGREES)

def motor5_turn_right():
    motor_5.spin_for(REVERSE, 220, DEGREES)

def motor1_turn_left():
    motor_1.spin_for(REVERSE, 220, DEGREES)

def motor5_turn_left():
    motor_5.spin_for(FORWARD, 220, DEGREES)

# Register callback functions to events
FWD(motor1_move_forward)
FWD(motor5_move_forward)
RT(motor1_turn_right)
RT(motor5_turn_right)
LT(motor1_turn_left)
LT(motor5_turn_left)

# --- CARD DEFINITIONS ---
COLORS = ["Red", "Yellow", "Green", "Blue"]
COLOR_ACTION_CARDS = ["Skip", "Reverse", "Draw Two"]
WILD_CARDS = ["Wild", "Wild Draw Four"]

# ----------------------------------------------------------------------------
# LCD SCREEN DISPLAY HELPERS
# ----------------------------------------------------------------------------
def print_screen_line(row, text):
    if len(text) > 16:
        text = text[0:16]
    brain.screen.set_cursor(row, 1)
    brain.screen.print(text)

def wait_for_button_press():
    while True:
        if brain.buttonLeft.pressing():
            while brain.buttonLeft.pressing():
                time.sleep(0.05)
            return "LEFT"
        if brain.buttonRight.pressing():
            while brain.buttonRight.pressing():
                time.sleep(0.05)
            return "RIGHT"
        if brain.buttonCheck.pressing():
            while brain.buttonCheck.pressing():
                time.sleep(0.05)
            return "CHECK"
        time.sleep(0.05)

def draw_card_back():
    """Displays the back of an Uno card on the VEX screen."""
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    for i in range(5):
        brain.screen.draw_rectangle(0+i, 0+i, 159-(i*2), 107-(i*2))
    
    brain.screen.set_fill_color(Color.RED)
    brain.screen.set_pen_color(Color.RED)
    for i in range(40):
        brain.screen.draw_circle(60+i, 42+(i/2), 30)
    
    brain.screen.set_pen_color(Color.YELLOW)
    for i in range(5):
        brain.screen.draw_line(75, 50+i-5, 85, 50+i-5)
        brain.screen.draw_line(75, 50+i+5, 85, 50+i+5)
        brain.screen.draw_line(75, 50+i+5, 85, 50+i-5)

        brain.screen.draw_line(75, 50+i-15, 85, 50+i-15)
        brain.screen.draw_line(75+(i/2), 50-15, 75+(i/2), 50-25)
        brain.screen.draw_line(83+(i/2), 50-15, 83+(i/2), 50-25)
        brain.screen.draw_line(75, 50+i-25, 85, 50+i-25)

        brain.screen.draw_line(75, 50+i+15, 85, 50+i+15)
        brain.screen.draw_line(83+(i/2), 50+15, 83+(i/2), 50+25)
        brain.screen.draw_line(75, 50+i+25, 85, 50+i+25)
    brain.screen.set_fill_color(Color.TRANSPARENT)

def draw_card_full_screen(card_str, color_code):
    brain.screen.clear_screen()
    if color_code == 'R': brain.screen.set_fill_color(Color.RED)
    elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
    elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
    elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
    else: brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    for i in range(5):
        brain.screen.draw_rectangle(0+i, 0+i, 159-(i*2), 107-(i*2))
   
    card = card_str[1:] if len(card_str) > 1 else card_str
    if card == "0":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
    elif card == "8":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(72+i, 20, 72+i, 85)
    elif card == "1":
        for i in range(15):
            brain.screen.draw_line(20, 47+i, 139, 47+i)
    elif card == "3":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
    elif card == "2":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "5":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "6":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "9":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "4" and "D" not in card_str:
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
    elif card == "7":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
    elif card == "Rv":
        for i in range(15):
            brain.screen.draw_line(62+i, 30, 62+i, 87)
            brain.screen.draw_line(69, 20, 52+i, 40)
            brain.screen.draw_line(69, 20, 82-i, 40)
            brain.screen.draw_line(82+i, 20, 82+i, 77)
            brain.screen.draw_line(89, 87, 74+i, 67)
            brain.screen.draw_line(89, 87, 104-i, 67)
    elif card == "S":
        for i in range(15):
            brain.screen.draw_rectangle(40+i, 20+i, 82-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(52+i, 20, 92+i, 80)
    elif card == "D2":
        brain.screen.set_fill_color(Color.WHITE)
        for i in range(40):
            brain.screen.draw_circle(60+i, 42+(i/2), 30)
        if color_code == 'R': brain.screen.set_fill_color(Color.RED)
        elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
        elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
        elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(47, 32, 40, 25)
        brain.screen.draw_rectangle(73, 52, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10+i, 66, 10+i, 79)
            brain.screen.draw_line(10, 66+i, 20, 66+i)
            brain.screen.draw_line(18+i, 66, 18+i, 79)
            brain.screen.draw_line(20, 75+i, 30, 75+i)
            brain.screen.draw_line(26+i, 66, 26+i, 79)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10-i, 107-66, 159-10-i, 107-79)
            brain.screen.draw_line(159-10, 107-66-i, 159-20, 107-66-i)
            brain.screen.draw_line(159-18-i, 107-66, 159-18-i, 107-79)
            brain.screen.draw_line(159-20, 107-75-i, 159-30, 107-75-i)
            brain.screen.draw_line(159-26-i, 107-66, 159-26-i, 107-79)
    elif card_str == "W":
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(50, 20, 30, 32)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(50, 52, 30, 32)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(80, 20, 30, 32)
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(80, 52, 30, 32)
        brain.screen.set_fill_color(Color.TRANSPARENT)
        brain.screen.set_pen_width(3)
        for i in range(15):
            brain.screen.draw_circle(80, 52, 30-(i/5))
        brain.screen.set_pen_color(Color.BLACK)
        for i in range(65):
            brain.screen.draw_circle(80, 52, 31+(i/5))
        brain.screen.set_pen_width(1)
    elif card_str == "D4":
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(78, 42, 40, 25)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(60, 28, 40, 25)
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(42, 42, 40, 25)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(60, 56, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10, 75+i, 20, 75+i)
            brain.screen.draw_line(16+i, 75, 16+i, 66)
            brain.screen.draw_line(10, 66+i, 30, 66+i)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10, 107-75-i, 159-20, 107-75-i)
            brain.screen.draw_line(159-16-i, 107-75, 159-16-i, 107-66)
            brain.screen.draw_line(159-10, 107-66-i, 159-30, 107-66-i)
    else:
        draw_card_back()
    brain.screen.set_fill_color(Color.TRANSPARENT)

def render_uno_card_object(card):
    """Converts a card dictionary into card_str and color_code for draw_card_full_screen."""
    color_code = str(card['color'])[0].upper()
    val = str(card['value'])

    if card['type'] == 'wild':
        card_str = "W" if val == "Wild" else "D4"
        color_code = "W"
    else:
        if val == "Draw Two":
            card_val = "D2"
        elif val == "Reverse":
            card_val = "Rv"
        elif val == "Skip":
            card_val = "S"
        else:
            card_val = val
        card_str = color_code + card_val

    draw_card_full_screen(card_str, color_code)

# ----------------------------------------------------------------------------
# ROBOT MOVEMENT ROUTINES
# ----------------------------------------------------------------------------
def drive_to_center():
    brain.screen.clear_screen()
    print_screen_line(2, "DRIVING TO")
    print_screen_line(3, "CENTER PILE...")
    FWD.broadcast_and_wait()
    LT.broadcast_and_wait()
    FWD.broadcast_and_wait()
    RT.broadcast_and_wait()
    FWD.broadcast_and_wait()

def drive_back_to_player():
    brain.screen.clear_screen()
    print_screen_line(2, "RETURNING TO")
    print_screen_line(3, "PLAYER...")
    LT.broadcast_and_wait()
    LT.broadcast_and_wait()
    FWD.broadcast_and_wait()
    LT.broadcast_and_wait()
    FWD.broadcast_and_wait()
    RT.broadcast_and_wait()
    FWD.broadcast_and_wait()
    LT.broadcast_and_wait()
    LT.broadcast_and_wait()

# ----------------------------------------------------------------------------
# DECK MANAGEMENT
# ----------------------------------------------------------------------------
def build_uno_deck():
    deck = []
    for color in COLORS:
        deck.append({'color': color, 'type': 'number', 'value': 0})
        for num in range(1, 10):
            deck.append({'color': color, 'type': 'number', 'value': num})
            deck.append({'color': color, 'type': 'number', 'value': num})

    for color in COLORS:
        for action in COLOR_ACTION_CARDS:
            deck.append({'color': color, 'type': 'action', 'value': action})
            deck.append({'color': color, 'type': 'action', 'value': action})

    for wild_type in WILD_CARDS:
        for _ in range(4):
            deck.append({'color': 'Wild', 'type': 'wild', 'value': wild_type})

    return deck

def custom_shuffle(items):
    n = len(items)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        items[i], items[j] = items[j], items[i]

def draw_multiple_cards(count, draw_pile, discard_pile, hand):
    """Draws multiple cards sequentially, displaying the card back animation for each."""
    for i in range(count):
        drawn, draw_pile, discard_pile = draw_card(draw_pile, discard_pile)
        if drawn:
            hand.append(drawn)
            draw_card_back()
            time.sleep(0.4)
            brain.screen.clear_screen()
            time.sleep(0.1)
    return draw_pile, discard_pile

def draw_card(draw_pile, discard_pile):
    if len(draw_pile) == 0:
        if len(discard_pile) <= 1:
            return None, draw_pile, discard_pile
        top_discard = discard_pile.pop()
        draw_pile = list(discard_pile)
        discard_pile = [top_discard]
        custom_shuffle(draw_pile)

    drawn_card = draw_pile.pop(0)
    return drawn_card, draw_pile, discard_pile

def format_card_short(card):
    if card['type'] == 'wild':
        return "[WILD]" if card['value'] == 'Wild' else "[W+4]"
    else:
        c_code = str(card['color'])[0]
        val = str(card['value'])
        if val == "Draw Two":
            val = "+2"
        elif val == "Reverse":
            val = "Rev"
        elif val == "Skip":
            val = "Skp"
        return c_code + " " + val

def display_player_hand(hand):
    brain.screen.clear_screen()
    print_screen_line(1, "HAND (" + str(len(hand)) + " CARDS)")
    row = 2
    card_idx = 1
    line_str = ""
    for card in hand:
        card_str = str(card_idx) + ":" + format_card_short(card) + " "
        if len(line_str + card_str) > 16:
            print_screen_line(row, line_str)
            row += 1
            line_str = card_str
            if row > 4:
                break
        else:
            line_str += card_str
        card_idx += 1

    if row <= 4 and len(line_str) > 0:
        print_screen_line(row, line_str)

    print_screen_line(5, "Press CHECK...")
    wait_for_button_press()

# ----------------------------------------------------------------------------
# MENUS
# ----------------------------------------------------------------------------
def choose_wild_color():
    color_idx = 0
    while True:
        brain.screen.clear_screen()
        print_screen_line(1, "WILD CARD!")
        print_screen_line(2, "Choose Color:")
        print_screen_line(3, "< " + COLORS[color_idx] + " >")
        print_screen_line(5, "L/R:Nav CHECK:Ok")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            color_idx = (color_idx - 1) % len(COLORS)
        elif btn == "RIGHT":
            color_idx = (color_idx + 1) % len(COLORS)
        elif btn == "CHECK":
            return COLORS[color_idx]

def input_top_card_menu():
    color_idx = 0
    while True:
        brain.screen.clear_screen()
        print_screen_line(1, "SET DISCARD TOP")
        print_screen_line(2, "Select Color:")
        print_screen_line(3, "< " + COLORS[color_idx] + " >")
        print_screen_line(5, "L/R:Nav CHECK:Ok")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            color_idx = (color_idx - 1) % len(COLORS)
        elif btn == "RIGHT":
            color_idx = (color_idx + 1) % len(COLORS)
        elif btn == "CHECK":
            selected_color = COLORS[color_idx]
            break

    values = ["0","1","2","3","4","5","6","7","8","9","Skip","Reverse","Draw Two"]
    val_idx = 0
    while True:
        brain.screen.clear_screen()
        print_screen_line(1, "SET DISCARD TOP")
        print_screen_line(2, "Color: " + selected_color)
        print_screen_line(3, "Val: < " + values[val_idx] + " >")
        print_screen_line(5, "L/R:Nav CHECK:Ok")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            val_idx = (val_idx - 1) % len(values)
        elif btn == "RIGHT":
            val_idx = (val_idx + 1) % len(values)
        elif btn == "CHECK":
            selected_val = values[val_idx]
            break

    card_type = "number"
    if selected_val in COLOR_ACTION_CARDS:
        card_type = "action"
    elif selected_val in ["0","1","2","3","4","5","6","7","8","9"]:
        selected_val = int(selected_val)

    return {'color': selected_color, 'type': card_type, 'value': selected_val}

def get_legal_cards(hand, top_card):
    legal_cards = []
    index = 0
    for card in hand:
        if card['type'] == 'wild':
            legal_cards.append((index, card))
        elif card['color'] == top_card['color']:
            legal_cards.append((index, card))
        elif str(card['value']) == str(top_card['value']):
            legal_cards.append((index, card))
        index += 1
    return legal_cards

def play_or_draw_menu(player_name, hand, top_card):
    legal_options = get_legal_cards(hand, top_card)
    menu_options = ["DRAW CARD"]
    for item in legal_options:
        menu_options.append(format_card_short(item[1]))
        
    current_idx = 0
    while True:
        brain.screen.clear_screen()
        print_screen_line(1, player_name + "'s Turn")
        print_screen_line(2, "Top: " + format_card_short(top_card))
        
        if current_idx == 0:
            print_screen_line(3, "Option: < DRAW >")
            print_screen_line(4, "Action: Take Card")
        else:
            selected_legal = legal_options[current_idx - 1]
            hand_pos = selected_legal[0] + 1
            print_screen_line(3, "Opt: < " + menu_options[current_idx] + " >")
            print_screen_line(4, "Card #" + str(hand_pos) + " Playable")
            
        print_screen_line(5, "L/R:Nav CHECK:Ok")
        
        btn = wait_for_button_press()
        if btn == "LEFT":
            current_idx = (current_idx - 1) % len(menu_options)
        elif btn == "RIGHT":
            current_idx = (current_idx + 1) % len(menu_options)
        elif btn == "CHECK":
            if current_idx == 0:
                return "DRAW", None
            else:
                chosen_hand_index = legal_options[current_idx - 1][0]
                return "PLAY", chosen_hand_index

# ----------------------------------------------------------------------------
# MAIN GAME STARTUP
# ----------------------------------------------------------------------------
def when_started():
    time.sleep(0.015)

    deck = build_uno_deck()
    custom_shuffle(deck)
    draw_pile = deck
    discard_pile = []
    
    # Initial deal: draw 7 cards showing card back graphics
    p1_hand = []
    draw_pile, discard_pile = draw_multiple_cards(7, draw_pile, discard_pile, p1_hand)

    top_card = input_top_card_menu()
    discard_pile.append(top_card)

    game_over = False
    while not game_over:
        display_player_hand(p1_hand)
        action, hand_index = play_or_draw_menu("P1", p1_hand, top_card)
        
        # Hide hand and show privacy screen while robot travels
        drive_to_center()

        if action == "DRAW":
            draw_pile, discard_pile = draw_multiple_cards(1, draw_pile, discard_pile, p1_hand)
        elif action == "PLAY":
            played_card = p1_hand.pop(hand_index)
            
            if played_card['type'] == 'wild':
                chosen_color = choose_wild_color()
                played_card['color'] = chosen_color

            discard_pile.append(played_card)
            top_card = played_card
            render_uno_card_object(played_card)
            time.sleep(2)

        # Hide screen while returning
        drive_back_to_player()

        if len(p1_hand) == 0:
            game_over = True
            brain.screen.clear_screen()
            print_screen_line(2, "=== YOU WIN! ===")
            print_screen_line(3, "NO CARDS LEFT")
            print_screen_line(5, "GAME OVER")
            time.sleep(5)

# Execute program
when_started()