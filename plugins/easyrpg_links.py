"""
easyrpg_links.py - Shortcuts for the EasyRPG homepage and GitHub

This sopel plugin is part of EV0003

Copyright 2014-2021, carstene1ns <dev @ f4ke . de>

Licensed under the Eiffel Forum License 2.

https://github.com/EasyRPG/EV0003
"""
from __future__ import generator_stop

from sopel import plugin

@plugin.command('bugs')
@plugin.example('.bugs liblcf')
def link_bugs(bot, trigger):
  project = trigger.group(2)
  # TODO: iterate over all projects to find the right
  if not project:
    bot.reply("You need to provide a project!")
    return plugin.NOLIMIT
  # CT: no checking, YOLO
  bot.reply("https://github.com/EasyRPG/%s/issues" % project)

@plugin.command('web')
def link_web(bot, trigger):
  bot.reply("https://easyrpg.org/")

@plugin.command('blog')
def link_blog(bot, trigger):
  bot.reply("https://blog.easyrpg.org/")

@plugin.command('forums', 'community')
def link_forums(bot, trigger):
  bot.reply("https://community.easyrpg.org/")

@plugin.command('jenkins', 'ci')
def link_jenkins(bot, trigger):
  bot.reply("https://ci.easyrpg.org/")

@plugin.command('twitter')
def link_twitter(bot, trigger):
  bot.reply("https://twitter.com/easyrpg/")

@plugin.command('facebook')
def link_facebook(bot, trigger):
  bot.reply("https://www.facebook.com/easyrpgofficial/")

@plugin.command('instagram')
def link_instagram(bot, trigger):
  bot.reply("https://www.instagram.com/easyrpg_org/")

@plugin.command('paste')
def link_paste(bot, trigger):
  bot.reply("https://gist.github.com/ (please sign in before pasting if the content is relevant)")
