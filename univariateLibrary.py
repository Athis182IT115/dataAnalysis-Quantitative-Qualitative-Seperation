class univariateClass():#step--5 making it into class so that we can make it libraray and import
                       #it any where needed
    def QuanQual(self,dataset):#step--4 converting it into function
        Quan=[]#step--1 creating list to store our quantitative and 
        Qual=[]#qualitative columns
        for columnName in dataset.columns:# step--2 writing optimised code ie working for all datasets
            if(dataset[columnName].dtype=="int64" or dataset[columnName].dtype=="float64" ):
                Quan.append(columnName)
            else:
                Qual.append(columnName)
        return Quan,Qual# step--3 returning Quan,Qual
#step--6 Make it into .py file for importing 