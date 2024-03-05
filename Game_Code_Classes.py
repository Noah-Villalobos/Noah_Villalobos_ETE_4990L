#!/usr/bin/env python
# coding: utf-8

# In[135]:


import random

class CardType:
    def __init__(self, card, effect):
        self.card = card
        self.effect = effect

        
class Attack(CardType):
    def __init__(self, card, effect, damage):
        super().__init__(card, effect)
        self.damage = damage

    def do_damage(self, target):
        target.take_damage(self.damage)
        print('You used an attack!')
        
        
class Defense(CardType):
    def __init__(self, card, effect, protection):
        super().__init__(card, effect)
        self.protection = protection

    def protect(self, target):
        target.get_protection(self.protection)
        print("You used a shield!")

        
class Rejuvinate(CardType):
    def __init__(self, card, effect, healing):
        super().__init__(card, effect)
        self.healing = healing
        
    def heal(self, target):
        target.get_healed(self.healing)
        ("You have been healed!")

        
class Deck:
    def __init__(self):
        self.cards = []

    def generate_deck(self):
        deck_size = 10
        for i in range(deck_size):
            card_type = random.choice([Attack, Defense, Rejuvinate])
            if card_type == Attack:
                card = Attack
            elif card_type == Defense:
                card = Defense
            else:
                card = Rejuvinate
            self.cards.append(card)
            print(self.cards)
            
            
class DiscardPile:
    
            
class Hand:
    def __init__(self):
        self.cards = []
        
    def draw_hand(self):
        hand_size = 5
        for i in range(hand_size):
            drawn_card = Deck.cards.pop(0)
            self.cards.append(drawn_card)
        print(Deck.cards)
        print(self.cards)
         
            
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.old_health = health
        self.protection = 0
        
    def take_damage(self, damage):
        effective_damage = max(damage - self.protection, 0)  
        new_health = self.health - effective_damage
        if new_health < self.old_health:  
            self.old_health = self.health  
            self.health = max(new_health, 0)
            if self.health <= 0: 
                print(Player.name, Player.health)
                print('You are dead!')
            else:
                print(Player.name, Player.health)
                print('You took damage!')
        else:
            print(Player.name, Player.health)
            print('You have been protected!')
        
        
    def get_protection(self, protection):
        self.protection = max(protection, self.protection)
        
    def get_healed(self, healing):
        self.health += healing
        print(Player.name, Player.health)
        print('You have been healed!')


# In[136]:


Player = Player(input(), 100)
print(Player.name, Player.health)


# In[137]:


Attack = Attack('Attack', 'do damage', 20)
Defense = Defense('Shield', 'protect', 15)
Rejuvinate = Rejuvinate('Revive', 'heal',5)
Deck = Deck()
Hand = Hand()
DiscardPile = DiscardPile()


# In[ ]:




