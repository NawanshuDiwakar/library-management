qvalue=('No',Book_name)
c=con.cursor()
c.execute(query1,qvalue)
con.commit()
print("-"*60,'your data entered successfully',"-"*60)
print('Bookname',Book_name)
print('Accession No.',Accession_number)
print('-'*60,'your data entered successfully',"-"*60)

def IssueBook():
query=('select * from books')
c=con.cursor()
c.execute(query)
res=c.fetchall()
print('-'*60)
print('list of books')
for i in res:
   print('Book_Name:',i[1])
print('-'*60)
Book_name=str(input('enter book name:'))
if res == Book_name :
   print('book cannot be issued')
   print('search for another book')
   IssueBook()
else:
   print('book can be issued')
   Student_name=str(input('enter student name:'))
   accession_number=int(input('enter accession number.:'))
   Book_name=str(input('enter book name:'))
   
   
