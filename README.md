# PySudoku: A Python Sudoku Solver and Generator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/betty-godier/sudoku-solveur-generator/blob/master/LICENSE)

A Sudoku generator and solver using the Pygame library. Sudoku is a popular logic-based number placement puzzle, and this project aims to provide a user-friendly interface for both generating new Sudoku puzzles and solving existing ones.

## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Instructions](#instructions)
- [License](#license)

## Introduction

This repository contains a Python implementation of a Sudoku generator and solver using the Pygame library. Sudoku is a well-known logic-based puzzle that requires players to fill a 9x9 grid with numbers so that each row, column, and 3x3 subgrid contains all the digits from 1 to 9 without repetition.
## Key Features

-Generate new Sudoku puzzles with varying levels of difficulty.
-Allow players to interactively solve Sudoku puzzles using a user-friendly interface.
-Implement a backtracking algorithm to efficiently solve the puzzles.
-Check for the validity of entered numbers according to Sudoku rules

## Instructions

1. Clone or download this repository to your local machine.
2. Make sure you have Python 3.x installed on your system.
3. Install the Pygame library using pip:
pip install pygame
4. Run the main.py script to start the Sudoku game.
5. Use the arrow keys to navigate to the desired cell.
6. Press the number keys (1 to 9) to enter a value in the selected cell.
7. Press the Enter key to confirm the entered value and view it in the cell.
8. If the entered value violates the Sudoku rules (duplicate numbers in the same row, column, or 3x3 subgrid), an error message will be displayed briefly.
9. Press the 'R' key to erase a value from the selected cell.
10. Press the 'D' key to reset the puzzle to its initial state.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
