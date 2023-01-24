from turtle import Turtle
from abc import ABCMeta, abstractmethod


class Sprite(Turtle, metaclass=ABCMeta):
    """Base sprite"""
    @abstractmethod
    def __init__(self):
        super().__init__(shape='circle')

    @abstractmethod
    def move(self):
        pass
