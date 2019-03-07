from mypackage import *

# If mypackage/__init__.py is left blanck,
# you need the following imports
#
# from mypackage.mymultis import *
# from mypackage.mysums import *

if __name__ == "__main__":

    print("Test summing")
    print(sumTwoNums(2,3))

    print("Test multiplying")
    print(multi2(3))
    print(multi3(3))
