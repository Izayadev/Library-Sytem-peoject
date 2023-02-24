from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Tools as tool
import Database, DateFile


# Globla Variables

db = Database.ConnectSqlite3()
empty = 0
adminAccess = 0
reusedData = ()

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
            tool.showDataInTable(table, dailyBooks)    
        
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
            tool.showDataInTable(table, booksFounded)
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

                tool.showDataInTable(tabObjects['table'], booksFounded)
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

        
class BookTab():

    # Get bookd from database and show in the table widget.
    def getAllBooks(self, thisObjects):
        """After get book, show it, return notification.\n
        thisObjects --> pass as dictionary.\n
        Objects are --> branch id, table"""

        # VARIABLES
        branchAccess = thisObjects['branch id'] 
        table = thisObjects['table']
        

        # TABLE DATA
        if branchAccess == adminAccess:
            booksData = db.getAll("select code, title, category_id, author_id, price from books")

        else:
            booksData = db.getAll("select code, title, category_id, author_id, price from books where Branch = {}".format(branchAccess))


        # INSERT
        tool.showDataInTable(table, booksData)

        # NOTIFICATIONS
        print("Books loaded in the screen!")        


    # Search about a book via title, author.
    def searchAboutBook(self, thisObjects):
        """U can search via title, author and an other useful data.\n
        thisObjects --> pass data as dictionary.\n
        objects are --> search text, table, branch id"""

        # VARIABLES 
        branchAccess = thisObjects['branch id']
        searchText = thisObjects['search text']
        table = thisObjects['table']
        sqlQuery = """select code, title, category_id, author_id, price from books
        where title like '%{0}%' or category_id like '%{0}%' or author_id like '%{0}%' or description like '%{0}%'"""
        
        
        # GET
        if branchAccess == adminAccess:
            bookFounded = db.getAll( sqlQuery.format(searchText) )

        else:
            bookFounded = db.getAll( sqlQuery.format(searchText)+' and Branch = {}'.format(branchAccess) )

        # NOTIFICATIONS
        print("There are {} books founded".format( len(bookFounded) ))


        
        # SHOW
        if len(bookFounded) == empty:
            print("No book founded!")
        else:
            table.clearContents()
            tool.showDataInTable(table, bookFounded)

    # Submit those data to add a new book.
    def submitNewBook(self, thisObjects):
        """Get book details, save it, load it, notification cutomers\n
        thisObjects are a dictioanry data type pass thoses data in order(11 elemnts)\n
        title, description, author, category, publisher, part, price, code, barcode, status, quantity, image, branch id, employee id
        """

        # VARIABLES
        bookTitle = thisObjects['title']
        bookDescription = thisObjects['description']
        bookAuthor = thisObjects['author']
        bookCategory = thisObjects['category']
        bookPublisher = thisObjects['publisher']
        bookPart = thisObjects['part']
        bookPrice = thisObjects['price']
        bookCode = thisObjects['code']
        bookbarcode = thisObjects['barcode']
        bookStatus = thisObjects['status']
        bookQuantity = thisObjects['quantity']
        bookImage = thisObjects['image']

        currentDate = DateFile.dmyDate

        bookID = db.generateID("select * from books")
        branchID = thisObjects['branch id']
        employeeID = thisObjects['employee id']

        # SAVE IN DATABASE        
        db.insertManyData("insert into books values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[(
            bookID, bookTitle, bookDescription, bookCategory,
            bookCode, bookbarcode, bookPart,
            bookPrice, bookPublisher, bookAuthor,
            bookStatus, currentDate, bookQuantity, branchID, bookImage
        )])

        # SAVE ACTION
        tool.SaveActionToHistory({'action':"Add new Book", 'extra':bookTitle, 'branch id':branchID, 'employee id':employeeID})

        # NOTIFICATIONS
        print("The new book {} added".format(bookTitle) )

    # Submit those Edit book.
    def submitEditBook(self, thisObjects):
        """Load data in fields, handle changes, svae it.\n
        thisObjects is a dictionary data type take those arguments\n
        book code, branch id, book title, book part, book image,
        book quantity, book author, book description, book category, 
        book publisher, book price, book code, pixmap"""

        
        # VARIABLES
        bookSearch = thisObjects['book search']; branchID = thisObjects['branch id']
        bookCode = thisObjects['book code']; 
        bookTitle = thisObjects['book title']
        bookPart = thisObjects['book part']; bookImage = thisObjects['book image']
        bookQuantity = thisObjects['book quantity']; bookAuthor = thisObjects['book author']
        bookDescription = thisObjects['book description']; bookCategory = thisObjects['book category']
        bookPublisher = thisObjects['book publisher']; bookPrice = thisObjects['book price']
        pixmap = thisObjects['pixmap']; bookStatus = thisObjects['book status']

        # indexies
        title=1; desciption=2; category=3; 
        code=4; part=6; price=7; publisher=8; author=9 ;
        status=10; quantity=12; image = 14

        

        # GET 
        if branchID == adminAccess:
            sqlQuery = "select * from books where code like {}".format( bookSearch.text() )

        else:
            sqlQuery = "select * from books where code like {} and Branch = {}".format(bookSearch.text(), branchID)
        
        thisBookData = db.getOne(sqlQuery)

        # CHECK
        if len( thisBookData ) == empty:
            print("Wrong!!... There is no book has this {} code".format( bookSearch.text() ))

        elif len( thisBookData ) != empty:
            
            # Load data to fields
            bookTitle.setText(thisBookData[title])
            bookDescription.setPlainText(str(thisBookData[desciption]))

            bookCategory.setCurrentIndex(thisBookData[category])
            bookPrice.setText(str(thisBookData[price]))

            bookCode.setText(thisBookData[code])
            bookPublisher.setCurrentIndex(thisBookData[publisher])

            bookAuthor.setCurrentIndex(thisBookData[author])
            bookPart.setText(str(thisBookData[part]))

            bookQuantity.setText(str(thisBookData[quantity]))
            bookStatus.setCurrentText(thisBookData[status])

            codeID = bookSearch.text()
            # Get a binary image
            imageUrl = thisBookData[image]

            # Open The Image 
            pixmap = QPixmap(imageUrl)

            # Add Image to Label
            bookImage.setPixmap(pixmap)


            # NOTIFICATION
            print("{} Loaded to edit..".format( bookTitle.text() ))

            # RETURN to REUSE
            global reusedData
            reusedData = (
                bookTitle, bookDescription, bookCategory,
                bookCode, bookPart, bookPrice,
                bookPublisher, bookAuthor, bookStatus,
                bookQuantity, codeID
            )


            

    # Submit change to database
    def submitChange(self):
        """Variable reused declayering in submitEditBook Function and set to be global."""

        # INDEXIES
        title = 0; desciption = 1; category = 2;
        code = 3; part = 4; price = 5;
        publisher = 6; author = 7; status = 8;
        quantity = 9; code2 = 10;

        # UPDATE 
        updateSqlQuery = """update books
                set title = '{0}',
                description = '{1}',
                category_id = {2},
                code = '{3}',
                part_order = {4},
                price = '{5}',
                publisher_id = {6},
                author_id = {7},
                status = '{8}',
                quantity = {9}
                where code = {10}
                """.format(
                    reusedData[title].text(), reusedData[desciption].toPlainText(), reusedData[category].currentIndex(),
                    reusedData[code].text(), reusedData[part].text(), reusedData[price].text(),
                    reusedData[publisher].currentIndex(), reusedData[author].currentIndex(), reusedData[status].currentIndex(),
                    reusedData[quantity].text(), reusedData[code2]
                )
                
                
        db.updateData(updateSqlQuery)

        print("Hai done!")

        




















