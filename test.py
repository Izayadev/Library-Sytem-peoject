flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
Frame.setWindowFlags(flags)
Frame.setAttribute(QtCore.Qt.WA_TranslucentBackground)

self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 185, 100)))
self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))

self.pushButton.clicked.connect(self.login)

    def login(self):
        global id, done

        accses=[0, 0]
        bitaData=[]
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        bitaData.append(username)
        bitaData.append(password)

        # Check my own username & password
        if username=='admin' and password=='000':
            print(username)
            print(password)
            its_me=1
            accses[0]=its_me
            #### Insert data into database
            # Generate id
            self.cur.execute("select * from login")
            id = len( self.cur.fetchall() )+1

            # Check is There another id same and fix it
            self.cur.execute("select * from login")
            count_id = len( self.cur.fetchall() )
            
            if count_id > 0:
                id+=1
            self.cur.executemany("insert into login values (?,?,?,?,?)",[(
                id, username, password, 1, 0
            )])
            
            self.db.commit()
            
        else:
            print(username)
            print(password)
            # Check data to login
            self.cur.execute("select password, name from employee where name = '{}' and Password = '{}'".format(username, password))
            data = self.cur.fetchall()

            if len( data ) != 0:
                print(" Login Done")

                #### Insert data into database
                # Generate id
                self.cur.execute("select * from login")
                id = len( self.cur.fetchall() )+1

                # Check is There another id same and fix it
                self.cur.execute("select * from login")
                count_id = len( self.cur.fetchall() )
                
                if count_id > 0:
                    id+=1
                self.cur.executemany("insert into login values (?,?,?,?,?)",[(
                    id, username, password, 0, 0
                )])
                self.db.commit()

                
        
            else:
                print("There is no account with this {} username".format(username))
  


        done=1
        QtWidgets.qApp.quit()
            
            