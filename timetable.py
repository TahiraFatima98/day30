timetable1=['monday', 'OB','OB','OB','MPI','NM']
timetable2=['tuesday','MPI LAB','VLSI']
timetable3=['wednesday','VLSI','MPI', 'VLSI LAB']
timetable4=['thursday','NM','NM','MPI','VLSI']
timetable5=['Friday', 'FYP DAY']
name= input('Enter your name: ')
print("Welcome "+ name + " to your timetable")
day=input("Enter a day between monday and friday: ")
if day=='monday':
    print('your subjects for '+ timetable1[0]+ ' are:' + '\n'+timetable1[1] + '\n'+timetable1[2] + '\n'+timetable1[3] + '\n'+timetable1[4] + '\n'+timetable1[5])
elif day=='tuesday':
    print('your subjects for '+ timetable2[0]+ ' are:' + '\n'+timetable2[1] + '\n'+timetable2[2])
elif day=='wednesday':
    print('your subjects for '+ timetable3[0]+ ' are:' + '\n'+timetable3[1] + '\n'+timetable3[2] + '\n'+timetable3[3])
elif day=='thursday':
    print('your subjects for '+ timetable4[0]+ ' are:' + '\n'+timetable4[1] + '\n'+timetable4[2] + '\n'+timetable4[3] + '\n'+timetable4[4])
elif  day=='friday':
    print(timetable5[0] + '\n'+timetable5[1])
else:
    print('Invalid entry')
    
    
        

