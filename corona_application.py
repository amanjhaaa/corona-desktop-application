# first project 


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("",'end',values = i)

#will search the data from database by using country name and continent name 

def search():
    q2 = q.get()
    query = "SELECT * FROM coronaUpdate WHERE Country_Name LIKE '%"+q2+"%'OR continent_region LIKE '%"+q2+"%'"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

def clear():
    query = "SELECT * FROM CoronaUpdate"
    mycursor.execute(query)
    row = mycursor.fetchall()
    update(rows)
    


def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    #print(item['values'][5])
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])
    t7.set(item['values'][6])
    t8.set(item['values'][7])

#  updation of coronatable row can be updated only by giving id    
def update_coronadata():
    country = t1.get()
    continent = t2.get()
    totalcases = t3.get()
    totaldeath = t4.get()
    totalrecovery = t5.get()
    corona_id = t8.get()
    
    
    if messagebox.askyesno("Confirm please","Are you sure you want to update the corona data!!"):
        query = "UPDATE coronaupdate SET Country_Name = %s,Continent_Region = %s, New_Cases = %s, New_Death = %s, New_Recovery = %s WHERE id = %s"
        value = (country,continent,totalcases,totaldeath,totalrecovery,corona_id)
        mycursor.execute(query,value)
        conn.commit()
        clear()
    
    else:
        return True 
        
def add_new():
    country = t1.get()
    continent = t2.get()
    totalcases = t3.get()
    totaldeath = t4.get()
    totalrecovery = t5.get()
    query = "INSERT INTO coronaupdate (Country_Name,Continent_Region,New_Cases,New_Death,New_Recovery,Created_Date,Modified_Date,id) VALUES (%s, %s, %s, %s, %s,NOW(),NOW(),NULL)"
    mycursor.execute(query, (country,continent,totalcases,totaldeath,totalrecovery))
    conn.commit()
    clear()


#   it is connected with event handling ,deletion of any row can be possible if we double click on that row and delete that  
def delete_CoronaData():
    
    corona_id = t8.get()
    if messagebox.askyesno("Confirm delete?","are you sure to delete this corona data!!!!"):
        query = "DELETE FROM coronaUpdate WHERE id ="+corona_id
        
        mycursor.execute(query)
        conn.commit()
        clear()
    else:
        return True
    

conn = pymysql.connect(host = "localhost", user = "root", passwd = "Amanjha@123",database = "aman")
mycursor=conn.cursor()
# conn.insert_id()






root = Tk()
root.title("Corona update")
#root.geometry("800x700")

q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()

wrapper1 = LabelFrame(root,text = "World corona list")
wrapper2 = LabelFrame(root,text = "Search")
wrapper3 = LabelFrame(root,text = "corona country data")

wrapper1.pack(fill = BOTH,expand = TRUE,padx = 20,pady = 10)
wrapper2.pack(fill = BOTH,expand = TRUE,padx = 20,pady = 10)
wrapper3.pack(fill = BOTH,expand = TRUE,padx = 20,pady = 10)


trv = ttk.Treeview(wrapper1,show = "headings",height = "6")
trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8") 
trv.column("1", width = 90, anchor ='ne') 
trv.column("2", width = 120, anchor ='ne') 
trv.column("3", width = 90, anchor ='ne')
trv.column("4", width = 90, anchor ='ne')
trv.column("5", width = 90, anchor ='ne')
trv.column("6", width = 90, anchor ='ne')
trv.column("7", width = 90, anchor ='ne') 
trv.column("8", width = 90, anchor ='ne')

trv.pack()

trv.heading(1,text = "country_name")
trv.heading(2,text = "continent_region")
trv.heading(3,text = "new_case")
trv.heading(4,text = "new_death")
trv.heading(5,text = "new_recovery")
trv.heading(6,text = "created_date")
trv.heading(7,text = "Modified_date")
trv.heading(8,text = "id")

trv.bind("<Double-1>",getrow) # will be accessed by clicking double to the left key .

query = "SELECT * FROM coronaupdate"
mycursor.execute(query)
rows = mycursor.fetchall()

update(rows)


#seae=rch section

lbl = Label(wrapper2,text = "search")
lbl.pack(side = LEFT,padx =10)

ent = Entry(wrapper2,textvariable = q)
ent.pack(side = "left",padx = 6)

btn = Button(wrapper2,text = "Search",command = search)
btn.pack(side = LEFT,padx = 6)

clearbtn = Button(wrapper2,text = "clear",command = clear)
clearbtn.pack(side = "left",padx = 6)


# user data section


lbl1 = Label(wrapper3,text = "CountryName")
lbl1.grid(row = 0,column = 0,padx = 4,pady = 3)
ent1 = Entry(wrapper3,textvariable = t1)
ent1.grid(row = 0,column = 1,padx = 4,pady = 3)

