class io():
  def __init__(self):
    print('  [builtin-debug] Debug Package')
  def call(self,message):
    print('i [builtin-debug] Received Message: {}\nChannel: {}'.format(message.content,message.channel))
