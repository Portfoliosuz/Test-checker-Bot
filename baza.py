import sqlite3
import sinov
def addstudent(tkod,studentname,studentuser,njavoblar,id):
    conn = sqlite3.connect('database.db')
    info=conn.cursor()
    nl = 0
    for s in njavoblar:
        if s == ',':
            nl += 1          
    info.execute(f"""
        insert into '{tkod}' values ('{studentname}','{studentuser}','{njavoblar}','{nl}','{id}')
    """)   
    conn.commit()
    conn.close()
def give_natija(tkod):
    nl = 0
    natijalar = ''
    conn = sqlite3.connect('database.db')
    info=conn.cursor()
    info.execute(f"""
                select rowid,studentname,studentuser,njavoblar from '{tkod}' order by lenn
    """)
    natija  = info.fetchall()
    print(natija)
    nate = 0
    ball = ['🥇', '🥈', '🥉']
    for i in natija: 
        for s in i[3]:
            if s == ',':
                nl += 1          
        if nate<len(ball):
            natijalar +=ball[nate]+ ' '+f'<b>{str(i[1])}</b>'+' '+ str(nl) +'❌\n'
            nate+=1
        else:
            nate+=1
            natijalar +=str(nate)+ ' '+f'<b>{str(i[1])}</b>'+' '+ str(nl) +'❌\n'
        nl = 0
    return natijalar 
    conn.commit()
    conn.close()
def addtable(id):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""create table if not exists'{id}' (tkod number,javoblar text)""")
    conn.commit()
    conn.close()
def addtest(id,tkod,javoblari):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
              insert into '{id}' values(
                  '{tkod}','{javoblari}'
                  
              )
    
    """)
    info.execute(f"""
            insert into kodlar values(
                '{tkod}'
            )
    """)
    info.execute(f"""
            insert into datajavoblar values(
        '{tkod}','{javoblari}'
    )
    """)
    info.execute(f"""
                insert into kod_user values(
                        '{tkod}','{id}'
                )

    """)
    info.execute(f"""
        create table if not exists'{tkod}'(
            studentname text,
            studentuser text,
            njavoblar text,
            lenn number,
            id number

        )
    """)
    conn.commit()
    conn.close()
def deletetable(id):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
        select tkod from kod_user where id = {id}
    """)
    requ = info.fetchall()
    if requ:
        for i in requ:
            info.execute(f"drop table '{i[0]}'") 
            info.execute(f"delete from kodlar where kod = {i[0]}")
            info.execute(f"delete from datajavoblar where tkod = {i[0]}")
            info.execute(f"delete from kod_user where tkod = {i[0]}")
            info.execute(f""" delete from tkod_student where kod = {i[0]}""")
    info.execute(f"""
        drop table '{id}'

""")   
    conn.commit()
    conn.close()

def deletetest(id,tkod):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
               delete from '{id}' where tkod = '{tkod}'
    
    """)
    info.execute(f"""
                delete from kodlar where kod = '{tkod}'
    
    """)
    info.execute(f"""
                delete from datajavoblar where tkod = '{tkod}'

    """)
    info.execute(f"""
                delete from kod_user where tkod = '{tkod}'

    """)
    info.execute(f"""
            drop table '{tkod}'

    """)
    info.execute(f"""
        delete from tkod_student where kod = {tkod}

""")
    conn.commit()
    conn.close()
def give_me_answers(id,tkod):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
               select javoblar from '{id}' where tkod = '{tkod}'
    
    """)
    return info.fetchall()[0][0]
    conn.commit()
    conn.close()
def exprement(id):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
            select * from '{id}'
    
    """)
    return info.fetchall()
    conn.commit()
    conn.close()
def tkod():
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""select kod from kodlar""")
    return info.fetchall()
    conn.commit()
    conn.close()
def tkodlist():
    kodlar = []
    for i in tkod():
        kodlar.append(i[0])
    return kodlar
def datanswershow(kod):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
                select javoblar from datajavoblar where tkod = '{kod}'

    """)
    return info.fetchall()[0][0]
    conn.commit()
    conn.close()
def kod_usershow(tkod):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
                select id from kod_user where tkod= '{tkod}'
    """)
    return info.fetchall()[0][0]
    conn.commit()
    conn.close()
def give_tkod(id):
    tkoda = []
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
                select tkod from '{id}'
    """)
    info = info.fetchall()
    for i in info:
        tkoda.append(i[0])
    return tkoda
    conn.commit()
    conn.close()
def tkod_userid(kod,studentid,njavoblar):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""insert into tkod_student values(
        '{kod}','{studentid}','{njavoblar}'
    )""")
    conn.commit()
    conn.close()
def get_studentid(kod):
    users = []
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""
        select userid,njavoblar from tkod_student where kod = '{kod}'
    """)
    info = info.fetchall()
    for i in info:   
        users.append([i[0],i[1]])
    return users
    conn.commit()
    conn.close()
def delpupil(kod,id):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""delete from '{kod}' where id='{id}'""")
    conn.commit()
    conn.close()
def give_del_user(tkod,id):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""select studentname from '{tkod}' where id='{id}'""")
    return info.fetchone()[0]
    conn.commit()
    conn.close()
def finduserid(tkod,id):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""select '{id}'from '{tkod}' where id='{id}'""")
    return info.fetchall()
    conn.commit()
    conn.close()
def clearbase(message):
    li = []
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    info.execute(f"""select user from allusers""")
    for i in info.fetchall():
        if sinov.usertekshiruvi(i[0] , message):
            if i[0] in li:
                pass
            else:
                li.append(i[0])
        else:
            try:
                deletetable(i[0])
            except:
                pass
    li.append(len(li))
    return li
    conn.commit()
    conn.close()
def start(id = 123456789):
    conn = sqlite3.connect('database.db')
    info = conn.cursor()
    users =  info.execute("select user from allusers").fetchall()
    if (f'{id}',) in users:
        pass
    else:
        info.execute(f"""insert into allusers values('{id}')""")
    conn.commit()
    conn.close()
    return len(users)