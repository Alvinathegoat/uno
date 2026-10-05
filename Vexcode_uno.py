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

import random
import time


# Initialize VEX Brain
brain = Brain()

# --- CARD ATTRIBUTES ---
COLORS = ["Red", "Yellow", "Green", "Blue"]
COLOR_ACTION_CARDS = ["Skip", "Reverse", "Draw Two"]
WILD_CARDS = ["Wild", "Wild Draw Four"]

def build_uno_deck():
    deck = []

    # 1. Number Cards (76 cards)
    for color in COLORS:
        deck.append({'color': color, 'type': 'number', 'value': 0})
        for num in range(1, 10):
            deck.append({'color': color, 'type': 'number', 'value': num})
            deck.append({'color': color, 'type': 'number', 'value': num})

    # 2. Colored Action Cards (24 cards)
    for color in COLORS:
        for action in COLOR_ACTION_CARDS:
            deck.append({'color': color, 'type': 'action', 'value': action})
            deck.append({'color': color, 'type': 'action', 'value': action})

    # 3. Wild Action Cards (8 cards)
    for wild_type in WILD_CARDS:
        for _ in range(4):
            deck.append({'color': 'Wild', 'type': 'wild', 'value': wild_type})

    return deck

def custom_shuffle(items):
    n = len(items)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        items[i], items[j] = items[j], items[i]

# ----------------------------------------------------------------------------
# Reusable Card Drawing Function
# ----------------------------------------------------------------------------
def draw_card(draw_pile, discard_pile):
    if len(draw_pile) == 0:
        if len(discard_pile) <= 1:
            print("No cards left to draw!")
            return None, draw_pile, discard_pile
            
        top_discard = discard_pile.pop()
        draw_pile = list(discard_pile)
        discard_pile = [top_discard]
        custom_shuffle(draw_pile)
        print("--- Draw pile empty. Discard pile reshuffled! ---")

    drawn_card = draw_pile.pop(0)
    return drawn_card, draw_pile, discard_pile

# ----------------------------------------------------------------------------
# Reusable Game Startup Function
# ----------------------------------------------------------------------------
def start_game(num_players=2):
    deck = build_uno_deck()
    custom_shuffle(deck)
    
    draw_pile = deck
    discard_pile = []
    players_hands = {}

    p_num = 1
    while p_num <= num_players:
        players_hands["Player_" + str(p_num)] = []
        p_num = p_num + 1

    # Draw 7 cards for each player
    card_count = 0
    while card_count < 7:
        p_num = 1
        while p_num <= num_players:
            card, draw_pile, discard_pile = draw_card(draw_pile, discard_pile)
            players_hands["Player_" + str(p_num)].append(card)
            p_num = p_num + 1
        card_count = card_count + 1

    # Start discard pile
    starting_card, draw_pile, discard_pile = draw_card(draw_pile, discard_pile)
    while starting_card['value'] == "Wild Draw Four":
        draw_pile.append(starting_card)
        custom_shuffle(draw_pile)
        starting_card, draw_pile, discard_pile = draw_card(draw_pile, discard_pile)

    discard_pile.append(starting_card)

    return draw_pile, discard_pile, players_hands

# ----------------------------------------------------------------------------
# Helper Function to Shorten Card String to Fit Screen (Max 16 Chars)
# ----------------------------------------------------------------------------
def format_card_short(card):
    if card['type'] == 'wild':
        if card['value'] == 'Wild':
            return "[WILD]"
        else:
            return "[W+4]"
    else:
        c_code = str(card['color'])[0]  # First letter (R, Y, G, B)
        val = str(card['value'])
        if val == "Draw Two":
            val = "+2"
        elif val == "Reverse":
            val = "Rev"
        elif val == "Skip":
            val = "Skp"
        return c_code + " " + val

# ----------------------------------------------------------------------------
# VEX Brain LCD Screen Printing Function
# ----------------------------------------------------------------------------
def print_to_lcd(row, text):
    """
    Sets cursor position on the Lcd screen and prints text.
    Row: 1 to 5
    Col: 1 (Truncates text to 16 characters max)
    """
    if len(text) > 16:
        text = text[0:16]
        
    brain.screen.set_cursor(row, 1)
    brain.screen.print(text)

def print_starting_hand_to_screen(hand):
    # Clear screen first
    brain.screen.clear_screen()

    # Format cards for 5 rows x 16 columns layout
    c1 = format_card_short(hand[0])
    c2 = format_card_short(hand[1])
    c3 = format_card_short(hand[2])
    c4 = format_card_short(hand[3])
    c5 = format_card_short(hand[4])
    c6 = format_card_short(hand[5])
    c7 = format_card_short(hand[6])

    # Row 1: Title Header
    print_to_lcd(1, "P1 HAND (7 CARDS)")

    # Rows 2-5: Pack two cards per row within 16 chars
    print_to_lcd(2, "1:" + c1 + " 2:" + c2)
    print_to_lcd(3, "3:" + c3 + " 4:" + c4)
    print_to_lcd(4, "5:" + c5 + " 6:" + c6)
    print_to_lcd(5, "7:" + c7)

def print_starting_hand_to_console(player_name, hand):
    print("=== STARTING HAND FOR " + player_name + " (7 Cards) ===")
    index = 1
    for card in hand:
        if card['type'] == 'wild':
            print("Card " + str(index) + ": [" + str(card['value']) + "]")
        else:
            print("Card " + str(index) + ": " + str(card['color']) + " " + str(card['value']))
        index = index + 1
    print("")

# ----------------------------------------------------------------------------
# Main Execution
# ----------------------------------------------------------------------------
def main():
    # Start game and draw initial 7 cards
    draw_pile, discard_pile, players_hands = start_game(num_players=2)
    
    p1_hand = players_hands["Player_1"]

    # Output to Console Terminal
    print_starting_hand_to_console("Player_1", p1_hand)

    # Output to VEX Brain LCD Screen
    print_starting_hand_to_screen(p1_hand)

    # Keep program alive so the display remains visible
    while True:
        time.sleep(1)

main()