#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()
motor_1 = Motor(Ports.PORT1, False)
motor_5 = Motor(Ports.PORT5, True)


# Wait for sensor(s) to fully initialize
wait(100, MSEC)

# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 

# Initialize random seed 
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode EXP Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

# create events
FWD = Event()
RT = Event()
LT = Event()

#Functions
def when_started():
    FWD.broadcast_and_wait()
    LT.broadcast_and_wait()
    FWD.broadcast_and_wait()
    RT.broadcast_and_wait()
    FWD.broadcast_and_wait()

def motor1_move_forward():
    motor_1.spin_for(FORWARD, 425, DEGREES)
def motor5_move_forward():
    motor_5.spin_for(FORWARD, 425, DEGREES)
def motor1_turn_right():
    motor_1.spin_for(FORWARD, 220, DEGREES,)
def motor5_turn_right():
    motor_5.spin_for(FORWARD, 220, DEGREES,)
def motor1_turn_left():
    motor_1.spin_for(FORWARD, 220, DEGREES,)
def motor5_turn_left():
    motor_5.spin_for(FORWARD, 220, DEGREES,)

    #register the callback functions to the evnts 
    FWD(motor1_move_forward)
    FWD(motor5_move_forward)
    RT(motor1_turn_right)
    RT(motor5_turn_right)
    LT(motor1_turn_left)
    LT(motor5_turn_left)
    wait(15, MSEC)

    # start the program!
# Color-specific action cards (2 of each per color)
COLOR_ACTION_CARDS = ["Skip", "Reverse", "Draw Two"]

# Wild cards (no specific color, 4 of each in deck)
WILD_CARDS = ["Wild", "Wild Draw Four"]
# ----------------------------------------------------------------------------
# VEX EXP Python Code - Complete UNO Deck & Setup
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - Complete UNO Deck & Setup (No F-Strings)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - Complete UNO Deck & Setup (VEX MicroPython Clean)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - Complete UNO Deck Setup (Console Output Only)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - Complete UNO Deck Setup (Maximum Compatibility)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - Complete UNO Deck Setup (Maximum Compatibility)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - UNO Startup & Screen Display (5x16 Grid)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - UNO Startup & Screen Display (Universal Compatibility)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - Fixed LCD Screen Display Methods
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - Complete Interactive UNO Game with Driving
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP Python Code - UNO Robot Driver & Game Loop
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game (Full Integration)
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - Complete UNO Robot Game
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game (With Motor Hardware Driving)
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game (With Motor Hardware Driving)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - Complete UNO Robot Game
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# BROADCAST DEFINITIONS & MOVEMENT HANDLERS
# ----------------------------------------------------------------------------
# Define Broadcast Events
# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# VEX EXP MicroPython Code - UNO Robot Game
# ----------------------------------------------------------------------------

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



def motor1_turn_right():
    motor_1.spin_for(FORWARD, 220, DEGREES)

def motor5_turn_right():
    motor_5.spin_for(REVERSE, 220, DEGREES)

def motor1_turn_left():
    motor_1.spin_for(REVERSE, 220, DEGREES)

def motor5_turn_left():
    motor_5.spin_for(FORWARD, 220, DEGREES)

# Register callback functions to events
FWD.broadcast(motor1_move_forward)
FWD.broadcast(motor5_move_forward)
RT.broadcast(motor1_turn_right)
RT.broadcast(motor5_turn_right)
LT.broadcast(motor1_turn_left)
LT.broadcast(motor5_turn_left)

# --- CARD DEFINITIONS ---
COLORS = ["Red", "Yellow", "Green", "Blue"]
COLOR_ACTION_CARDS = ["Skip", "Reverse", "Draw Two"]
WILD_CARDS = ["Wild", "Wild Draw Four"]

# ----------------------------------------------------------------------------
# LCD SCREEN DISPLAY HELPERS (5 Rows x 16 Columns)
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

def draw_card_full_screen(card_str, color_code):
    brain.screen.clear_screen()
    corner_tag = str(color_code)[0].upper()
    top_line = "+--[" + corner_tag + "]--------+"
    bottom_line = "+--------[" + corner_tag + "]--+"

    center_text = str(color_code).upper() + " " + str(card_str).upper()
    total_padding = 14 - len(center_text)
    if total_padding < 0:
        center_text = center_text[0:14]
        left_pad = 0
        right_pad = 0
    else:
        left_pad = total_padding // 2
        right_pad = total_padding - left_pad

    middle_line = "|" + (" " * left_pad) + center_text + (" " * right_pad) + "|"

    print_screen_line(1, top_line)
    print_screen_line(2, "|              |")
    print_screen_line(3, middle_line)
    print_screen_line(4, "|              |")
    print_screen_line(5, bottom_line)

def render_uno_card_object(card):
    if card['type'] == 'wild':
        if card['value'] == 'Wild':
            draw_card_full_screen("WILD", "WILD")
        else:
            draw_card_full_screen("+4", "WILD")
    else:
        val = str(card['value'])
        if val == "Draw Two":
            val = "+2"
        elif val == "Reverse":
            val = "REV"
        elif val == "Skip":
            val = "SKIP"
        draw_card_full_screen(val, str(card['color']).upper())

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
# MENU 1: INPUT INITIAL TOP DISCARD CARD
# ----------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------
# MENU 2: SELECT LEGAL PLAY OR DRAW
# ----------------------------------------------------------------------------
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
    time.sleep(0.015) # Wait 15ms as specified in setup

    deck = build_uno_deck()
    custom_shuffle(deck)
    draw_pile = deck
    discard_pile = []
    
    p1_hand = []
    for _ in range(7):
        card, draw_pile, discard_pile = draw_card(draw_pile, discard_pile)
        p1_hand.append(card)

    top_card = input_top_card_menu()
    discard_pile.append(top_card)

    game_over = False
    while not game_over:
        display_player_hand(p1_hand)
        action, hand_index = play_or_draw_menu("P1", p1_hand, top_card)
        
        drive_to_center()

        if action == "DRAW":
            drawn, draw_pile, discard_pile = draw_card(draw_pile, discard_pile)
            if drawn:
                p1_hand.append(drawn)
                render_uno_card_object(drawn)
                time.sleep(2)
        elif action == "PLAY":
            played_card = p1_hand.pop(hand_index)
            discard_pile.append(played_card)
            top_card = played_card
            render_uno_card_object(played_card)
            time.sleep(2)

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