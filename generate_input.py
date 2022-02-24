#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
import sys
import random

from .game.card import *

"""
Generate sample input for build_deck.py
"""

d = deck()
random.shuffle(d)

for card in d:
    print(card.number, card.color)
    print()

