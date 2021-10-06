def intToChr(int:int, start:chr = b'\x30') -> chr:
    return chr(int + ord(start)) 

def isOnRange(number, range) -> int:
    if not number in range: raise IndexError("Number must be in range 1-" + range.__len__().__str__() + ", got " + number.__str__())
    else: return int(number)

def current_milli_time() -> int:
    from time import time
    return round(time() * 1000)

def log(msg) -> None:
    from threading import currentThread
    from datetime import datetime
    print("[" + currentThread().name + "(id:" + currentThread().ident.__str__() + ") " + datetime.now().__str__() + "] " + msg)

def empty(*args) -> None:
    pass
