"""
asciifood.py - Just delicious

This sopel plugin is part of EV0003

Copyright 2014-2021, carstene1ns <dev @ f4ke . de>

Licensed under the Eiffel Forum License 2.

https://github.com/EasyRPG/EV0003
"""
from __future__ import generator_stop

from sopel import plugin

import inspect

@plugin.command('beer')
@plugin.rate(channel = 60)
def beer(bot, trigger):
  """Pours some beers."""
  beers = """
       .:.      .:.         .:.
     _oOoOo   _oOoOo       oOoOo_
    [_|||||  [_|||||       |||||_]
      |||||    |||||       |||||
      ~~~~~    ~~~~~       ~~~~~
  """
  for line in inspect.cleandoc(beers).splitlines():
    bot.say(line)

@plugin.command('pizza')
@plugin.rate(channel = 60)
def pizza(bot, trigger):
  """Gives out some cheesy pizza."""
  pizza = """
     //\"\"\"--.._
    ||  (_)  _ "-._      PPPPP IIII ZZZZZ ZZZZZ    A
    ||    _ (_)    '-.   PP  PP II    ZZ    ZZ    A A
    ||   (_)   __..-'    PPPPP  II   ZZ    ZZ    AAAAA
     \\\\__..--""          PP    IIII ZZZZZ ZZZZZ A     A
  """
  for line in inspect.cleandoc(pizza).splitlines():
    bot.say(line)

@plugin.command('coffee')
@plugin.rate(channel = 60)
def coffee(bot, trigger):
  """Exactly what you need."""
  coffee = """
      ;)( ;
     :----:
    C|====|
     |    |
     `----'
  """
  for line in inspect.cleandoc(coffee).splitlines():
    bot.say(line)
