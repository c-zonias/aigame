# Weekly Report 1

**Hours worked:** 10

## What did I do this week?
This week I implemented the full core game logic for my Connect4. I completed the Board class, including the grid representation, and legal moves (available columns) as well as piece dropping and undoing moves. Also completed checking if the board is full, draw detection, and winner detection (horizontal, vertical, and both diagonal directions). I also did quick manual tests to verify that moves, undo, and win detection behave correctly.

## How has the program progressed?
The board engine is now complete and stable, which gives me a solid foundation to start building the AI player. The current implementation supports efficient search because I can quickly generate moves and apply/undo actions, and. Overall the project has moved from planning into an actual working implementation of the core mechanics.


## What did I learn this week?
I learned how to implement winner detection efficiently by scanning only valid starting positions to avoid out of bounds mistakes. I also studied why having an undo operation is essential for minimax search, since the algorithm needs to explore many hypothetical move sequences and backtrack quickly.


## What remains unclear or has been challenging?
The most challenging parts were handling edge cases in winner detection and ensuring undo removes the correct piece from a column. Also, while I have manually tested the logic, I still need to formalize these checks into ato unit tests.

## What will I do next?
Next week, I will implement a simple heuristic agent. Then I will start implementing minimax with alpha–beta pruning. I will also add auto tests for winner detection and undo correctness to make sure the game logic remains reliable as I extend the project.