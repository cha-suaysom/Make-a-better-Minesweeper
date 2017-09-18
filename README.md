# Make-a-better-Minesweeper
For Independent Study with Prof. Omar

## minesweeper.py

A regular minesweeper game. The spot is picked by choosing x,y coordinates. Boardsize and number of bombs can be picked.
This is based on `https://github.com/RaemondBW/Python-Minesweeper/blob/master/minesweeper.py`

## newMinesweeper.py

Based on `minesweeper.py`, this file makes it so that the number instead of showing number of bombs in surrounded 3 X 3 cells (or any cells with distance 1), but a 5 X 5 cell (or any cells with distance 2). This can be useful for later when we look at k-domination number. From some of my experience this is 

## getExpression.py
(There is a way to put latex in markdown I'll figure it out at some point)
Parameter : k,m,n

This file calculate the value of $phi^{-1}_k(l)$ where $phi_k(i,j) = (k+1)i+kj$, then the closest point to the grid $G_{m,n}$ is found. An example in the paper $3,6,6$ is shown. 

Todo: 1. Put this in actual minesweeper board, see what happens.
2. Observe other behavior and comes up with some conjecture

## Note/Observation

1. The number presented in the paper show a configuration of the minimum number of bombs needed in an m X n board so that any non-mine cell in k-minesweeper has positive number. This means that any 'click' will open a mine or only a single cell number, which is very challenging.