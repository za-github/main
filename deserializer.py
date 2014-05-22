# -*- coding: utf-8 -*-
import player as za
def deserialize_player(player_dict):
  wwaw = za.Player('wwaw')
  for p, val in player_dict.iteritems():
  	wwaw.p = val
  return wwaw