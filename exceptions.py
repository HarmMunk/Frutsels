
# class StopIteration(Exception):
#     pass

try:
    raise(StopIteration)
except Exception("bla") as exc:
    print(str(exc))
except StopIteration:
    print("Stop iteration")
