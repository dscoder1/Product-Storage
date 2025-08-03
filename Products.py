import mysql.connector
import pymongo
import datetime
import time

# Database Setup

class Products:
    def add(self):
        self.PrdId=int(input("\nEnter Product Id:"))
        self.PrdName=input("\nEnter Product Name:")
        self.PrdDesc=input("\nEnter Product Description:")
        self.PrdCost=float(input("\nEnter Product Cost:"))
        cur.execute("insert into ProductsDetails values({},'{}','{}',{},'{}','{}')".format(self.PrdId,self.PrdName,self.PrdDesc,self.PrdCost,datetime.datetime.now(),datetime.datetime.now()))
        conn.commit()
        data={'Product Id':self.PrdId,'Product Name':self.PrdName,'Product Description':self.PrdDesc,'Product Cost':self.PrdCost,'Product Entry':datetime.datetime.now()}
        coll.insert_one(data)
        print("\nData Inserted In Both MySql and Mongo DB")

    def showAll(self):
        cur.execute("select * from productsdetails")
        allData=cur.fetchall()
        print(allData)
        for data in allData:
            print(data)
            print("\nProducts Id : ",data[0])
            print("\nProducts Name : ",data[1])
            print("\nProducts Description : ",data[2])
            print("\nProducts Cost : ",data[3])
            print("\nProducts Entry Time : ",data[4])
            print("\n-----------------------------\n")

        collection=coll.find({})
        print(collection)
        for docs in collection:
            print(docs)
            print("\nProducts Id : ",docs['Product Id'])
            print("\nProducts Name : ",docs['Product Name'])
            print("\nProducts Description : ",docs['Product Description'])
            print("\nProducts Cost : ",docs['Product Cost'])
            print("\nProducts Entry Time : ",docs['Product Entry'])
            print("\n-----------------------------\n")

    def showOne(self):
        ProductId=int(input("\nEnter Product Id : "))
        cur.execute("select * from productsdetails where ProductId={}".format(ProductId))
        data=cur.fetchone()
        if(data!=None):
            print("\nProducts Id : ",data[0])
            print("\nProducts Name : ",data[1])
            print("\nProducts Description : ",data[2])
            print("\nProducts Cost : ",data[3])
            print("\nProducts Entry Time : ",data[4])
            print("\n-----------------------------\n")
        else:
            print("\nProduct Not Available")

        collection=coll.find_one({'Product Id':ProductId})
        if(collection!=None):
            print("\nProducts Id : ",collection['Product Id'])
            print("\nProducts Name : ",collection['Product Name'])
            print("\nProducts Description : ",collection['Product Description'])
            print("\nProducts Cost : ",collection['Product Cost'])
            print("\nProducts Entry Time : ",collection['Product Entry'])
            print("\n-----------------------------\n")
        else:
            print("\nProduct Not Available")

    def deleteOne(self):
        ProductId=int(input("\nEnter Product Id : "))
        cur.execute("select * from productsdetails where ProductId={}".format(ProductId))
        data=cur.fetchone()
        if(data!=None):
            cur.execute("delete from productsdetails where ProductId ={}".format(ProductId))
            conn.commit()
            print("\nDeleted Product Is : \n")
            print("\nProducts Id : ",data[0])
            print("\nProducts Name : ",data[1])
            print("\nProducts Description : ",data[2])
            print("\nProducts Cost : ",data[3])
            print("\nProducts Entry Time : ",data[4])
            print("\n-----------------------------\n")
        else:
            print("\nProduct Not Available")

        collection=coll.find_one({'Product Id':ProductId})
        if(collection!=None):
            deletedData=coll.find_one_and_delete({'Product Id':ProductId})
            print("\nDeleted Product Is : \n")
            print("\nProducts Id : ",deletedData['Product Id'])
            print("\nProducts Name : ",deletedData['Product Name'])
            print("\nProducts Description : ",deletedData['Product Description'])
            print("\nProducts Cost : ",deletedData['Product Cost'])
            print("\nProducts Entry Time : ",deletedData['Product Entry'])
            print("\n-----------------------------\n")
        else:
            print("\nProduct Not Available")
            
    def updateOne():
        pass
    
print("\nEnter What You Want To Do :\n1.Add Products\n2.Show All Products\n3.Show Single Product By Id\n4.Delete Product By Id\n4.Update Product By Id\n5.Exit From Application\n")
Choice=int(input("\nEnter Your Choice: "))
while(Choice!=5):
    if(Choice==1):
        Obj=Products().add()
        Choice=int(input("\nEnter Your Choice: "))
    elif(Choice==2):
        Obj=Products().showAll()
        Choice=int(input("\nEnter Your Choice: "))
    elif(Choice==3):
        Obj=Products().showOne()
        Choice=int(input("\nEnter Your Choice: "))
    elif(Choice==4):
        Obj=Products().deleteOne()
        Choice=int(input("\nEnter Your Choice: "))
    elif(Choice==5):
        Obj=Products().updateOne()
        Choice=int(input("\nEnter Your Choice: "))
    else:
        pass


