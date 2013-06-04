#-*- coding:utf-8 -*- 
import Queue
import types
import threading
from contextlib import contextmanager

class ObjectPool(object):

    def __init__(self, fn_cls, *args, **kwargs):
        super(ObjectPool, self).__init__()
        self.fn_cls = fn_cls
        self._myInit(*args, **kwargs)
    
    def _myInit(self, *args, **kwargs):
        self.args = args
        self.maxSize = int(kwargs.get("maxSize",1))
        self.queue = Queue.Queue()
    def _getObj(self):
        if type(self.fn_cls) == types.FunctionType:
            return self.fn_cls(self.args)
        elif type(self.fn_cls) == types.ClassType or type(self.fn_cls) == types.TypeType:
            return apply(self.fn_cls, self.args)
        else:
            raise "Wrong type"
  
    def borrowObj(self):
        print self.queue._qsize()
        if self.queue.qsize()<self.maxSize and self.queue.empty():
            self.queue.put(self._getObj())
        return self.queue.get() 
  
    def returnObj(self,obj):
        self.queue.put(obj)
    
def echo_func(num):
    return num

class echo_cls(object):
    pass
@contextmanager
def poolObj(pool):
    obj = pool.borrowObj()
    try:
        yield obj
    except Exception, e:
        yield None
    finally:
        pool.returnObj(obj)

obj = ObjectPool(echo_func, 23, maxSize=4)
obj2 = ObjectPool(echo_cls, maxSize=4)

class MyThread(threading.Thread):

    def run(self):
        with poolObj(obj) as t:
            print t
        with poolObj(obj2) as t:
            print t

if __name__ == '__main__':
    threads = []
    for i in range(200):
        t = MyThread()
        t.start()
        threads.append(t)
    for t in threads:
        t.join(True)
