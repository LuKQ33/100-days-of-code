# Blackjack Console Game 🃏

A command-line implementation of the classic Blackjack card game built in Python as part of the **100 Days of Code** challenge.

## Features

- **Infinite Deck Simulation:** Cards are drawn randomly with replacement from a standard card value pool (`[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`).
- **Dynamic Ace Valuation:** Aces automatically adjust from `11` to `1` when the total hand score exceeds `21`.
- **Natural Blackjack Detection:** Two-card `21` hands are identified and prioritized during score evaluation.
- **Automated Dealer Logic:** The dealer draws cards automatically until reaching a minimum score of `17`.
- **Modular Structure:** Game logic is separated into focused functions (`deal_card`, `calculate_score`, `compare_scores`, and `play_game`).

## Project Structure

- `main.py` — Core game loop, scoring logic, and player/dealer turn management.
- `art.py` — ASCII art logo displayed at the start of each round.

## How to Run

1. Make sure you have **Python 3** installed.
2. Clone or download this repository and navigate to the project folder.
3. Run the game from your terminal:

```bash
python main.py
```

## Game Rules Implemented

- Face cards (`J`, `Q`, `K`) are worth `10` points.
- Number cards (`2`–`10`) are worth their face value.
- Aces (`A`) count as `11` unless doing so causes the hand to exceed `21`, in which case they count as `1`.
- Going over `21` results in an immediate loss (bust).
- After the player stands (`'n'`), the dealer draws until reaching at least `17`.