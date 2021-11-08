class myName:
    def __init__(self,firstN,lastN):
        self.fName = firstN
        self.lName = lastN

    def fullname(self):
        self.full_name = self.fName + self.lName
        return(self.full_name)
    def address(self):
        myfullname = self.fullname()
        #print(myfullname)
        return(myfullname)

myobj = myName("mustafa","al_ogaidi")
print(myobj.address())
