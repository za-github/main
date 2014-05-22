# -*- coding: utf-8 -*-
import codecs
class Player(object):
  def __init__(self, name):
    self.name = name
    self.energy = 10
    self.income = 6
    self.defence = float(32)
    self.shards = []
  
  def set_name(self, name):
  	self.name = name
  
  def update(self):
    self.defence = self.defence/2
    self.energy = self.energy + self.income
  
  def printable(self):
    a1 = 'Игрок: '.decode('utf-8') + self.name + '\n' + 'Энергия: '.decode('utf-8') + str(self.energy) + '\n'+ \
        'Доход: '.decode('utf-8') + str(self.income) + '\n' + 'Защита: '.decode('utf-8') + str(self.defence) + '\n'+ \
        'Осколки: '.decode('utf-8') + str(self.shards) + '\n';
    return a1;
  
  def serialize(self):
    return {u'name': self.name, 'energy': str(self.energy), 'income':str(self.income), 'defence': str(self.defence),
        'shards': str(self.shards)}
  
  def deserialize(self, dict_dump):
  	for key in dict_dump:
  	  self.key = dict_dump[key]




