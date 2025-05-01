# """
# Intent:
# The Singleton pattern is to make sure that the there is no more than one instance of 
# class is getting created at any given point in time.
# 
# When to Use:
# -> You want to ensure only one instance of a class exists throughout the 
#    application's lifecycle. Ex. Logger, Config Manager, Print Spooler
# -> You want controlled, global access to an instance — like a shared resource 
#    that all parts of your app should use. like DB connection
# -> When all parts of the application need to operate on the same state/data.
# 
# """

# __new__() Method Implmentation
class DBConn():
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

conn1 = DBConn()
conn2 = DBConn()
print(conn1, conn2)


# Decorator Implementation
def Singleton(cls):
    instances = {}
    def inner(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return inner

@Singleton
class DBConn:
    def __init__(self):
        print('New instance created')

conn1 = DBConn()
conn2 = DBConn()
print(conn1, conn2)

# Thread safe class implementation
import threading

class DBConn:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
