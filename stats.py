
GOLD_FARMED = 0
ELIXIR_FARMED = 0
DARK_ELIXIR_FARMED = 0

GOLD_COLLECTED = 0
ELIXIR_COLLECTED = 0
DARK_ELIXIR_COLLECTED = 0

TROPHIES = 0

def display_stats():
    print("Farming Stats:")
    print(f"Gold Farmed: {GOLD_FARMED}")
    print(f"Elixir Farmed: {ELIXIR_FARMED}")
    print(f"Dark Elixir Farmed: {DARK_ELIXIR_FARMED}")
    print(f"Gold Collected: {GOLD_COLLECTED}")
    print(f"Elixir Collected: {ELIXIR_COLLECTED}")
    print(f"Dark Elixir Collected: {DARK_ELIXIR_COLLECTED}")
    if(TROPHIES > 0):
        print(f"Trophies gained: {TROPHIES}")
    else:
        print(f"Trophies lost: {-TROPHIES}")

def update_stats(gold_farmed, elixir_farmed, dark_elixir_farmed, gold_collected, elixir_collected, dark_elixir_collected, trophies):
    global GOLD_FARMED, ELIXIR_FARMED, DARK_ELIXIR_FARMED
    global GOLD_COLLECTED, ELIXIR_COLLECTED, DARK_ELIXIR_COLLECTED
    global TROPHIES

    GOLD_FARMED += gold_farmed
    ELIXIR_FARMED += elixir_farmed
    DARK_ELIXIR_FARMED += dark_elixir_farmed
    GOLD_COLLECTED += gold_collected
    ELIXIR_COLLECTED += elixir_collected
    DARK_ELIXIR_COLLECTED += dark_elixir_collected
    TROPHIES += trophies