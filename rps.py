#!/usr/bin/env python3
from enum import Enum
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

# Print terminal colors for python was taken from
# https://www.geeksforgeeks.org/print-colors-python-terminal/


def prScores(skk):
    print("\033[91m {}\033[00m" .format(skk))


def prTie(skk):
    print("\033[93m {}\033[00m" .format(skk))


def prWin(skk):
    print("\033[92m {}\033[00m" .format(skk))


class Player:
    def move(self):
        return Move.ROCK.value

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return Move.ROCK.value


def beats(one, two):
    return two in {
        'rock': ['scissors'],
        'scissors': ['paper'],
        'paper': ['rock']
    }.get(one, [])


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score1 += 1
            prWin("Player 1 wins!")
        elif beats(move2, move1):
            self.score2 += 1
            prWin("Player 2 wins!")
        else:
            prTie("Tie!")
        prScores("Current scores:")
        prScores(f"Player 1: {self.score1}")
        prScores(f"Player 2: {self.score2}\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while True:
            try:
                rounds = int(input("How many rounds would"
                                   " you like to play? > "))
                break
            except ValueError:
                print("Invalid input. Try again.")
        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print("General scores:")
        print(f"Player 1: {self.score1}")
        print(f"Player 2: {self.score2}")
        if self.score1 > self.score2:
            prWin("Player 1 won the game!")
        elif self.score2 > self.score1:
            prWin("Player 2 won the game!")
        else:
            prTie("The game is a tie!")


class RandomPlayer(Player):
    def move(self):
        return random.choice(Move.moves())


class Move(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    @classmethod
    def moves(cls):
        return [e.value for e in cls]


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, or scissors? > ").lower()
            if move in Move.moves():
                return move
            else:
                print("Invalid move. Try again.")


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(Move.moves())
        else:
            return self.their_move

    def learn(self, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return random.choice(Move.moves())
        else:
            if self.my_move == 'rock':
                return 'paper'
            elif self.my_move == 'paper':
                return 'scissors'
            else:
                return 'rock'

    def learn(self, my_move):
        self.my_move = my_move


if __name__ == '__main__':
    opponents = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(opponents)
    game = Game(p1, p2)
    game.play_game()
