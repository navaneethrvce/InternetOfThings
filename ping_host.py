from __future__ import print_function
from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)
from scapy.all import get_if_addr, conf
from commands import getoutput
from multiprocessing import Process
from sys import exit


class PING_SWEEP(object):

  def __init__(self):
    self.ping_sweeper.__init__(self)

  def pinger(self, host_num):
    """thread pinger function"""
    hostadrr = get_if_addr('wlp0s20u12').split('.')[:-1]
    hostadrr = '.'.join(hostadrr) + '.' + repr(host_num)
    line = getoutput("ping -n -c 1 %s 2> /dev/null" % hostadrr)

    while True:
      if line.find(hostadrr) and line.find("bytes from") > -1:  # Host Active
        is_active = []
        is_active.append(hostadrr)
        alive_host = is_active.pop()
        print(alive_host)
        break
      elif line.find(hostadrr) and line.find(
          "Unreachable") > -1:  # No response from host
        not_active = []
        not_active.append(hostadrr)
        not_alive_host = not_active.pop()
        #print("\033[91m No response from \033[0m", not_alive_host)
        break
      else:
        exit(0)

  def ping_sweeper(self):
    for host_num in range(1, 255):
      ping = Process(target=self.pinger, args=(host_num,))
      ping.start()


if __name__ == '__main__':
  try:
    PING_SWEEP().ping_sweeper()
  except KeyboardInterrupt:
    pass

