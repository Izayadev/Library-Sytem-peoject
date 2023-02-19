from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Tools as tool
import Database, DateFile


# Globla Variables

db = Database.ConnectSqlite3()
empty = 0

class DailyMovment():
    
    # Show Daily Books
    def showDailyBooks(self, dailyObjects): # Work with DB --> DailyMovments Table.
        """get the books from database dn load it in the table in the daily movments tab.\n
        dailyObject --> pass a data as dictionary.\n
        data are --> table"""

        # VARIABLES
        table = dailyObjects['table']
        # GET 
        dailyBooks = db.getAll("select book_id, client_id, type, book_from, book_to from daily_movments")

        # CHECK
        if len( dailyBooks ) != empty:
            # CHECK
            tool.showBooksInTable(table, dailyBooks)    
        
        else:
            print("No Books!")

    # Search in daily movment tab
    def getDailyBooksSearch(self,dsObjects) :# Work with DB --> DailyMovment Table.
        """search about a book in daily movment table [tab].\n
        dsObjects (daily search objects) -- > pass as dectionary.\n
        objects are --> search text, table"""

        # VARIABLES
        searchText = dsObjects['search text']
        table = dsObjects['table']

        # SEARCH
        booksFounded = db.getAll("select book_id, type, client_id, Book_from, Book_to from daily_movments where book_id like '%{}%'".format(searchText))

        # NOTIFICATIONS
        print("Searching in Last Daily Movments...")
        print("There are {} books founded".format( len(booksFounded) ))

        # REFRESH
        if len( booksFounded ) != empty:
            
            table.clear()
            tool.showBooksInTable(table, booksFounded)
        else:
            print("No Books")



    # Search in order a book tab --> Workable
    def getOrderTabSearch(self,tabObjects): # Work with DB --> books table.
        """Search about a book and use the result as a data to show it in the table.\n
        tabObject --> pass the objects as a dictionary."""
        # GET
        searchText = tabObjects['search text'].text()
        
        # CHECK
        checkResult = tool.checkFields( {'search text':searchText} )

        if checkResult != empty:

            # SEARCH
            booksFounded = db.getAll("select title, author_id, part_order, price, quantity from books where title like '%{}%'".format(searchText))

            # NOTIFICATIONS
            print("Searching in books...")
            print("There is {} Books founded ".format(len(booksFounded)))

            # REFRESH
            if len( booksFounded ) != empty:

                tool.showBooksInTable(tabObjects['table'], booksFounded)
            else:
                print("No Books")
        

            # OUTPUT
            return booksFounded

    # Get Order Derails
    def getOrderDetails(self,orderObjects): # Work with DB --> Books table.
        """get the data from fields, work in ,check it, then submit it into database.\n
        orderObjects --> tabObject --> pass the objects as a dictionary.\n
        objects are --> empoyee id, branch id, book title, client id, order type, label.\n"""

        # VARIABLES
        employeeID = orderObjects['employee id']
        branchID = orderObjects['branch id']

        bookTitle = orderObjects['book title']
        clientID = orderObjects['client id']
        clientName = tool.getClientName(clientID)
        orderType = orderObjects['order type']

        currentDate = DateFile.dmyDate # the date
        retrieveData = "NONE"

        label = orderObjects['label']




        """=== PROSSES ==="""
        # MESSAGE
        if orderType == 'Rent':
            retrieveData = DateFile.afterDays(7)
            thisMessage = """Dear {}\n
            You Have Ordered the book {},\n
            and you may return it in one week from this date {} .""".format(clientName, bookTitle, retrieveData)
            
            
        else:
            thisMessage = """Dear {}\n
            We Retrieve this book {} from you,\n
            Thank you for visit us  .""".format(clientName, bookTitle)
            
            
        # NOTIFICATION
        label.setText(thisMessage)


        # SUBMIT
        dailyMpvmentsID = db.generateID("select * from daily_movments")
        thisData = [(
            dailyMpvmentsID, bookTitle, clientID, orderType, 
            currentDate, branchID, currentDate, retrieveData,
            employeeID 
        )]
        db.insertManyData("insert into daily_movments values(?,?,?,?,?,?,?,?,?)",thisData)

        historyID = db.generateID("select * from history")
        db.insertManyData("insert into history values(?,?,?,?,?,?)",[
            (historyID, employeeID,
            orderType+" a Book", currentDate,
            branchID, bookTitle)
        ])

        































