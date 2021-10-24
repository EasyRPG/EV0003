# -*- coding: utf8 -*-
"""
log-link.py - Give the correct log file link by date

This sopel plugin is part of EV0003

Copyright 2021, carstene1ns <dev @ f4ke . de>

Licensed under the Eiffel Forum License 2.

https://github.com/EasyRPG/EV0003
"""

from sopel import plugin
from sopel.config import types
import dateparser

class LogLinkSection(types.StaticSection):
  logurl = types.ValidatedAttribute('logurl', default="https://example.com")

def setup(bot):
   bot.settings.define_section('log_link', LogLinkSection)

def configure(config):
   config.define_section('log_link', LogLinkSection)
   config.log_link.configure_setting('logurl', 'Base URL for irc logfiles.')

@plugin.command('log')
@plugin.example('.log yesterday')
@plugin.output_prefix('[irclog] ')
def link_log(bot, trigger):
  """Try to find right log by date"""
  date = trigger.group(2)
  if not date:
    date = "today"

  # throw whatever time spec the user wanted at dateparser module
  requested_date = dateparser.parse(date, settings={'PREFER_DATES_FROM': 'past'})
  if not requested_date:
    bot.reply("I really have no idea which logfile you want…")
    return plugin.NOLIMIT

  bot.say("%s/%s/" % (bot.config.log_link.logurl,
                      requested_date.strftime('%Y/%m/%d')))