countrychoosen = ttk.Combobox(wrapper3,width = 20,textvariable = t1)
countrychoosen.grid(row= 0, column= 1)


countrychoosen['values'] = ("Afghanistan","Albania","Algeria","Andorra","Angola","Antigua","Argentina","Armenia","Australia","Austria","Azerbaijan",
'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia ','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi',
'Cambodia','Cameroon','Canada','Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo','DR Congo','Costa Rica','Croatia','Cuba','Cyprus','Czech Republic',
'Democratic Republic of the Congo','Denmark','Djibouti','Dominica','Dominican Republic',
'East Timor','Ecuador','Egypt','El Salvador','Equatorial Guinea','Ethiopia',
'Fiji','Finland','France',
'Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala',',Guinea','Guinea-Bissau','Guyana',
'Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Ivory Coast',
'Jamaica','Japan','Jordan',
'Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyzstan',
'Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg',
'Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique',
'Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Korea','Norway',
'Oman',
'Pakistan','Philippines','Poland','Peru','Portugal','Papua New Guinea','Paraguay','Palestine State','Panama','Palau',
'Qatar',
'Romania','Russia','Rwanda',
'Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia',
'Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka',
'Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria',
'Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu',
'Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan',
'Vanuatu','Vatican City','Venezuela','Vietnam',
"Wales","Western Sahara","Western Samoa","WA Self",
"Yemen",
"Zambia","Zimbabwe"
)





lbl2 = Label(wrapper3,text = "continent_Region")
lbl2.grid(row = 1,column = 0,padx = 4,pady = 3)
ent2 = Entry(wrapper3,textvariable = t2)
ent2.grid(row = 1,column = 1,padx = 4,pady = 3)


continentchoosen = ttk.Combobox(wrapper3,width = 20,textvariable = t2)
continentchoosen.grid(row = 1,column = 1)

continentchoosen['values'] = ("Asia","Africa","North America","South America","Australia/oceania","Antarctica","Europe")



lbl3 = Label(wrapper3,text = "New_Case")
lbl3.grid(row = 2,column = 0,padx = 4,pady = 3)
ent3 = Entry(wrapper3,textvariable = t3)
ent3.grid(row = 2,column = 1,padx = 4,pady = 3)

lbl4 = Label(wrapper3,text = "New_Death")
lbl4.grid(row = 3,column = 0,padx = 4,pady = 3)
ent4 = Entry(wrapper3,textvariable = t4)
ent4.grid(row = 3,column = 1,padx = 4,pady = 3)

lbl5 = Label(wrapper3,text = "New_Recovery")
lbl5.grid(row = 4,column = 0,padx = 4,pady = 3)
ent5 = Entry(wrapper3,textvariable = t5)
ent5.grid(row = 4,column = 1,padx = 4,pady = 3)

# lbl6 = Label(wrapper3,text = "Created_Date")
# lbl6.grid(row = 5,column = 0,padx = 4,pady = 3)
# ent6 = Entry(wrapper3,textvariable = t6)
# ent6.grid(row = 5,column = 1,padx = 4,pady = 3)

# lbl7 = Label(wrapper3,text = "Modified_Date")
# lbl7.grid(row = 6,column = 0,padx = 4,pady = 3)
# ent7 = Entry(wrapper3,textvariable = t7)
# ent7.grid(row = 6,column = 1,padx = 4,pady = 3)

lbl8 = Label(wrapper3,text = "id")
lbl8.grid(row = 7,column = 0,padx = 4,pady = 3)
ent8 = Entry(wrapper3,textvariable = t8)
ent8.grid(row = 7,column = 1,padx = 4,pady = 3)

update_btn = Button(wrapper3,text = "update",command = update_coronadata)
add_btn = Button(wrapper3,text = "Add new",command = add_new)
delete_btn = Button(wrapper3,text = "delete ",command = delete_CoronaData)

add_btn.grid(row = 8,column = 0,padx = 5,pady = 3)
update_btn.grid(row = 8,column = 1,padx = 5,pady = 3)
delete_btn.grid(row = 8,column = 2,padx = 5,pady = 3)


countrychoosen.current(0)
continentchoosen.current(0)


root.mainloop()



#Database query for making table and databases
# use aman;
# create table coronaupdate(
# Country_Name varchar(255),
# Continent_Region varchar(255),
# New_Cases varchar(255),
# New_Death varchar(255),
# New_Recovery varchar(255),
# Created_Date datetime,
# Modified_Date datetime,
# id INT AUTO_INCREMENT,
# PRIMARY KEY(id)
# );
# select * from coronaupdate;
# drop table coronaupdate;
# ALTER TABLE coronaupdate AUTO_INCREMENT=0;

# DROP TABLE  aman.coronaupdate;
# DROP TABLE coronaupdate;
# DROP TABLE database_name.table_name;
# show tables;
