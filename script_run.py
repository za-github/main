# -*- coding: utf-8 -*-
import player as za
import deserializer as deser
import world as world
import json
import shards

za_world = world.World()
za_world.add_player(za.Player(u'ттт'))
za_world.add_player(za.Player(u'Wwaw'))
za_world.update()
za_world.update()
test_shard = shards.shard()
za_world.add_shard(test_shard)

za_world.connect_shard_to_world(za_world.players[0],test_shard)

za_world.save_to_json('test.txt')
za_world.print_situation()
