import sys
from pprint import pprint

if __name__ == "__main__" and __package__ in [None, ""]:
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../..")

    __package__ = "chatbots.subfolder1"


from ..subfolder2.module_2_1 import say_hello

pprint(sys.path)


say_hello()

""" if __name__ == "__main__" and __package__ in [None, ""]:
    import os
    import sys
    print("in main")
    print(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
    __package__ = "subfolder1"



import pprint
import sys

pprint.pprint(sys.path)

print(f"packge is {__package__}")

from .module1_1 import say_hello

say_hello()
 """
