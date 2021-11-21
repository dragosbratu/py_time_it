import time
   
class timeit():
    from datetime import datetime
    def _enter_(self):
        self.tic = self.datetime.now()
        print("Start time {}".format(self.tic.strftime("%H:%M:%S %d/%m/%Y")))
    def _exit_(self, *args, **kwargs):
        self.tock = self.datetime.now()
        print('runtime: {}'.format(self.tock - self.tic))
        print("End time {}".format(self.tock.strftime("%H:%M:%S %d/%m/%Y")))

t = timeit()

t._enter_()
print("Time it!")
t._exit_()

t._enter_()
time.sleep(3)
t._exit_()

t._enter_()
for x in range(10_000_000):
  a = x+1
print("Time it long time")
t._exit_()
