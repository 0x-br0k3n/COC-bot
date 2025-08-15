import stats
import time
import utils
import region
import pyautogui
import cv2
import numpy as np
import tkinter as tk
from main import cc_reinforce

from constants import ASSETS_DIR
CONFIDENCE = 0.6

SUPER_BARBARIAN_ICON = 'assets/super_barbarian.png'

ATTACK=(43, 224)

def attack_init():
    print("Attack initiated")
    utils.click(*ATTACK) # start attack macro
    time.sleep(10)
    # TODO: implement lightning
    lightning_attack()

    time.sleep(60)
    try:
        utils.find_and_click(f'{ASSETS_DIR}/return_home.png')
    except Exception as e:
        print(f"Ending battle forcefully...")
    end_attack()
    
def end_attack():
    print("Ending the attack...")
    utils.find_and_click(f'{ASSETS_DIR}/end_battle.png')
    time.sleep(1)
    utils.find_and_click(f'{ASSETS_DIR}/confirm_end_battle.png')
    time.sleep(1)
    print("Updating stats...")
    gold = utils.capture_and_read_text(region.REGION_GOLD_ATTACK)
    elixir = utils.capture_and_read_text(region.REGION_ELIXIR_ATTACK)
    dark_elixir = utils.capture_and_read_text(region.REGION_DARK_ELIXIR_ATTACK)
    trophies = utils.capture_and_read_text(region.REGION_TROPHIES_ATTACK)
    stats.update_stats(gold, elixir, dark_elixir, 0, 0, 0, trophies)
    utils.find_and_click(f'{ASSETS_DIR}/return_home.png')
    time.sleep(4)
    cc_reinforce()

def lightning_attack():
    try:
        utils.find_and_click(f'{ASSETS_DIR}/lightning_pump.png',region=(374, 122, 1203, 648), conf=0.6)
        utils.find_and_click(f'{ASSETS_DIR}/lightning_hero.png',region=(374, 122, 1203, 648), conf=0.6)
    except Exception as e:
        print(f"Hero or collector not found :(")