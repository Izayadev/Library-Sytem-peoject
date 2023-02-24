# This class is to work with excel files
from numpy import empty_like
from xlsxwriter import *
import Database, Tools
import DateFile as date
db = Database.ConnectSqlite3()


class BookReports():

        
    def exportBookReport(self, objects):
        """The list of books in book tab exported as excel file.\n
        objects are --> employee id, branch id"""

        # VARIABLES
        currentDate = date.dofmDate
        employee = objects['employee id']
        branch = objects['branch id']

        # GET
        bookData = db.getAll("select code, title, category_id, author_id, price from books")
        
        
        """=========== EXCEL FILE SETTING ============="""
        # SET FILE
        excelFile = Workbook('Book Export Report ('+str( currentDate )+' ).xlsx')
        thisSheet = excelFile.add_worksheet()

        # Add Formats
        bold = excelFile.add_format({'bold':1})
        money_format = excelFile.add_format({"num_format": '$#,##0'})
        
        # Format Columns
        thisSheet.set_column(0,3,18)

        # Set Headers
        thisSheet.write('A1','Book Code', bold)
        thisSheet.write('B1','Book Title', bold)
        thisSheet.write('C1','Category', bold)
        thisSheet.write('D1','Author', bold)
        thisSheet.write('E1','Price', bold)


        # Insert data from database to excel file
        for row, form in enumerate(bookData):
            row+=1
            for col, item in enumerate(form):
                # Get real data name for category and author
    
                if col==4:
                    thisSheet.write(row, col, item, money_format)
                    
                else:
                    thisSheet.write(row, col, item)


        # Close Excel file to save
        excelFile.close()

        # Save action to history
        if branch == Tools.adminAccess:
            thisData = {'employee id':"Admin", 'branch id':"Admin", 'action':"export book's list", 'extra':'from Book tab'} 
        else:
            thisData = {'employee id':employee, 'branch id':branch, 'action':"export book's list", 'extra':'from Book tab'} 

        Tools.SaveActionToHistory(thisData)
