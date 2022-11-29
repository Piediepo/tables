dict2 = {'onoma':'maria',
        'phone':' 67890'}
dict1 = {'onoma':'kostas',
        'phone':'12345'}
import sqlite3
connection = sqlite3.connect('mathites.db')

cursor = connection.cursor()

cursor.execute(
    '''
        create table if not exists mathites(
            id integer primary key,
            name text,
            phone text)
    ''')
cursor.execute(
    ''' Select count (*) from mathites
    ''')

records=cursor.fetchall()
print records

record=records[0]
print record
if record[0]==0:
    cursor.execute('INSERT INTO mathites(name,phone) VALUES("kostas","123456")')
    cursor.execute('INSERT INTO mathites(name,phone) VALUES("maria","67890")')
    connection.commit()
names=[dict1,dict2]
while True:
 
    i = 1
    for item in names:
        print i,item['onoma'], item['phone']
        i += 1
    print "1:eisagogi 2:diagrafi 3:epeksergasia 4:taksinomisi 9:eksodos"
    s=input()
    if s == 9:
        exit()
    elif s == 1:
        k=raw_input('dose onoma ')
        names.append(k) 
    elif s == 2:
        m=input('pio thes na sbisis ')
        names.pop(m-1)
    elif s == 3:
        f=input('dose thesi ')
        o=raw_input('dose onoma ')
        names[f-1]=o
    
        

