class myClass:
    __privateVAR = 27
    def __privMeth(self):
        print("im inside my class")

    def hello(self):
        print("Private Variable value", myClass.__privateVAR)

foo = myClass()
foo.hello()
foo.__privMeth
#end of program