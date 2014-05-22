# -*- coding: utf-8 -*-
import player as za_player
import deserializer as deser
import json
import shards

class World:
  players = []
  shards = []
  items = []
  
#игровые методы 
  def add_player(self, player):
    self.players.append(player)
  
  def add_shard(self, shard):
    self.shards.append(shard)
  
  def update(self):
    for p in self.players:
      p.update()

#методы для сохранения, загрузки, и печать ИС в читабельном виде  
  def save_to_json(self, filename):
    with open(filename, 'w') as f:
      json.dump(self.serialize(),f)

  def serialize(self):
    players_serialized = []
    shards_serialized = []
    for p in self.players:
      players_serialized.append(p.serialize())
    for s in self.shards:
      shards_serialized.append(s.serialize())
    a = {u'players': players_serialized, u'shards': shards_serialized}
    return a

  def load_from_json(self, filename):
    with open(filename, 'r') as f:
      self.players = []
      loaded = json.load(f)
      players_loaded_from_json = loaded['players']
      for p in players_loaded_from_json:
        player_to_insert = za_player.Player('')
        player_to_insert.deserialize(p)
        self.players.append(player_to_insert)
      shards_loaded_from_json = loaded['shards']
      for s in shards_loaded_from_json:
        shard_to_insert = shards.shard()

  def print_situation(self):
    for p in self.players:
      print p.printable()
    for s in self.shards:
      print s.printable()

  def connect_shard_to_world(self, player, shard):
    player.shards.append(shard.number)
    shard.owner = player.name