# -*- coding: utf-8 -*-
class shard(object):
  def __init__(self):
    self.name = u''
    self.height = int()
    self.defence  = 0
    self.owner = u'neutral'
    self.perks = []
    self.trophies = []
    self.tactic = u'warrior'
    self.number = 666
    self.description = u''
  
  def set_name(self, name):
    self.name = name
  
  def set_height(self, height):
  	self.height = height
  
  def set_defence(self, defence):
  	self.defence = defence
    
  def serialize(self):
    return {u'name': self.name, 'height': str(self.height), 'defence':str(self.defence), 'owner': self.owner, \
    'perks': str(self.perks), 'trophies': str(self.trophies), 'tactic': str(self.tactic), 'number': str(self.number), \
    'description': str(self.description)}

  def printable(self):
    a1 = str(self.number) +'. Осколок: '.decode('utf-8') + self.name + '\n' + 'Высота: '.decode('utf-8') + str(self.height) + '\n'+ \
        'Защита: '.decode('utf-8') + str(self.defence) + '\n' + 'Особенности: '.decode('utf-8') + str(self.perks) + '\n';
    return a1;