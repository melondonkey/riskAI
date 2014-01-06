class Territory:
    """Defines the territories in the risk board"""

    armies = 0
    occupier = 0
    
    def __init__(self, continent, neighbors):
        self.continent = continent
        self.neighbors = neighbors
    
    def self.changeOccupier(newOccupier):
        self.occupier = newOccupier
        
    def self.changeArmies(changeArmies):
        self.armies = self.armies + changeArmies
        
class Continent:
    """Defines the continents of the board"""
    def __init__(self, name, continent_additional_armies):
        self.name = name 
        self.continent_additional_armies = continent_additional_armies

        
class Player:
    """Defines a Risk Player"""
    def __init__(self, name, color, turn_order):
        self.name = name
        self.color = color
        self.turn_order = turn_order

    is_winner = 0
    
    cards_in_hand = 0
    armies_to_place = 0
    countries_occupied = 0
    continents_controlled = 0
    
    
class RiskCard:
    in_deck = 
    owner =
    soldier_type =
    territory =
    
from random import randint

def roll(dice, sides = 6):
    """Rolls Dice."""
    return [randint(1, sides) for i in range(dice)]

    
def battle(attack_dice, defense_dice)
    attack_roll = roll(attack_dice)
    defense_roll = roll(defense_dice)
    
    stakes = min( len(attack_roll), len(defense_roll) )
    
    attack_roll.sort()
    attack_roll.reverse()
    defense_roll.sort()
    defense_roll.reverse()
    
    for x in xrange(stakes):
        if attack_roll[x - 1] > defense_roll[x-1]:
        
        
class GameBoard:
    def __init__(self, graph)
        self.graph = graph
