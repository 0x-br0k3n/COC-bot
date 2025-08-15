import pyautogui
import time
import region as reg
import stats
import utils
import keyboard
import attack
from constants import ASSETS_DIR, CONFIDENCE

CC=(145, 720)
CC_RE=(1488, 786)
CC_CONFIRM=(1136, 705)
EXIT_CC=(1693, 161)

def isSuitableBase():
    # gold : region=(155, 214, 194, 35)
    # elixir : region=(153, 262, 155, 35)
    # dark elixir : region=(150, 306, 155, 35)
    # utils.swipe(970, 490, 1001, 99)

    gold = utils.capture_and_read_text(reg.REGION_GOLD_ENEMY)
    elixir = utils.capture_and_read_text(reg.REGION_ELIXIR_ENEMY)
    dark_elixir= utils.capture_and_read_text(reg.REGION_DARK_ELIXIR_ENEMY)

    print(f"Gold: {gold}, Elixir: {elixir}, Dark Elixir: {dark_elixir}")

    if(dark_elixir >= 5000):
            print("Suitable base found with sufficient Dark Elixir, start attack...")
            return True
    if(gold == -1 or elixir == -1 or dark_elixir == -1):
        print("One or more resources could not be read!")

    return False

def collect_resources():
    try:
        if pyautogui.locateOnScreen(f'{ASSETS_DIR}/collect_gold.png', confidence=CONFIDENCE) is not None:
            gold_before = utils.capture_and_read_text(reg.REGION_GOLD_MY)
            utils.find_and_click(f'{ASSETS_DIR}/collect_gold.png')
            time.sleep(1)
            gold_after = utils.capture_and_read_text(reg.REGION_GOLD_MY)
            stats.update_stats(0, 0, 0, gold_after - gold_before, 0, 0, 0)
            print(f"Gold collected: {gold_after - gold_before}")

        if pyautogui.locateOnScreen(f'{ASSETS_DIR}/collect_elixir.png', confidence=CONFIDENCE) is not None:
            elixir_before = utils.capture_and_read_text(reg.REGION_ELIXIR_MY)
            utils.find_and_click(f'{ASSETS_DIR}/collect_elixir.png')
            time.sleep(1)
            elixir_after = utils.capture_and_read_text(reg.REGION_ELIXIR_MY)
            stats.update_stats(0, 0, 0, 0, elixir_after - elixir_before, 0, 0)
            print(f"Elixir collected: {elixir_after - elixir_before}")

        if pyautogui.locateOnScreen(f'{ASSETS_DIR}/collect_dark_elixir.png', confidence=CONFIDENCE) is not None:
            dark_elixir_before = utils.capture_and_read_text(reg.REGION_DARK_ELIXIR_MY)
            utils.find_and_click(f'{ASSETS_DIR}/collect_dark_elixir.png')
            time.sleep(1)
            dark_elixir_after = utils.capture_and_read_text(reg.REGION_DARK_ELIXIR_MY)
            stats.update_stats(0, 0, 0, 0, 0, dark_elixir_after - dark_elixir_before, 0)
            print(f"Dark Elixir collected: {dark_elixir_after - dark_elixir_before}")

    except pyautogui.ImageNotFoundException:
        print("No resource collection button found.")

def cc_reinforce():
    try:
        utils.click(*CC)
        utils.click(*CC_RE)
        utils.click(*CC_CONFIRM)
        utils.click(*EXIT_CC)
        utils.click(*EXIT_CC)
        print("Reinforcing Clan Castle...")
    except pyautogui.ImageNotFoundException:
        print("Clan Castle reinforcement button not found.")

def main():
    print("Starting bot...")
    print("Press 'q' to quit.")
    while True:
        if keyboard.is_pressed('q'):
            print("Exiting...")
            break

        try:
            time.sleep(2)
            collect_resources()
            time.sleep(1)
            

            if utils.find_and_click(f'{ASSETS_DIR}/attack0.png', (95, 776, 172, 164)):
                print("In home, preparing for attack...")
                time.sleep(0.5)
            if utils.find_and_click(f'{ASSETS_DIR}/attack1.png', (1146, 509, 299, 170)):
                print("Starting searching for bases...")

            while True:
                try:
                    if pyautogui.locateOnScreen(f'{ASSETS_DIR}/next.png', region=(1573, 645, 260, 128), confidence=CONFIDENCE) is not None:
                        # base found, now we will check if base is suitable by calculating resource offered by performing ocr
                        # if isSuitableBase():
                        attack.attack_init()
                        break
                        # else:
                        #     print("Base is not suitable, going to next base...")
                        #     utils.find_and_click(f'{ASSETS_DIR}/next.png', (1573, 645, 260, 128))

                except pyautogui.ImageNotFoundException:
                    try:
                        if pyautogui.locateOnScreen(f'{ASSETS_DIR}/attack0.png', region=(95, 776, 172, 164), confidence=CONFIDENCE) is None:
                            print("In home...")
                            break
                    except:
                        try:
                            utils.find_and_click(f'{ASSETS_DIR}/confirm_end_battle.png')
                        except:
                            try:
                                utils.find_and_click(f'{ASSETS_DIR}/return_home.png')
                            except:
                                print("Undefined state, needs fix")

                    print("Searching for bases...")
                    time.sleep(4)

        except pyautogui.ImageNotFoundException:
            print("Idle...")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user. Exiting.")
            stats.display_stats()
        time.sleep(1)

if __name__ == '__main__':
    main()