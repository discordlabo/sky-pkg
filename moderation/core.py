class io():
  def __init__(self,version,bot=None):
    self.version = version
    self.bot = bot
    self.name = 'Warning System 0.1.0 Stable'
  def call(self,message):
    if message.content.startswith(':warn/'):
      yield from bot.send_message(message.channel,':warning: Warning Feature is not available now. :pensive:')
    elif message.content.startswith(':ban/'):
      yield from bot.send_message(message.channel,':warning: Ban Feature is not available now. :pensive:')
    elif message.content.startswith(':kick/'):
      yield from bot.send_message(message.channel,':warning: Kick Feature is not available now. :pensive:')
    elif message.content.startswith(':reset/'):
      yield from bot.send_message(message.channel,':warning: Reset Feature is not available now. :pensive:')
  def name(self):
    reurn self.name
