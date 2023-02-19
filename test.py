from index import Main
a=Main

empty = 0

class Tool():  


    def checkFileds(self,fields): # --> Tool to Check.
        """Check the fields passed.\n
        fields --> pass the fields in dictionary as {FieldName : FieldData}."""

        fieldsStatus = True
        
        # WORK
        for field in fields:
            if len( fields[field] ) == empty:
                print("Please {} cannot be empty.".format(field) )
                fieldsStatus = False
                break

        # OUTPUT
        return fieldsStatus

    def did(self): 
        
        self.pushButton_22.clicked.connect(self.prnt())

    def prnt(self):
        print("oh yeah!!")

