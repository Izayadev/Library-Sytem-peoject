from calendar import day_name
from csv import excel
from curses import window
from datetime import datetime
from distutils.log import error
from email.policy import EmailPolicy
from enum import EnumMeta
from pydoc import allmethods
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sys , sqlite3 , Tools, login_frame, Database, TabWidget, ExcelFiles
# from xlsxwriter import *


MainUI,_ = loadUiType('main.ui')
""" Handle Classes"""
hpTool = TabWidget.DailyMovment()
helpTool = TabWidget


database = Database.ConnectSqlite3()
print("Connected to Database.")

""" Gloabl Variable"""
empty = 0 # to use in if statements.

# employee_id & branch_id for history ,check database
employee_id = 0
branch_id = 0

# Default Image for Book
default_book_image = '/home/izy/Desktop/Library System/wBook.png'
use_book = 1


class Main(QMainWindow , MainUI):

    # The Constractor.
    def __init__(self, parent=None):
        super(Main , self).__init__(parent)

        QMainWindow.__init__(self)
        
        self.setupUi(self)
        self.Db_Connect()
        self.UI_Changes()
        self.Handle_Buttons()

        
        # Set Visibale Tabs
        self.tabWidget_2.setTabVisible(1,0)
        self.tabWidget_2.setTabVisible(2,0)

        self.tabWidget_3.setTabVisible(1,0)
        self.tabWidget_3.setTabVisible(2,0)

        self.tabWidget_4.setTabVisible(2,0)
        self.tabWidget_4.setTabVisible(3,0)
        self.tabWidget_4.setTabVisible(1,0)

        # Load Data To ComboBoxies
        self.Show_All_Categories()
        self.Show_All_Publishers()
        self.Show_All_Authors()
        self.Show_Employee()
        

        # Login
        self.Handle_Login()

        # Retrieve Daily movments
        # self.Retrieve()


    # Handling GUI changes.
    def UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)
        


    def Db_Connect(self):
        # Connect Between Database and Programe.
        self.db = sqlite3.connect("Library_Database.db")
        self.cur = self.db.cursor()
        print("Connected!")


    # Call the Buutons in one Group to Load them in system
    def Handle_Buttons(self):

        

        # Open Taps Buttons
        self.pushButton.clicked.connect(self.Open_Daily_Movment_Tap)
        self.pushButton_2.clicked.connect(self.Open_Books_Tap)
        self.pushButton_6.clicked.connect(self.Open_Clients_Tap)
        self.pushButton_5.clicked.connect(self.Open_Dashboard_Tap)
        self.pushButton_4.clicked.connect(self.Open_History_Tap)
        self.pushButton_3.clicked.connect(self.Open_Reports_Tap)
        self.pushButton_7.clicked.connect(self.Open_Settings_Tap)

        #### Daily Movemnet Buttons
        self.pushButton_23.clicked.connect(self.getDilyTabSearch)
        self.pushButton_37.clicked.connect(self.getOrder)
        self.pushButton_22.clicked.connect(self.openCommitOrder)
        self.pushButton_8.clicked.connect(self.commitBookOrder)

        #### Books Tap's Buttons
        self.pushButton_13.clicked.connect(self.Add_New_Book)
        self.pushButton_14.clicked.connect(self.Edit_Book_Search)
        self.pushButton_15.clicked.connect(self.Save_Edit_Book)
        self.pushButton_16.clicked.connect(self.Delete_Book)
        self.pushButton_10.clicked.connect(self.Book_filter_Search)
        self.pushButton_11.clicked.connect(self.Book_Export_Report)
        
        



        #### Clients Tap's Buttons
        self.pushButton_27.clicked.connect(self.Add_New_Client)
        self.pushButton_28.clicked.connect(self.Edit_Client_Search)
        self.pushButton_29.clicked.connect(self.Save_Edit_Client)
        self.pushButton_30.clicked.connect(self.Delete_Client)




        #### Settings Buttons
        # Setting [All Data] Buttons
        self.pushButton_24.clicked.connect(self.Add_Branch)
        self.pushButton_25.clicked.connect(self.Add_Publisher)
        self.pushButton_31.clicked.connect(self.Add_Author)
        self.pushButton_32.clicked.connect(self.Add_Category)
        # Employeies tap's buttons
        self.pushButton_38.clicked.connect(self.Add_Employee)
        self.pushButton_36.clicked.connect(self.Check_Employee_toEdit)
        self.pushButton_56.clicked.connect(self.Save_Edit_Employee) 
        self.pushButton_40.clicked.connect(self.Add_Employee_Permissions) 
        self.pushButton_39.clicked.connect(self.Check_empployee_Permissions)


        #### Reports Buttons 
        self.pushButton_49.clicked.connect(self.All_Books_Reports) # Export tab book
        self.pushButton_50.clicked.connect(self.All_Clients_Reports)
        self.pushButton_51.clicked.connect(self.All_Employeies_Reports)

        # Open Image
        self.pushButton_17.clicked.connect(self.getImage)
           

    # Enabel ALL the permissions in the system.
    def adminPermissions(self):
        # Side Buttons
        self.pushButton_2.setEnabled(1)
        self.pushButton_6.setEnabled(1)
        self.pushButton_5.setEnabled(1)
        self.pushButton_4.setEnabled(1)
        self.pushButton_3.setEnabled(1)
        self.pushButton_7.setEnabled(1)

        # Book's tap buttons
        self.tabWidget_2.setTabVisible(1,1) # Add new book
        self.tabWidget_2.setTabVisible(2,1) # edit or delete book
        self.pushButton_11.setEnabled(1)
        self.pushButton_12.setEnabled(1)
        # self.pushButton_14.setEnabled(1)
        self.pushButton_15.setEnabled(1)
        self.pushButton_16.setEnabled(1)

        # Client's tap buttons
        self.tabWidget_3.setTabVisible(1,1) # Add new client
        self.tabWidget_3.setTabVisible(2,1) # edit or delete client
        # self.pushButton_26.setEnabled(1)
        self.pushButton_44.setEnabled(1)
        self.pushButton_45.setEnabled(1)
        self.pushButton_27.setEnabled(1)
        # self.pushButton_28.setEnabled(1)
        self.pushButton_29.setEnabled(1)
        self.pushButton_30.setEnabled(1)

        # Settings's tap buttons
        self.tabWidget_4.setTabVisible(1,1) # Add new or edit employee
        self.tabWidget_4.setTabVisible(2,1) # permissions
        self.tabWidget_4.setTabVisible(3,1) # reports
        self.pushButton_25.setEnabled(1)
        self.pushButton_24.setEnabled(1)
        self.pushButton_31.setEnabled(1)
        self.pushButton_32.setEnabled(1)
        self.pushButton_36.setEnabled(1)
        self.pushButton_41.setEnabled(1)
        self.pushButton_38.setEnabled(1)

    # Get employee permissions from database, and return it.
    def getEmployeePermissions(self):
        # Get permissions from database
        employeePermissions = database.getOne("select * from employee_permission where name = '{}'".format(username))

        thePermissions = {
            'name':employeePermissions[1], 
            'add_book':employeePermissions[2], 'edit_book':employeePermissions[3], 'delete_book':employeePermissions[4], 'export_book':employeePermissions[5], 'import_book':employeePermissions[6],
            'add_client':employeePermissions[7], 'edit_client':employeePermissions[8], 'delete_client':employeePermissions[9], 'export_client':employeePermissions[10], 'import_client':employeePermissions[11],
            'book_tap':employeePermissions[12], 'cient_tap':employeePermissions[13], 'dashbuord_tap':employeePermissions[14], 'history_tap':employeePermissions[15], 'reports_tap':employeePermissions[16], 'setting_tap':employeePermissions[17],
            'add_branch':employeePermissions[18], 'add_publiher':employeePermissions[19], 'add_author':employeePermissions[20], 'add_cateogry':employeePermissions[21],
            'add_employee':employeePermissions[22], 'edit_employee':employeePermissions[23], 'admin':employeePermissions[24]
        }

        return thePermissions


    # Handle loginning and work with login_fram data and GUI.
    def Handle_Login(self):
        
        # Get Login_frame data Form database
        loginUiData = database.getOne("select username, password, its_me, error from login where id = {}".format(login_frame.userLoginID))
        
        # Get data from fields
        loginUiUsername = 0; loginUipassword = 1; loginUiIts_me=2; loginUiError=3;
        
        username  = loginUiData[loginUiUsername]
        password  = loginUiData[loginUipassword]
        
        loginAsAdmin = loginUiData[loginUiIts_me]
        loginAsUser= loginUiData[loginUiError]



        

        # Loginning as Admin.
        if username=='admin' and password=='000':
            print("Logining... --> username is Admin")

        else: # Loginning as an Employee
            # Check username and password data in database.
            employeeLoginData = database.getAll("select name, password, Branch from employee where name = '{}' and Password = '{}'".format(username, password))
            empty = 0

            if len( employeeLoginData ) != empty:
                
                # Get employee_id & branch
                global employee_id, branch_id

                employee_id = employeeLoginData[0][1]
                branch_id = employeeLoginData[0][2]

            
                # Get permissions from database
                employeePermissions = self.getEmployeePermissions()

                print("Loginnig... --> username is {}".format(username))


            else:
                print("=========== WRONG!! ============= \npassword or username is incorrect.")


        # Enable Permissions Acces
        if loginAsAdmin == True: # just my own user UwU
            print("Welcome Admin... \nWait to set the permissions.")
            
            # Admin -> All permissions
            self.adminPermissions()            

            # Open Today tap
            self.Open_Daily_Movment_Tap()

        elif loginAsUser == True: # --> Login as employee

            print("Welcome {} ... \nwait to set the permissions.".format(username))

            if employeePermissions['admin']==True: # Admin -> All permissions
                self.adminPermissions()

            # Book tap permissions
            if employeePermissions['add_book']==True: 
                self.pushButton_2.setEnabled(1)

                if employeePermissions['export_book'] == True:# Check Export  
                    self.pushButton_11.setEnabled(1)
                if employeePermissions['import_book'] == True: # Check Import
                    self.pushButton_12.setEnabled(1)


                if employeePermissions['add_book'] == True:# Check Add Book
                    self.tabWidget_2.setTabVisible(1,1)
                
                if employeePermissions['edit_book'] == True :# Check Edit Book
                    self.tabWidget_2.setTabVisible(2,1)
                    self.pushButton_15.setEnabled(1)
                    
                    if employeePermissions['delete_book'] == True : # Check delete book
                        self.pushButton_16.setEnabled(1)

            # Client tap permissions
            if employeePermissions['client_book'] == True : 
                self.pushButton_6.setEnabled(1)

                if employeePermissions['export_client'] == True :# Check Export  
                    self.pushButton_45.setEnabled(1)
                if employeePermissions['import_client'] == True : # Check Import
                    self.pushButton_44.setEnabled(1)


                if employeePermissions['add_client'] == True :# Check Add Client
                    self.tabWidget_3.setTabVisible(1,1)
                
                if employeePermissions['edit_client'] == True :# Check Edit Client
                    self.tabWidget_3.setTabVisible(2,1)
                    self.pushButton_29.setEnabled(1)
                    
                    if employeePermissions['delete_client'] == True : # Check delete Client
                        self.pushButton_30.setEnabled(1)
                        
            # Dashbourd tab permissions
            if employeePermissions['dashbuord_tap'] == True :
                self.pushButton_5.setEnabled(1)
            
            # History tab permissions
            if employeePermissions['hitory_tap'] == True :
                self.pushButton_4.setEnabled(1)

            # Reports tab permissions
            if employeePermissions['reports_tap'] == True :
                self.pushButton_3.setEnabled(1)

            # Settings tab permissions
            if employeePermissions['setting_tap'] == True :
                self.pushButton_7.setEnabled(1)

                if employeePermissions['add_employee'] == True : # Add employee
                    self.tabWidget_4.setTabVisible(1,1)
                
                if employeePermissions['edit_employee'] == True : # Edit Employee
                    self.pushButton_36.setEnabled(1)
                    self.pushButton_41.setEnabled(1)

                if employeePermissions['add_branch'] == True : # Add branch
                    self.pushButton_24.setEnabled(1)
                
                if employeePermissions['add_publisher'] == True : # Add publisher
                    self.pushButton_25.setEnabled(1)
                
                if employeePermissions['add_author'] == True : # Add author
                    self.pushButton_31.setEnabled(1)
                
                if employeePermissions['add_category'] == True : # Add category
                    self.pushButton_32.setEnabled(1)

            # Add this Aciotn in History
            history_id = database.generateID("select * from history")
            dateFromSystem = datetime.now().strftime('%d-%m-%Y %H:%M')
            
            database.insertManyData("insert into history values(?,?,?,?,?,?)",[
                (history_id, employee_id, 'Loing', dateFromSystem, branch_id, username)
            ])
            
            
            # Open Today tap
            self.Open_Daily_Movment_Tap()

        

    def Handle_Reset_Password(self):
        pass

    """==================================================================================
    ========================= Today tab's functions =================================="""
    
    """Dailymovments tab"""
    # Search
    # Workable
    def getDilyTabSearch(self): # Work with DB --> daily_movments table.
        
        # VARIABLES
        searchText = self.lineEdit_59.text()
        table = self.tableWidget_2

        # DATA
        thisData = {'search text':searchText, 'table':table}
        
        
        # CHECK
        if len(searchText) != empty:
            
            # PROSSES
            hpTool.getDailyBooksSearch(thisData)

        # OUTPUT

    """Order a Book, tab"""
    def getOrder(self):

        searchText = self.lineEdit_60
        table = self.tableWidget_4

        thisData = {'search text':searchText, 'table':table}
        hpTool.getOrderTabSearch(thisData)


    """Commit order tab"""
    def openCommitOrder(self): # --> Tool to do in UI.
        """Opent the tab and load book title field."""
        # OPEN 
        self.TaodayWidget.setCurrentIndex(2)
        
        # GET
        orderABook = self.lineEdit_60.text()

        # SET
        self.lineEdit_4.setText(orderABook)    

    # Workable
    def commitBookOrder(self): # Wrok with GUI --> Commit Order Tab.

        # GET DATA
        bookTitle = self.lineEdit_4.text()
        clientID = self.lineEdit_7.text()
        orderType = self.comboBox.currentText()

        label = self.label_21

        # SORD DATA
        thisData = {'employee id':employee_id, 'branch id':branch_id,
        'book title':bookTitle, 'client id':clientID, 
        'order type':orderType, 'label':label}

        # CHECK
        thisFields = {'book title':bookTitle, 'client id':clientID}
        checkResult = Tools.checkFields(thisFields)
        
        if checkResult != empty:

            hpTool.getOrderDetails(thisData)

            

        # REFRASH
        tableName = self.tableWidget_2
        hpTool.showDailyBooks({'table':tableName})


    """===========================================================================
    ======================== Book tab's functions ============================="""

    # Book tap filter to search in database
    def Book_filter_Search(self):

        # VARIABLES
        searchText = self.lineEdit_5.text()
        table = self.tableWidget_3
        thisData = {'search text':searchText, 'table':table, 'branch id':branch_id}

        # RUN
        helpTool.BookTab().searchAboutBook(thisData)
    

    # Show the Books in The Table.
    def Show_All_Books(self):

        # VARIABLES
        thisData = {'branch id':branch_id, 'table':self.tableWidget_3}     

        # RUN
        helpTool.BookTab().getAllBooks(thisData)


    # Open a Dialog Window and Get Pecture for Books or a Profile
    def getImage(self):
        global use_book , img_name
        # Default image
        # default_image = '/home/izy/Desktop/Library System/wBook.png'
        # self.pixmap = QPixmap(default_image)

        # Open Dialog and Get Picture
        img_name = QFileDialog.getOpenFileName(self, "Get the Image", "/home/izy/Desktop/Library System", "All Files (*);;PNG Files (*.png)")

        # Open The Image this run
        self.pixmap = QPixmap(img_name[0])

        # Add Image to Label
        self.label_19.setPixmap(self.pixmap)

        # Change use_book variable statue
        use_book = 0


    # Add New Book to Database
    def Add_New_Book(self):
         
        # Get Data from GUI [Fields]
        bookTitle = self.lineEdit_6.text(); bookPrice = self.lineEdit_11.text()
        bookCode = self.lineEdit_47.text(); bookPart = self.lineEdit_50.text()
        
        bookBarcode = self.lineEdit_49.text(); bookDescription = self.textEdit.toPlainText()
        bookCategory = self.comboBox_4.currentText(); bookPublisher = self.comboBox_8.currentText()
        
        bookAuthor = self.comboBox_6.currentText(); bookStatus = self.comboBox_7.currentText()
        bookQuantity = self.lineEdit_54.text()

        # Get the Image
        if use_book==1 : # User didnt add a picture

            # Get image path
            bookImage = default_book_image

        else : # User Add a picture

            # Get image path
            bookImage = img_name[0]
        

        # Sort data
        thisData = {
            'title':bookTitle, 'description':bookDescription, 'author':bookAuthor,
            'category':bookCategory, 'publisher':bookPublisher, 'part':bookPart,
            'price':bookPrice, 'code':bookCode, 'barcode':bookBarcode,
            'status':bookStatus, 'quantity':bookQuantity, 'image':bookImage,
            'branch id':branch_id, 'employee id':employee_id
        }

        # RUN
        helpTool.BookTab().submitNewBook(thisData)


        # REFRESH
        self.Show_All_Books()

        # Clear Fields
        self.lineEdit_6.clear()
        self.lineEdit_11.clear()
        self.lineEdit_47.clear()
        self.lineEdit_50.clear()
        self.lineEdit_49.clear()        
        self.textEdit.clear()
        self.lineEdit_54.clear()


    # Edit a Book and svae changes in database
    def Edit_Book_Search(self):
        
        
        # Sort data.
        bookTitle = self.lineEdit_9.text()

        thisData = {'branch id':branch_id, 'book search':self.lineEdit_8, 'book title':self.lineEdit_9,
        'book description':self.textEdit_3, 'book category':self.comboBox_5,
        'book price':self.lineEdit_48, "book code":self.lineEdit_12,
        "book publisher":self.comboBox_13, "book author":self.comboBox_10,
        "book part":self.lineEdit_51, "book quantity":self.lineEdit_55, 'book status':self.comboBox_12,
        'book image':self.label_20, 'pixmap':self.pixmap}
            
        # RUN
        helpTool.BookTab().submitEditBook(thisData)


    # Save Changes from Edit Book in database
    def Save_Edit_Book(self):
        
        TabWidget.BookTab().submitChange()
        # Notification
        self.statusBar().showMessage("Edited !!") # Notification

    # Delete a Book and Save th Changes in Database
    def Delete_Book(self):
        
        code = self.lineEdit_8.text() # Get a code to search via 

        # Get book name
        self.cur.execute("selcet name from books where code = {}".format(code))        
        book_title = self.cur.fetchone()[0]
        # Delete from database
        self.cur.execute("delete from books where code = {}".format(code))        

        # Add this Actions in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Delete Book", date, branch_id, book_title
        )])

        # Save data in database
        self.db.commit()

        # Clear fields
        book_title = self.lineEdit_9.clear()
        book_description = self.textEdit_3.clear()
        book_price = self.lineEdit_48.clear()
        book_code = self.lineEdit_12.clear()
        book_part_order = self.lineEdit_51.clear()

        book_category = self.comboBox_5.setCurrentIndex(0)
        book_publisher = self.comboBox_13.setCurrentIndex(0)
        book_author = self.comboBox_10.setCurrentIndex(0)
        book_status = self.comboBox_12.setCurrentIndex(0)


        # Notification
        # print("Deleted !!") 
        self.statusBar().showMessage("Deleted !!") # Notification

        # Refreash Data
        self.Show_All_Books()



    #################################################
    #### Clients
    # Show data in client table
    def Show_All_Clients(self):
        
        # Get Data from Database.
        self.cur.execute("select name, mail, phone, national_id, date   from clients")
        data = self.cur.fetchall()

        # Insert data into table
        for row , form in enumerate(data):
            # Insert new Row
            row_position = self.tableWidget_5.rowCount()
            if row_position <= row:
                self.tableWidget_5.insertRow(row_position)

            for col, item in enumerate(form):
                self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)) )
                col+=1 # to new column

            

        # Notification
        print("Show All Clients Done")

    # Add New Client & Save changes in database.
    def Add_New_Client(self):
        
        # Get Data from Fields
        client_name = self.lineEdit_13.text()
        client_mail = self.lineEdit_14.text()
        client_phone = self.lineEdit_16.text()
        client_national_id = self.lineEdit_18.text()

        self.cur.execute("select * from clients")
        id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')

        # Check is There another id same and fix it
        self.cur.execute("select * from clients where id = '{}'".format(id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            id+=1



        # Load Data to Database
        data = [
            (id, client_name, client_mail, client_phone, date, client_national_id)
        ]
        self.cur.executemany("insert into clients values(?,?,?,?,?,?)",data)        

        # Add this Actions in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        # date = datetime.now()


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Add Client", date, branch_id, client_name
        )])

        # Save data in database
        self.db.commit()


        # Clear Fields
        client_name = self.lineEdit_13.clear()
        client_mail = self.lineEdit_14.clear()
        client_phone = self.lineEdit_16.clear()
        client_national_id = self.lineEdit_18.clear()


        # Notification
        print("Client "+str(client_name)+" Added!")
        self.Show_All_Clients()


        


    def Edit_Client_Search(self):
        
        # Get Client data to search via
        client_data = str(self.lineEdit_21.text()) # Here Data text what i will search via.

        # Check is there last search !!
        if ( len(self.lineEdit_17.text()) > 0 ) : # is not empty  --> Here i take client name feild to check
            
            # Clear Feilds
            self.lineEdit_17.clear() # name
            self.lineEdit_15.clear() # mail
            self.lineEdit_20.clear() # phone
            self.lineEdit_19.clear() # nationa ID

        
        # Get filter search
        filter = self.comboBox_37.currentIndex()
        filter_name = ""

        if filter == 0:
            filter_name = "name"

        elif filter == 1:
            filter_name = "mail"
            
        elif filter == 2:
            filter_name = "phone"

        else:
            filter_name = "national_id"


        # Check if client data dield is empty
        if len(client_data) <= 0:
            print("Please Enter Client Data to Search !!") # Notification

        else : # is not Empty

            # Search in database using filter code
            sql = "select * from clients where {0} = '{1}'" 
            sql = sql.format(filter_name, client_data)
            self.cur.execute(sql)

            data_lenghth = len( self.cur.fetchall() ) # how many data here

            if data_lenghth == 0 : # is it not in database
                self.statusBar().showMessage("There is no Client with this {} data !".format(client_data)) # Notification

            else : # if Founded
                
                sql = "select * from clients where {0} = '{1}'" 
                sql = sql.format(filter_name, client_data)
                
                
                self.cur.execute(sql)
                data = self.cur.fetchone()                 

                # Load data to fields
                client_name = self.lineEdit_17.setText(data[1])
                client_mail = self.lineEdit_15.setText(data[2])
                client_phone = self.lineEdit_20.setText(data[3])
                client_national_id = self.lineEdit_19.setText(str(data[5]))

                # Notification
                print("Search Done !!")



    def Save_Edit_Client(self):
        # Get Data from Fields
        client_name = self.lineEdit_17.text()
        client_mail = self.lineEdit_15.text()
        client_phone = self.lineEdit_20.text()
        client_national_id = self.lineEdit_19.text()


        


        # Get client id from database
        client_data = str(self.lineEdit_21.text()) # Here Data text what i will search via.

        # Get filter search
        filter = self.comboBox_37.currentIndex()
        filter_name = ""

        if filter == 0:
            filter_name = "name"

        elif filter == 1:
            filter_name = "mail"
            
        elif filter == 2:
            filter_name = "phone"

        else:
            filter_name = "national_id"

        self.cur.execute("select * from clients where {0} = '{1}'".format(filter_name, client_data))
        id  = self.cur.fetchone()[0]

        print(id)

        # Update to database
        sqle = """update clients 
                set name = '{0}',
                mail = '{1}',
                phone = '{2}',
                national_id = {3}
                where id = {4}"""
        sqle = sqle.format(
            client_name, client_mail, client_phone, client_national_id,
            id
            )
        
        self.cur.execute(sqle)


        # Add this Actions in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Edit Client", date, branch_id, client_name
        )])

        # Save data in database
        self.db.commit()


        # Notifications
        message = "The Cleint {} was updated !".format(client_name)
        print(message)
        self.statusBar().showMessage(message)



    def Delete_Client(self):
        

        # Get client id from database
        client_data = str(self.lineEdit_21.text()) # Here Data text what i will search via.
        name = self.lineEdit_17.text()

        # Get filter search
        filter = self.comboBox_37.currentIndex()
        filter_name = ""

        if filter == 0:
            filter_name = "name"

        elif filter == 1:
            filter_name = "mail"
            
        elif filter == 2:
            filter_name = "phone"

        else:
            filter_name = "national_id"

        self.cur.execute("select * from clients where {0} = '{1}'".format(filter_name, client_data))
        id  = self.cur.fetchone()[0]


        print(id)

        # Now Delete it
        self.cur.execute("delete from clients where id = '{}'".format(id))

        


        # Add this Actions in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        client_name = self.lineEdit_17.text()

        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Delete Client", date, branch_id, client_name
        )])

        # Save data in database
        self.db.commit()

        # Now Clear Feilds
        client_name = self.lineEdit_17.clear()
        client_mail = self.lineEdit_15.clear()
        client_phone = self.lineEdit_20.clear()
        client_national_id = self.lineEdit_19.clear()

        client_data = self.lineEdit_21.clear()


        # Now Show a Notifications
        message = "The Cleint {} was deleted !".format(name)
        print(message)
        self.statusBar().showMessage(message)



    ###############################################################
    #### Hitory
    # Shoe the data from table history in database to history tap in gui
    def Show_Hitory(self):
        # Get data from database
        self.cur.execute("select employee, actions, branch_id, date from history")
        data = self.cur.fetchall()

        # Insert data into table
        for row , form in enumerate(data):
            # Insert new Row
            row_position = self.tableWidget_6.rowCount()
            if row_position <= row:
                self.tableWidget_6.insertRow(row_position)

            for col, item in enumerate(form):
                self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)) )
                col+=1 # to new column

        print("Show_Hitory Done!")



    ###############################################################
    #### Books Reports
    
    def Show_All_Book_Reports(self):
        #### Get date from fields
        # Get Qdatetime[dt] atribute from this code --> self.dateTimeEdit.dateTime()
        from_date = str( self.dateTimeEdit.textFromDateTime( self.dateTimeEdit.dateTime() ) ).replace("/","-")
        to_date = str( self.dateTimeEdit_2.textFromDateTime( self.dateTimeEdit_2.dateTime() ) ).replace("/","-")
        
        print("from_date "+ from_date)
        print("to_date "+ to_date)

        # Get data from table books in database 
        self.cur.execute("select code, title, category_id, author_id from books")
        data = self.cur.fetchall()
        print(data)

        # Get Books names from data
        books = []
        for book in data:
            books.append(book[1])

        print("bboks:"+str(books))

        
        # Get Branchies
        branchies = []
        for book in books:
            rent = book+" Rent"
            retrieve = book+" Retrieve"

            # Get branchies from database
            self.cur.execute("select branch_id from history where extra = '{}' or extra = '{}'".format(rent, retrieve))
            branchies_db = self.cur.fetchall()

            # Generata branchies & Quantity
            for branch in branchies_db:
                if branch[0] not in branchies:
                    branchies.append( (branch[0]) )
                

        # Generata table fields
        row_position = len(books) #*len(branchies)
        row_count = self.tableWidget_7.rowCount()
        if row_count==0:
            for i in range(row_position):
                self.tableWidget_7.insertRow(i)


        in_row = 0; temp=0
        for row , form in enumerate(data):
            book_title=""
            print("bran : "+str(branchies[row]))

            # Calculate
            # Rent
            self.cur.execute("select id from history where extra = '{}' and branch_id = {}".format(books[row]+" Rent", branchies[row]))
            rent_sum = len( self.cur.fetchall() )
            # Retrieve
            self.cur.execute("select id from history where extra = '{}' and branch_id = {}".format(books[row]+" Retrieve", branchies[row]))
            retrieve_sum = len( self.cur.fetchall() )
            
            

            # Insert new Row
            for col, item in enumerate(form):
                if col == 1:
                    self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(str( data[row][col] )) )
                # Get real data name for category and author
                elif col == 2:
                    self.cur.execute("select category_name from category where id = '{}'".format(data[row][2]))
                    self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(str(self.cur.fetchone()[0])) )
                
                elif col == 3:
                    self.cur.execute("select name from author where id = '{}'".format(data[row][3]))
                    self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(str(self.cur.fetchone()[0])) )


                else:
                    self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(item) )
                    
                    # Get Quantity
                    book_title = data[row][1]
                    print("boook="+book_title)
                    self.cur.execute("select quantity from books where title = '{}' and Branch = '{}'".format(
                        book_title, branchies[row]))
                    # Quantity
                    quantity = self.cur.fetchone()[0]
                    print("quantity:"+str(quantity))
                    quantity = (quantity-rent_sum)+retrieve_sum
                    self.tableWidget_7.setItem(row+in_row, 5, QTableWidgetItem(str(quantity)) )

                    self.tableWidget_7.setItem(row+in_row, 4, QTableWidgetItem(str(branchies[row])) )


                col+=1 # to new column
        # for i in branchies:
            
            
            
            
        #     # Insert data into table
        #     for row , form in enumerate(data):
        #         book_title=""
        #         print("bran : "+str(i))

        #         # Calculate
        #         # Rent
        #         self.cur.execute("select id from history where extra = '{}' and branch_id = {}".format(books[row]+" Rent", i))
        #         rent_sum = len( self.cur.fetchall() )
        #         # Retrieve
        #         self.cur.execute("select id from history where extra = '{}' and branch_id = {}".format(books[row]+" Retrieve", i))
        #         retrieve_sum = len( self.cur.fetchall() )
                
                

        #         # Insert new Row
        #         for col, item in enumerate(form):
        #             if col == 1:
        #                 self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(str( data[row][col] )) )
        #             # Get real data name for category and author
        #             elif col == 2:
        #                 self.cur.execute("select category_name from category where id = '{}'".format(data[row][2]))
        #                 self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(str(self.cur.fetchone()[0])) )
                    
        #             elif col == 3:
        #                 self.cur.execute("select name from author where id = '{}'".format(data[row][3]))
        #                 self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(str(self.cur.fetchone()[0])) )


        #             else:
        #                 self.tableWidget_7.setItem(row+in_row, col, QTableWidgetItem(item) )
                        
        #                 # Get Quantity
        #                 book_title = data[row][1]
        #                 print("boook="+book_title)
        #                 self.cur.execute("select quantity from books where title = '{}' and Branch = '{}'".format(
        #                     book_title, i))
        #                 # Quantity
        #                 quantity = self.cur.fetchone()[0]
        #                 print("quantity:"+str(quantity))
        #                 quantity = (quantity-rent_sum)+retrieve_sum
        #                 self.tableWidget_7.setItem(row+in_row, 5, QTableWidgetItem(str(quantity)) )

        #                 self.tableWidget_7.setItem(row+in_row, 4, QTableWidgetItem(str(i)) )


        #             col+=1 # to new column
        #         # Row
        #         temp=row

        #     # Zehahahah
        #     in_row+=temp+1





    def All_Books_Reports(self):
        

        # Load data into excel file
        file_date = datetime.now().strftime('%d of %m')

        excel_file = Workbook('All Book Export Report ('+str( file_date )+' ).xlsx')
        sheet1 = excel_file.add_worksheet()

        # Add Formats
        bold = excel_file.add_format({'bold':1})
        
        # Format Columns
        sheet1.set_column(1,3,18)

        # Set Headers
        sheet1.write('A1','Book Code', bold)
        sheet1.write('B1','Book Title', bold)
        sheet1.write('C1','Category', bold)
        sheet1.write('D1','Author', bold)
        sheet1.write('E1','Branch', bold)
        sheet1.write('F1','Quantity', bold)

        # Insert data from database to excel file
        # Get row, column counts
        rowCount = self.tableWidget_7.rowCount()
        columnCount = self.tableWidget_7.columnCount()

        # Loop through that numbers
        sheetRow=0
        for row in range(rowCount):
            sheetRow+=1
            for col in range(columnCount):
                data = self.tableWidget_7.item(row, col).text()
                sheet1.write(sheetRow, col, data)

        # Close Excel file to save
        excel_file.close()




    # This for book tab
    def Book_Export_Report(self):
        """Export book's list to an Excel file."""

        # RUN
        ExcelFiles.BookReports().exportBookReport({'employee id':employee_id, 'branch id':branch_id})

        # NOTIFICATIONS
        print("Exported!")



    ###############################################################
    #### Clients Reports
    
    def Show_All_Client_Reports(self):
        # Get data
        self.cur.execute("select name, mail, phone, national_id from clients")
        data = self.cur.fetchall()

        # get client's book
        books = []
        for client in data:
            
            self.cur.execute("select book_id from daily_movments where client_id = {}".format(client[3]))
            books.append( len(self.cur.fetchall()) )
        print(books)
        
        # Insert data into table
        for row , form in enumerate(data):
            # Insert new Row
            row_position = self.tableWidget_8.rowCount()
            if row_position <= row:
                self.tableWidget_8.insertRow(row_position)

            for col, item in enumerate(form):
                if col==3:
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(books[row])) )
                else:    
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(item)) )
                col+=1 # to new column        

    def All_Clients_Reports(self):

        # Load data into excel file
        file_date = datetime.now().strftime('%d of %m')

        excel_file = Workbook('All Client Export Report ('+str( file_date )+' ).xlsx')
        sheet1 = excel_file.add_worksheet()

        # Add Formats
        bold = excel_file.add_format({'bold':1})
        
        # Format Columns
        sheet1.set_column(0,2,18)

        # Set Headers
        sheet1.write('A1','Name', bold)
        sheet1.write('B1','Mail', bold)
        sheet1.write('C1','Phone', bold)
        sheet1.write('D1','Book', bold)
        

        # Insert data from database to excel file
        # Get row, column counts
        rowCount = self.tableWidget_8.rowCount()
        columnCount = self.tableWidget_8.columnCount()

        # Loop through that numbers
        sheetRow=0
        for row in range(rowCount):
            sheetRow+=1
            for col in range(columnCount):
                data = self.tableWidget_8.item(row, col).text()
                sheet1.write(sheetRow, col, data)

        # Close Excel file to save
        excel_file.close()


    def Clinets_Filter_Report(self):
        pass

    def Client_Export_Report(self):
        pass



    ###############################################################
    #### Employee Reports

    def Show_Employee_Report(self):
        # Get data from database
        self.cur.execute("select employee, id, actions, date, branch_id from history")
        data = self.cur.fetchall()
        print("Employee_Report")
      

        # Get data 
        national_id = 0
        new_data = []
        rent=0; Retrieve=0; 
        add_book=0; edit_book =0;delete_book=0;
        add_client=0; edit_client=0; delete_client=0;


        
        # Get Employee name
        employeies = []
        for item in data:

            if item[0] not in employeies and item[0]!='0':
                employeies.append( (item[0]) )

        print("employeies ",end=" ")
        print(employeies)

        # Get employee's actions
        actions = {}
        row = 0

        for i in employeies:
            # Clear last data
            temp=row
            rent=0; retrieve=0; 
            add_book=0; edit_book =0;delete_book=0;
            add_client=0; edit_client=0; delete_client=0;

            # Get actions
            self.cur.execute("select actions from history where employee like '{}'".format(i))
            actions_db = self.cur.fetchall()
            
            # generate data
            for act in actions_db:
                
                if act[0]=='Rent':
                    rent = actions_db.count(act)
                
                elif act[0]=='Retrieve':
                    retrieve = actions_db.count(act)

                elif act[0]=='Add Book':
                    add_book = actions_db.count(act)

                elif act[0]=='Edit Book':
                    edit_book = actions_db.count(act)

                elif act[0]=='Delete Book':
                    delete_book = actions_db.count(act)

                elif act[0]=='Add Client':
                    add_client = actions_db.count(act)

                elif act[0]=='Edit Client':
                    edit_client = actions_db.count(act)

                elif act[0]=='Delete Client':
                    delete_client = actions_db.count(act)

            # insert data in dic
            actions = {
                'name':i,
                'Rent':rent, 'Retrieve':retrieve,
                'Add Book':add_book, 'Edit Book':edit_book, 'Delete Book':delete_book,
                'Add Client':add_client, 'Edit Client':edit_client, 'Delete Client':delete_client
            }

            print(actions)
            
            # Simple algorithm to get row count
            count=0 #counter
            for act in actions.values():
                
                if act!= actions['name'] :
                    if act>0:
                        count+=1
            print("count:"+str(count))

            # Get national id
            self.cur.execute("select national_id from employee where name like '%{}%'".format(i))
            national_id = self.cur.fetchone()[0]

            print("id:"+str(national_id))



            # Generata table fields
            row_count = self.tableWidget_10.rowCount()
            if row_count==temp:
                for rw in range(count):
                    rw+=temp
                    self.tableWidget_10.insertRow(temp)



            # Insert data into table
            here=1
            for act in actions.values():
                print("act="+str(act))
                print("here="+str(here))
                if act==actions['name']:
                    continue
                elif act==0:
                    here+=1

                
                if act==actions['Rent'] and act!=0 and here==1:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Rent : '+str(act)) )
                    
                    
                    self.cur.execute("select date ,branch_id from history where employee like '%{}%' and actions like '%{}%'".format(i, 'Rent'))
                    other = self.cur.fetchone()

                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )
                    
                    row+=1
                    here+=1
                
                
                elif act==actions['Retrieve'] and act!=0 and here==2:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Retrieve : '+str(act)) )
                    
                    self.cur.execute("select date ,branch_id from history where employee = '{}' and actions = '{}'".format(i, 'Retrieve'))
                    other = self.cur.fetchone()
                    
                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )
            
                    row+=1
                    here+=1

                elif act==actions['Add Book'] and act!=0 and here==3:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Add Book : '+str(act)) )
                    
                    self.cur.execute("select date ,branch_id from history where employee = '{}' and actions = '{}'".format(i, 'Add Book'))
                    other = self.cur.fetchone()
                    
                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )

                    row+=1
                    here+=1

                elif act==actions['Delete Book'] and act!=0 and here==5:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Delete Book : '+str(act)) )
                    
                    self.cur.execute("select date ,branch_id from history where employee = '{}' and actions = '{}'".format(i, 'Delete Book'))
                    other = self.cur.fetchone()
                    
                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )

                elif act==actions['Edit Book'] and act!=0 and here==4:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Edit Book : '+str(act)) )
                    
                    self.cur.execute("select date ,branch_id from history where employee = '{}' and actions = '{}'".format(i, 'Edit Book'))
                    other = self.cur.fetchone()
                    
                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )

                    row+=1
                    here+=1

                elif act==actions['Add Client'] and act!=0 and here==6:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Add Client : '+str(act)) )
                    
                    self.cur.execute("select date ,branch_id from history where employee = '{}' and actions = '{}'".format(i, 'Add Client'))
                    other = self.cur.fetchone()
                    
                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )
                    
                    row+=1
                    # here+=1

                elif act==actions['Delete Client'] and act!=0 and here==8:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Delete Client : '+str(act)) )
                    
                    self.cur.execute("select date ,branch_id from history where employee = '{}' Delete actions = '{}'".format(i, 'Add Client'))
                    other = self.cur.fetchone()
                    
                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )

                    row+=1

                elif act==actions['Edit Client'] and act!=0 and here==7:
                    self.tableWidget_10.setItem(row, 0, QTableWidgetItem(str(i)) )
                    self.tableWidget_10.setItem(row, 1, QTableWidgetItem(str(national_id)) )
                    self.tableWidget_10.setItem(row, 2, QTableWidgetItem('Edit Client : '+str(act)) )
                    
                    self.cur.execute("select date ,branch_id from history where employee = '{}' and actions = '{}'".format(i, 'Edit Client'))
                    other = self.cur.fetchone()
                    
                    self.tableWidget_10.setItem(row, 3, QTableWidgetItem(str( other[0] )) )
                    self.tableWidget_10.setItem(row, 4, QTableWidgetItem(str( other[1] )) )

                    row+=1
                    

            print("row:"+str(row))



    def All_Employeies_Reports(self):
        # Load data into excel file
        file_date = datetime.now().strftime('%d of %m')

        excel_file = Workbook('All Employeis Export Report ('+str( file_date )+' ).xlsx')
        sheet1 = excel_file.add_worksheet()

        # Add Formats
        bold = excel_file.add_format({'bold':1})
        
        # Format Columns
        sheet1.set_column(0,2,16)
        sheet1.set_column(3,3,18)

        # Set Headers
        sheet1.write('A1','Name', bold)
        sheet1.write('B1','National ID', bold)
        sheet1.write('C1','Actions', bold)
        sheet1.write('D1','Date', bold)
        sheet1.write('E1','Branch', bold)
        

        # Insert data from database to excel file
        # Get row, column counts
        rowCount = self.tableWidget_10.rowCount()
        columnCount = self.tableWidget_10.columnCount()

        # Loop through that numbers
        sheetRow=0
        for row in range(rowCount):
            sheetRow+=1
            for col in range(columnCount):
                data = self.tableWidget_10.item(row, col).text()
                sheet1.write(sheetRow, col, data)

        # Close Excel file to save
        excel_file.close()


    def Employee_Report_Export(self):
        pass


    ###############################################################
    #### Load Data To ComoBoxies

    def Show_All_Categories(self):
        # Clear Trash
        self.comboBox_25.clear() 
        self.comboBox_25.addItem("---------")
        # self.comboBox_3.clear() 
        # self.comboBox_3.addItem("---------")
        self.comboBox_4.clear() 
        self.comboBox_4.addItem("---------")
        self.comboBox_5.clear() 
        self.comboBox_5.addItem("---------")

        # Get Data from Database
        self.cur.execute("select category_name from category")
        categories = self.cur.fetchall()

        # Insert Data
        for category in categories:
            #print(category[0])
            self.comboBox_25.addItem(category[0])
            # self.comboBox_3.addItem(category[0])
            self.comboBox_4.addItem(category[0])
            self.comboBox_5.addItem(category[0])

    def Show_All_Publishers(self):
        # Clear Trash
        self.comboBox_8.clear() 
        self.comboBox_8.addItem("---------")
        self.comboBox_13.clear() 
        self.comboBox_13.addItem("---------")
        

        # Get Data from Database
        self.cur.execute("select name from publisher")
        publishers = self.cur.fetchall()

        # Insert Data
        for publisher in publishers:
            self.comboBox_8.addItem(publisher[0])
            self.comboBox_13.addItem(publisher[0])

    def Show_All_Authors(self):
        # Clear Trash
        self.comboBox_6.clear() 
        self.comboBox_6.addItem("---------")
        self.comboBox_10.clear() 
        self.comboBox_10.addItem("---------")
        

        # Get Data from Database
        self.cur.execute("select name from author")
        publishers = self.cur.fetchall()

        # Insert Data
        for publisher in publishers:
            self.comboBox_6.addItem(publisher[0])
            self.comboBox_10.addItem(publisher[0])

            



            

    ###############################################################
    #### Settings

    def Add_Branch(self):
        # Get Data About Author
        branch_name = self.lineEdit_23.text()
        branch_code = self.lineEdit_24.text()
        branch_location = self.lineEdit_25.text()

        # Add Data To Database

        # Here to get last id number
        self.cur.execute("select id from branch")
        id = len(self.cur.fetchall())+1

        # Check is There another id same and fix it
        self.cur.execute("select * from branch where id = '{}'".format(id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            id+=1

        data = [(
            id , branch_name , branch_code , branch_location
        )]

        
        self.cur.executemany("insert or ignore into branch values(?,?,?,?)",data)
        

        # Add this Actions in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Add Branch", date, branch_id, branch_name
        )])

        # Save data in database
        self.db.commit()

        # Cleart Fields
        self.lineEdit_23.clear()
        self.lineEdit_24.clear()
        self.lineEdit_25.clear()


        # Notifications
        print("Branch Added !")


    def Add_Category(self):
        # Get Data About Category
        category_name = self.lineEdit_30.text()
        parent_category = self.comboBox_25.currentIndex()

        parent_category_text = self.comboBox_25.currentText()
        
        # Check number range
        if parent_category_text[0]=="-":
            parent_category=0
        

        #Add Data To Database
        self.cur.execute("select id from category") # Here to get last id number
        id = len(self.cur.fetchall()) +1

        # Check is There another id same and fix it
        self.cur.execute("select * from category where id = '{}'".format(id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            id+=1

        data = [(
            id , category_name , parent_category
        )]

        
        self.cur.executemany("insert into category values(?,?,?)",data)

        # Cleart Fields
        self.lineEdit_30.clear()

        # Refreash Data in Combo Box
        self.Show_All_Categories()


        # Add this Aciotn in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Add Category", date, branch_id, category_name
        )])

        # Save data in database
        self.db.commit()


        # Notifications
        print("Category Added !")


    def Add_Publisher(self):
        # Get Data About Publisher
        publisher_name = self.lineEdit_27.text()
        publisher_location = self.lineEdit_26.text()

        # Add Data To Database
        self.cur.execute("select id from publisher") # Here to get last id number
        id = len(self.cur.fetchall())+1

        # Check is There another id same and fix it
        self.cur.execute("select * from author where id = '{}'".format(id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            id+=1

        data = [(
            id , publisher_name , publisher_location
        )]

        
        self.cur.executemany("insert or ignore into publisher values(?,?,?)",data)

        # Cleart Fields
        self.lineEdit_27.clear()
        self.lineEdit_26.clear()



        # Add this Aciotn in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Add Publisher", date, branch_id, publisher_name
        )])

        # Save data in database
        self.db.commit()


        # Notifications
        print("Publisher Added !")
        self.Show_All_Publishers()


    def Add_Author(self):
        # Get Data About Author
        author_name = self.lineEdit_29.text()
        author_location = self.lineEdit_28.text()

        # Add Data To Database
        self.cur.execute("select id from author") # Here to get last id number
        id = len(self.cur.fetchall())+1

        # Check is There another id same and fix it
        self.cur.execute("select * from author where id = '{}'".format(id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            id+=1

        data = [(
            id , author_name , author_location
        )]

        
        self.cur.executemany("insert or ignore into author values(?,?,?)",data)

        # Cleart Fields
        self.lineEdit_29.clear()
        self.lineEdit_28.clear()



        # Add this Aciotn in History
        # Generate History id
        self.cur.execute("select * from history")
        history_id = len( self.cur.fetchall() ) +1
        date = datetime.now().strftime('%d-%m-%Y %H:%M')


        # Check is There another id same and fix it
        self.cur.execute("select * from books where id = '{}'".format(history_id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            history_id+=1

        self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
            history_id, employee_id, "Add Author", date, branch_id, author_name
        )])

        # Save data in database
        self.db.commit()


        # Notifications
        print("Author Added !")
        self.Show_All_Authors()


    ###############################################################
    #### Settings tap Employeis

    # Add a New Employee & save changes in database.
    def Add_Employee(self):
        
        # Get data from feilds
        employee_name = self.lineEdit_31.text()
        employee_mail = self.lineEdit_32.text()

        employee_phone = self.lineEdit_33.text()
        employee_national_id = self.lineEdit_34.text()
        employee_periority = self.lineEdit_35.text()
        branch = self.lineEdit_53.text()

        employee_password = self.lineEdit_36.text()
        employee_repassword = self.lineEdit_37.text()

        date = datetime.now().strftime('%d-%m-%Y %H:%M')

        # Generate id
        self.cur.execute("select * from employee")
        id = len( self.cur.fetchall() ) +1

        # Check is There Employee id same and fix it
        self.cur.execute("select * from employee where id = '{}'".format(id))
        count_id = len( self.cur.fetchall() )
        
        if count_id > 0:
            id+=1
        
        # Check Password
        if employee_password==employee_repassword:
            # Load Data to Database
            data = [
                (id, employee_name, employee_mail, employee_phone, 
                date, employee_national_id, employee_periority, branch, employee_password)
            ]
            print(data)
            self.cur.executemany("insert into employee values(?,?,?,?,?,?,?,?,?)",data)

            

            # Add this Aciotn in History
            # Generate History id
            self.cur.execute("select * from history")
            history_id = len( self.cur.fetchall() ) +1
            # date = datetime.now()


            # Check is There another id same and fix it
            self.cur.execute("select * from books where id = '{}'".format(history_id))
            count_id = len( self.cur.fetchall() )
            
            if count_id > 0:
                history_id+=1

            self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
                history_id, employee_id, "Add Employee", date, branch_id, employee_name
            )])

            # Save data in database
            self.db.commit()

            


            # Notification
            print("Employee "+str(employee_name)+" Added!")
            self.Show_Employee()

        else:
            print("Please Enter Password Again!")

        
    # Chech the password and username from gui and connect with database
    def Check_Employee_toEdit(self):
        # Get data from fields
        employee_name = self.lineEdit_43.text()
        employee_password = self.lineEdit_44.text()

        # Check username and password in databse
        self.cur.execute("select name, password from employee where name like '{}%' and Password = '{}'".format(employee_name,employee_password))
        data = self.cur.fetchall()
        
        # Check is there a data
        if len(data)>0 : # There is a data so complate
            # Search in data about our person
            person_id=0
            for index, person in enumerate(data):
                if person[0]==employee_name  and person[1]==employee_password:
                    person_id=index

            # Check is password is True or False
            if data[person_id][1] == employee_password:
                # Enabel To Edit Employee
                self.groupBox.setEnabled(True)
                print("Connected !! \nand now you can edit employee data")
            else:
                print("Incurrect password !!")

            self.Edit_Employee_Data()
        
        else: # There is no data so stop
            print(" There is no user with this {} name!".format(employee_name))
        
        
    # Show Employee data in fields to edit it
    def Edit_Employee_Data(self):

        # Get username and password from fields
        employee_name = self.lineEdit_43.text()
        employee_password = self.lineEdit_44.text()

        # Get data from database
        self.cur.execute("select phone, national_id, Periority, Branch, Password from employee where name = '{}' and password = '{}'".format(employee_name, employee_password))
        data = self.cur.fetchone()

        # Load data to Fields        
        emplpoyee_phone = self.lineEdit_40.setText(data[0])
        emplpoyee_national_id = self.lineEdit_41.setText(str(data[1]))
        emplpoyee_periority = self.lineEdit_38.setText(str(data[2]))
        emplpoyee_branch = self.lineEdit_52.setText(str(data[3]))
        emplpoyee_password = self.lineEdit_42.setText(data[4])
        emplpoyee_repassword= self.lineEdit_39.setText(data[4])

    # Save the Edits to database    
    def Save_Edit_Employee(self):
        # Get username and password from fields
        username = self.lineEdit_43.text()
        password = self.lineEdit_44.text()

        # Get data to Fields        
        emplpoyee_phone = self.lineEdit_40.text()
        emplpoyee_national_id = self.lineEdit_41.text()
        emplpoyee_periority = self.lineEdit_38.text()
        emplpoyee_branch = self.lineEdit_52.text()
        emplpoyee_password = self.lineEdit_42.text()
        emplpoyee_repassword= self.lineEdit_39.text()


        # Check is password and repassword are currect then complate program
        if emplpoyee_password==emplpoyee_repassword:
            # Qeury string to update data
            sql = """update employee
                set phone = '{0}',
                national_id = '{1}',
                Periority = '{2}',
                Branch = '{3}',
                Password = '{4}'
                where name = '{5}' and password = '{6}'""".format(
                    emplpoyee_phone, emplpoyee_national_id,
                    emplpoyee_periority, emplpoyee_branch,
                    emplpoyee_password, username, password
                )
            self.cur.execute(sql)

            # Add this Aciotn in History
            # Generate History id
            self.cur.execute("select * from history")
            history_id = len( self.cur.fetchall() ) +1
            date = datetime.now().strftime('%d-%m-%Y %H:%M')


            # Check is There another id same and fix it
            self.cur.execute("select * from books where id = '{}'".format(history_id))
            count_id = len( self.cur.fetchall() )
            
            if count_id > 0:
                history_id+=1

            self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
                history_id, employee_id, "Edit Employee", date, branch_id, username
            )])

            # Save data in database
            self.db.commit()


            print("Save_Edit_Employee Done!")



    ###############################################################
    #### Settings tap Permissions & Reports
    def Show_Employee(self):
        # Clear ComboBox
        self.comboBox_29.clear()

        # Get data from database
        self.cur.execute("select name from employee")
        employeis = self.cur.fetchall()

        # Insert data in ComboBox
        for empployee in employeis:
            self.comboBox_29.addItem(empployee[0])

        print("Show_Employee Done!")
        






    # Check the employee permission and check it in GUI
    def Check_empployee_Permissions(self):
        name = self.comboBox_29.currentText() # Get name from field

        # Get data from database
        self.cur.execute("select * from employee_permission where name = '{}'".format(name))
        data = self.cur.fetchone()

        # Simple algorithm to know are all book, client, public or stteing permission is checked!
        # For book
        count_permissions = 0 # To count the size of data checked
        for index  in range(2,7):
            if data[index] == True:
                count_permissions+=1
        if count_permissions==5:
            self.checkBox_30.setChecked(1) # Check ALL ,GUI
        
        # For Client
        count_permissions = 0
        for index  in range(7,12):
            if data[index] == True:
                count_permissions+=1
        if count_permissions==5:
            self.checkBox_31.setChecked(1)

        # For Public
        count_permissions = 0
        for index  in range(12,18):
            if data[index] == True:
                count_permissions+=1
        if count_permissions==6:
            self.checkBox_32.setChecked(1)

        # For Settings
        count_permissions = 0
        for index  in range(18,24):
            if data[index] == True:
                count_permissions+=1
        if count_permissions==6:
            self.checkBox_33.setChecked(1)

        #### Load data to fields
        # Book Permission
        add_book =  self.checkBox.setChecked(data[2])
        edit_book =  self.checkBox_2.setChecked(data[3])
        delete_book =  self.checkBox_3.setChecked(data[4])
        export_book =  self.checkBox_26.setChecked(data[5])
        import_book =  self.checkBox_27.setChecked(data[6])

        # Client Permission
        add_client =  self.checkBox_4.setChecked(data[7])
        edit_client =  self.checkBox_5.setChecked(data[8])
        delete_client =  self.checkBox_6.setChecked(data[9])
        export_client =  self.checkBox_28.setChecked(data[10])
        import_client =  self.checkBox_29.setChecked(data[11])

        # Public Permission
        book_tap =  self.checkBox_7.setChecked(data[12])
        client_tap =  self.checkBox_8.setChecked(data[13])
        dashbourd_tap =  self.checkBox_9.setChecked(data[14])
        history_tap =  self.checkBox_10.setChecked(data[15])
        reports_tap =  self.checkBox_11.setChecked(data[16])
        settings_tap =  self.checkBox_12.setChecked(data[17])

        # Settings Permission
        add_branch =  self.checkBox_21.setChecked(data[18])
        add_publisher =  self.checkBox_20.setChecked(data[19])
        add_author =  self.checkBox_19.setChecked(data[20])
        add_category =  self.checkBox_23.setChecked(data[21])
        add_employee =  self.checkBox_22.setChecked(data[22])
        edit_employee =  self.checkBox_24.setChecked(data[23])

        # Special Permission
        admin = self.checkBox_25.setChecked(data[24])

    

    # Add a permossion to employee and save data in database
    def Add_Employee_Permissions(self):
        # Get name from field
        name = self.comboBox_29.currentText()

        # Special Permission
        admin = self.checkBox_25.isChecked()
        if admin==1: # Make all permissions allowed
            all_book=True
            all_client=True
            all_public=True
            all_employee=True


        ##### Book Permission
        # Special book
        all_book = self.checkBox_30.isChecked() # Check ALL ,GUI
        if all_book==1: # All Book
            # Add value
            add_book =  1
            edit_book =  1
            delete_book =  1
            export_book =  1
            import_book =  1

            # Ckeck in GUI
            self.checkBox.setChecked(1)
            self.checkBox_2.setChecked(1)
            self.checkBox_3.setChecked(1)
            self.checkBox_26.setChecked(1)
            self.checkBox_27.setChecked(1)
        
        else:
            add_book =  self.checkBox.isChecked()
            edit_book =  self.checkBox_2.isChecked()
            delete_book =  self.checkBox_3.isChecked()
            export_book =  self.checkBox_26.isChecked()
            import_book =  self.checkBox_27.isChecked()

        


        ##### Client Permission
        # Special client
        all_client = self.checkBox_31.isChecked()# Check ALL ,GUI
        if all_client==1: # All client
            # Add values
            add_client =  1
            edit_client =  1
            delete_client =  1
            export_client =  1
            import_client =  1

            # Check it in GUI
            self.checkBox_4.setChecked(1)
            self.checkBox_5.setChecked(1)
            self.checkBox_6.setChecked(1)
            self.checkBox_28.setChecked(1)
            self.checkBox_29.setChecked(1)
        
        else:
            add_client =  self.checkBox_4.isChecked()
            edit_client =  self.checkBox_5.isChecked()
            delete_client =  self.checkBox_6.isChecked()
            export_client =  self.checkBox_28.isChecked()
            import_client =  self.checkBox_29.isChecked()
        
        

        #### Public Permission
        # Special public
        all_public = self.checkBox_32.isChecked()# Check ALL ,GUI
        if all_public==1: # All public
            # Add Value
            book_tap =  1
            client_tap =  1
            dashbourd_tap = 1
            history_tap =  1
            reports_tap =  1
            settings_tap =  1

            # Check it in GUI
            self.checkBox_7.setChecked(1)
            self.checkBox_8.setChecked(1)
            self.checkBox_9.setChecked(1)
            self.checkBox_10.setChecked(1)
            self.checkBox_11.setChecked(1)
            self.checkBox_12.setChecked(1)
        else:
            book_tap =  self.checkBox_7.isChecked()
            client_tap =  self.checkBox_8.isChecked()
            dashbourd_tap =  self.checkBox_9.isChecked()
            history_tap =  self.checkBox_10.isChecked()
            reports_tap =  self.checkBox_11.isChecked()
            settings_tap =  self.checkBox_12.isChecked()

        


        #### Settings Permission
        # Special employee
        all_employee = self.checkBox_33.isChecked()# Check ALL ,GUI
        if all_employee==1: # All employee
            # Add Values
            add_branch =  1
            add_publisher =  1
            add_author =  1
            add_category =  1
            add_employee =  1
            edit_employee =  1

            self.checkBox_21.setChecked(1)
            self.checkBox_20.setChecked(1)
            self.checkBox_19.setChecked(1)
            self.checkBox_23.setChecked(1)
            self.checkBox_22.setChecked(1)
            self.checkBox_24.setChecked(1)

        else:
            add_branch =  self.checkBox_21.isChecked()
            add_publisher =  self.checkBox_20.isChecked()
            add_author =  self.checkBox_19.isChecked()
            add_category =  self.checkBox_23.isChecked()
            add_employee =  self.checkBox_22.isChecked()
            edit_employee =  self.checkBox_24.isChecked()



        # Simple Algorithm to know edit permission or add for first time
        self.cur.execute("select name from employee_permission where name = '{}'".format(name))
        check_name = len( self.cur.fetchall() )
        
        if check_name == 0: # Add Permission for first time
            # Generate id
            self.cur.execute("select * from employee_permission")
            id = len( self.cur.fetchall() ) +1
            
            
            # Check is There another id same and fix it
            self.cur.execute("select * from employee_permission where id = '{}'".format(id))
            count_id = len( self.cur.fetchall() )
            
            if count_id > 0:
                id+=1

            #### Insert data in databse
            data = [(id, name,
                add_book, edit_book, delete_book,export_book, import_book,
                add_client, edit_client, delete_client, export_client, import_client,
                book_tap, client_tap, dashbourd_tap, history_tap, reports_tap, settings_tap,
                add_branch, add_publisher, add_author, add_category, add_employee, edit_employee,
                admin
            )]

            self.cur.executemany("insert into employee_permission values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",data)

            # Add this Aciotn in History
            # Generate History id
            self.cur.execute("select * from history")
            history_id = len( self.cur.fetchall() ) +1
            date = datetime.now().strftime('%d-%m-%Y %H:%M')


            # Check is There another id same and fix it
            self.cur.execute("select * from books where id = '{}'".format(history_id))
            count_id = len( self.cur.fetchall() )
            
            if count_id > 0:
                history_id+=1

            self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
                history_id, employee_id, "Add Employee Permissions", date, branch_id, name
            )])

            # Save data in database
            self.db.commit()


            print("Add Employee {} permission done".format(name))

       
        elif check_name != 0: # Update employee permissions
            # Query to update data
            sql = """update employee_permission
                    set add_book = {0}, 
                    edit_book = {1}, 
                    delete_book = {2},
                    export_book = {3}, 
                    import_book = {4},
                        add_client = {5}, 
                        edit_client = {6}, 
                        delete_client = {7}, 
                        export_client = {8}, 
                        import_client = {9},
                            book_tap = {10}, 
                            client_tap = {11}, 
                            dashbourd_tap = {12}, 
                            history_tap = {13}, 
                            reports_tap = {14}, 
                            settings_tap = {15},
                        add_branch = {16}, 
                        add_publisher = {17}, 
                        add_author = {18}, 
                        add_category = {19}, 
                        add_employee = {20}, 
                        edit_employee = {21},
                    admin = {22}
                where name = '{23}'
                     """.format(
                         add_book, edit_book, delete_book,export_book, import_book,
                        add_client, edit_client, delete_client, export_client, import_client,
                        book_tap, client_tap, dashbourd_tap, history_tap, reports_tap, settings_tap,
                        add_branch, add_publisher, add_author, add_category, add_employee, edit_employee,
                        admin ,
                        name
                     )

            self.cur.execute(sql)


            # Add this Aciotn in History
            # Generate History id
            self.cur.execute("select * from history")
            history_id = len( self.cur.fetchall() ) +1
            date = datetime.now().strftime('%d-%m-%Y %H:%M')


            # Check is There another id same and fix it
            self.cur.execute("select * from books where id = '{}'".format(history_id))
            count_id = len( self.cur.fetchall() )
            
            if count_id > 0:
                history_id+=1

            self.cur.executemany("insert into history values (?,?,?,?,?,?)",[(
                history_id, employee_id, "Edit Employee Permissions", date, branch_id, name
            )])

            # Save data in database
            self.db.commit()


            print("Update Employee {} permission done".format(name))



    def Admin_Report(self):
        pass   



    ###############################################################
    #### Open Taps when Click Buttons
    

    def Open_Login_Tap(self):
        self.tabWidget.setCurrentIndex(0)
    
    def Open_Reset_Password_Tap(self):
        self.tabWidget.setCurrentIndex(1)
    
    def Open_Daily_Movment_Tap(self):
        self.tabWidget.setCurrentIndex(2)
        self.TaodayWidget.setCurrentIndex(0)

        # Refresh Data

        tableName = self.tableWidget_2
        hpTool.showDailyBooks({'table':tableName})
        
        
    def Open_Books_Tap(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        self.Show_All_Books()

        # Set defaut image
        self.pixmap = QPixmap(default_book_image)

        # Add Image to Label
        self.label_19.setPixmap(self.pixmap)








    
    def Open_Clients_Tap(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)
        self.Show_All_Clients()

        # Show Data in Tables
        self.Show_All_Clients()

    
    def Open_Dashboard_Tap(self):
        self.tabWidget.setCurrentIndex(5)

    def Open_History_Tap(self):
        self.Show_Hitory()
        self.tabWidget.setCurrentIndex(6)

    def Open_Reports_Tap(self):
        self.tabWidget.setCurrentIndex(7)
        self.tabWidget_5.setCurrentIndex(0)

        # Refresh data
        self.Show_All_Book_Reports()
        self.Show_All_Client_Reports()
        self.Show_Employee_Report()

        

        



    def Open_Settings_Tap(self):
        self.tabWidget.setCurrentIndex(8)
        self.tabWidget_4.setCurrentIndex(0)

        # Refreash Employee ComboBox data ,check GUI
        self.Show_Employee()



        






def Show_Login():

    app = QApplication(sys.argv)
    window = login_frame.Login()
    window.show()
    app.exec_()


    
 


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    Show_Login()
    
    if login_frame.loginStatus == True :
        main()