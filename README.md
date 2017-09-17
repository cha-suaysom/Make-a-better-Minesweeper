# Make-a-better-Minesweeper
For Independent Study with Prof. Omar

## minesweeper.py

A regular minesweeper game. The spot is picked by choosing x,y coordinates. Boardsize and number of bombs can be picked.
This is based on `https://github.com/RaemondBW/Python-Minesweeper/blob/master/minesweeper.py`

## newMinesweeper.py

Based on `minesweeper.py`, this file makes it so that the number instead of showing number of bombs in surrounded 3 X 3 cells (or any cells with distance 1), but a 5 X 5 cell (or any cells with distance 2). This can be useful for later when we look at k-domination number. From some of my experience this is 

## Note/Observation

1. The number presented in the paper show a configuration of the minimum number of bombs needed in an m X n board so that any non-mine cell in k-minesweeper has positive number. This means that any 'click' will open a mine or only a single cell number, which is very challenging.