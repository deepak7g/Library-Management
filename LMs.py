import datetime
# import os
# # os.getcwd()


class LMS:
    def __init__(self):
        self.ListOfBooks = "listOfBooks.txt"
        self.bookDict = {}
        Id = 101

        with open(self.ListOfBooks) as bk:
            content = bk.readlines()

        for item in content:
            self.splitContent = item.split()
            self.bookDict.update({str(Id):{"Book Name":self.splitContent[0],"Authour":self.splitContent[1],"Book Status":"Available",
                                                  "Issue Date":"","Lender Name":"","price":10}})
            Id = Id + 1


    def displayBooks(self):
        #This Method used to display books in database(text file)
        print("-----------------------------------Avalaible Books-----------------------------------------------------")
        print("ID","\t\t","Book name","\t\t","Book Authour","\t\t","Book Status","\t\t","Rent per day")
        print("-------------------------------------------------------------------------------------------------------")
        for key,value in self.bookDict.items():
            print(key,"\t\t",value.get("Book Name"),"\t\t",value.get("Authour"),"\t\t",value.get("Book Status"),"\t\t",value.get("price"))
        
    def issueBook(self):
        #This Method used to issue books in database(text file)
        print("----------------------------------------------Pick Books by id-----------------------------------------------------")
        bookId = input("Enter Book ID : ")
        isueDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        if bookId in self.bookDict:
            rentDay = int(input("Enter Renting Days : "))
            if not self.bookDict[bookId]["Book Status"]=="Available":
                print(f'''This book is already issued to {self.bookDict[bookId]['Lender Name']}
on {self.bookDict[bookId]['Issue Date']}''')
            elif self.bookDict[bookId]['Book Status'] == "Available":
                yourName = input("Enter your name to get book : ")
                self.bookDict[bookId]['Lender Name'] = yourName
                self.bookDict[bookId]['Issue Date'] = isueDate
                self.bookDict[bookId]['Book Status'] = "Not Available"
                print("total amount of book rent is",rentDay*self.bookDict[bookId]['price'],"Rupees for ",rentDay,"days")
                self.bookDict[bookId]['price'] = (f"Rented for {rentDay} days")

                print("Books issued successfully!!!!!!")
        else:
            print("Please enter valid Book id")
            return lib.issueBook()
        
    def addBooks(self):
        #This Method used to add new books in database(text file)
        newBooks = input("Enter Book Name : ")
        authourName = input("Enter author Name : ")
        if newBooks == "":
            print("You can't add books as empty")
            return lib.addBooks()
        elif len(newBooks)>20:
            print("it is too lengthy name to add book")
            return lib.addBooks()
        else:
            with open(self.ListOfBooks,"a") as bk:
                bk.writelines(f"{newBooks}\n")
                self.bookDict.update({str(int(max(self.bookDict))+1):{"Book Name":newBooks,"Authour":authourName,"Book Status":"Available",
                                                  "Issue Date":"","Lender Name":"","price":""}})
                print("Book added successfully")

    def returnBook(self):
        #This Method used to add returned books from lender in database(text file)
        returnId = input("Enter Your Book Id : ")
        if returnId in self.bookDict.keys():
            if self.bookDict[returnId]['Book Status'] == 'Available':
                print("This book is already Excisted in library")
            elif not self.bookDict[returnId]['Book Status'] == 'Available':
                self.bookDict[returnId]['Lender Name'] = ""
                self.bookDict[returnId]['Book Status'] = "Available"
                self.bookDict[returnId]["Issue Date"]  = ""
                self.bookDict[returnId ]['price'] = 10
                print("Successfully returned !!!!!!!!!!!!")

        else:
            print("Entered invaild book id ")

lib = LMS()

while True:
    print("""----------------------------------------Welcome to Library Management System------------------------------------------
    Enter d to Display Books
    Enter i to issue book
    enter a to add books
    enter r to return book
    enter q to quit """)
    key = input("Choose : ")
    if key =="d" :
        lib.displayBooks()
    elif key =="i":
        lib.issueBook()
    elif key == "a":
        lib.addBooks()
    elif key == "r":
        lib.returnBook()
    elif key == "q":
        print("----------------------Thank You------------------------")
        break
    else :
        print("--------------------------------------------Please Choose correct option-------------------------------------------")
        continue







