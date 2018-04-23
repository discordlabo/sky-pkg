class io():
  def __init__(self,version):
    print('  [builtin-debug] Debug Package')
  def call(self,message):
    print('i [builtin-debug] Received Message: {}\nChannel: {}'.format(message.content,message.channel))
  def name(self):
    return 'Debug'
