if __name__ == "__main__":
    import sys
    for arg in  sys.argv:
        print(arg)

def AAA(*arg1,**arg2):
    print("arg1 = ",arg1)
    print("arg2 = ",arg2)
 

AAA(1,2,3,4,name="alex",age=3)
