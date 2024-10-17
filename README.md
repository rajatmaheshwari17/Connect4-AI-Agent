# Connect4-AI-Agent
Connect4-AI-Agent is an AI-driven Connect 4 game implemented in Python. The AI agent is designed to provide a challenging experience to players by making optimal moves using advanced search algorithms like alpha-beta pruning and expectimax. The project is intended to be a fun way to demonstrate AI techniques in a classic board game setting.

Connect 4 is a popular two-player connection game in which players take turns dropping colored discs into a vertically suspended grid. The objective is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. With Connect4-AI-Agent, you can either compete against a highly strategic AI opponent or watch two AI players battle it out.

## Features
- **Alpha-Beta Pruning**: Efficient decision-making using a minimax approach with alpha-beta pruning to reduce the number of nodes evaluated in the search tree.
- **Expectimax Search**: Uses expectimax to provide more dynamic gameplay, especially against unpredictable opponents.
- **Depth-Limited Search**: Limits the depth of the search tree to balance performance and quality of gameplay.
- **Effective Board Evaluation**: Evaluates board states with sophisticated heuristics to determine the optimal move.
- **Human vs AI and AI vs AI**: Play against the AI or watch two AI agents compete.
- **Graphical User Interface**: Includes a simple GUI built using tkinter for an interactive experience.
- **Configurable AI Settings**: Modify search depth and other parameters to adjust the difficulty level of the AI.

## Installation
To get started with Connect4-AI-Agent, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone git@github.com:rajatmaheshwari17/Connect4-AI-Agent.git
   cd Connect4-AI-Agent
   ```

2. **Run the Game**
   ```sh
   python3 ConnectFour.py ai human
   ```

## Usage
You can play the game in different modes:
- **Human vs AI**: Play against the AI by running:
  ```sh
  python ConnectFour.py human ai
  ```
- **AI vs AI**: Watch two AI agents compete by running:
  ```sh
  python ConnectFour.py ai ai
  ```
- **Human vs Human**: Play against another human player:
  ```sh
  python ConnectFour.py human human
  ```

The game interface will show the Connect 4 board, and you can make your moves by entering the column number in the terminal.

## How It Works
The AI agent uses search algorithms to evaluate possible moves and choose the optimal one. The board is represented as a 2D array, and the AI evaluates each possible move to determine which one yields the best outcome.

The game state is updated after each move, and the graphical interface (built with tkinter) displays the current state of the board. The AI evaluates moves based on a combination of maximizing its own chances of winning while minimizing the opponent's opportunities.

## Algorithms
### Alpha-Beta Pruning
Alpha-beta pruning is used to optimize the minimax algorithm by reducing the number of nodes evaluated in the search tree. This allows the AI to make decisions faster while still considering a significant number of possible future moves. Alpha-beta pruning works by eliminating branches in the search tree that are not likely to affect the final decision, thereby significantly improving efficiency.

### Expectimax Search
Expectimax is used when playing against a non-deterministic opponent, such as a random player. It evaluates the expected value of moves rather than assuming the opponent will always play optimally. This approach allows the AI to better adapt to opponents who make unpredictable moves, providing a more realistic and challenging experience.

### Board Evaluation
The evaluation function scores the board based on various factors, such as the number of consecutive pieces in a row (horizontally, vertically, or diagonally) for both the AI and the opponent. The function assigns high values for moves that lead to a win and penalizes moves that allow the opponent to win. The evaluation considers:
- **Center Control**: Favoring moves in the center column to increase chances of forming multiple connections.
- **Blocking Opponent**: Prioritizing moves that block the opponent from winning.
- **Winning Opportunities**: Assigning the highest score to moves that immediately result in a win.

## Graphical User Interface
The game features a simple graphical user interface (GUI) built with tkinter. The GUI displays the Connect 4 board, and players can interact with it to drop their discs into the desired columns. The interface includes:
- **Board Visualization**: The game board is represented visually, with colors indicating each player's discs.
- **Next Move Button**: For AI vs AI mode, a button is available to progress the game one move at a time.
- **Winner Announcement**: At the end of the game, the GUI announces the winner.

## Depth Settings
Currently, the AI search depth is set to **3**. A higher depth allows the AI to evaluate more possible moves, leading to better decision-making and a more challenging opponent. However, increasing the depth also significantly increases the processing time, which can make the game feel slow or cause the UI to become unresponsive. For the best balance between performance and difficulty, the default depth is set to 3, but you can adjust it in the code if you wish to experiment with more advanced AI behavior.

**Note:** Increasing the depth beyond 4 or 5 may cause longer delays, especially on devices with limited RAM or processing power.


## 
_This README is a part of the Connect4-AI-Agent Project by Rajat Maheshwari._

