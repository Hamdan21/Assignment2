import statistics
import csv
import plotter

def quit():
    answer=input(("Are you sure? Y/N"))
    if answer in "yY":
        return(True)
    else:
        return(False)

def main():
    try:
        inp = input(("Enter a command>>"))
        words = inp.split()     #Splits the input provided by the user into a list
        if words[0]=='quit':    #words[0] is the first word provided by the user
            if quit()==True:
                print("Goodbye!")
            else:
                main()
        elif words[0]=='stu':
            x=student_average(words)
            if x==True:
                print("Plot finished (window may be hidden).")
            elif x==False:
                print("Plot failed (no such student).")
        elif words[0]=='avg':
            print_average(words)
        elif words[0]=='cavg':
            class_average(words)
            print("Plot is finished (window may be hidden).")

        elif words[0]=='help':
            help()
    except:   
        if inp=='':         #If there is no input provided by the user
            print("Enter a command or 'quit' to quit.")
        main()

def student_average(details):
    try:
        with open(details[1], 'r') as f:
            grades = []     #Initializing grades as an empty list
            lines = csv.reader(f)
            next(lines)
            for i in lines:     #Looping through each line in file
                line = i
                if line[0] == details[2] and line[1] == details[3]:  #line[0] is last name,line[1] is first name
                    for j in range(2,len(line)):        #Starting loop from 2 since we don't need Firstname and lastname
                        grades.append(float(line[j]))   #Adding each grade to the list grades
                    print(grades)
        plotter.x_axis_label("Name")
        plotter.y_axis_label("Grade")
        plotter.title("My graph")
        for grade in grades:            #Looping through each grade in grades list for plotting
            plotter.add_data_point(grade)   #Plotting each grade in graph
        plotter.plot()
        input("Press enter to continue")    #Keeps the window open until user provides an input
        return(True)

    except ValueError:
        print("Usage: stu <filename> <first name> <last name>")
    except FileNotFoundError:
        print("No such file:",details[1])

def print_average(details):
    try:
        f=open(details[1])      #details[1] is the filename
        grades=[]
        lines=f.readlines()     #reads all the lines in the file
        for i in range(1,len(lines)):
            line=lines[i]
            det=line.split(',')
            numb=int(details[2])+2
            grades.append(float(det[numb]))     #adds each grade to the list grades
        print(grades)
        avg=statistics.mean(grades)             #finds the mean of the grades
        print("Average:",avg)
        return(avg)
    except AttributeError:
        print("Usage: avg <filename> <grade item>")
        return(-1)
    except FileNotFoundError:
        print("No such file:", details[1])
        return(-1)
    except SyntaxError:
        print("Grade item must be a number.")
        return(-1)

def class_average(details):
    try:
        with open(details[1], 'r') as f:
            quiz = []       #Initilaizing each assignment/quiz to empty lists
            a1_1 = []
            a1_3 = []
            a2_1 = []
            a2_2 = []
            a3_1 = []
            a4_1 = []
            a5_1 = []
            a6_1 = []
            ass=[]
            lines = csv.reader(f)
            print(lines)
            next(lines)
            for i in lines:     #Loops through each line in the file
                line = i
                for j in range(2,len(line)):   #Loop starts from 2 since we are ignoring FirstName and LastName
                    if j==2:                   #If j is the second index
                        quiz.append(float(line[j])) #appends the quiz grade in the list
                    elif j==3:
                        a1_1.append(float(line[j]))
                    elif j==4:
                        a1_3.append(float(line[j]))
                    elif j==5:
                        a2_1.append(float(line[j]))
                    elif j==6:
                        a2_2.append(float(line[j]))
                    elif j==7:
                        a3_1.append(float(line[j]))
                    elif j==8:
                        a4_1.append(float(line[j]))
                    elif j==9:
                        a5_1.append(float(line[j]))
                    elif j==10:
                        a6_1.append(float(line[j]))
                    elif j==11:
                        ass.append(float(line[j]))
            quiz=statistics.mean(quiz)       #mean of quiz
            a11 = statistics.mean(a1_1)      #mean of a1_1
            a13= statistics.mean(a1_3)       #mean of a1_3
            a21= statistics.mean(a2_1)       #mean of a2_1
            a22= statistics.mean(a2_2)       #mean of a2_2
            a31= statistics.mean(a3_1)       #mean of a3_1
            a41= statistics.mean(a4_1)       #mean of a4_1
            a51= statistics.mean(a5_1)       #mean of a5_1
            a61= statistics.mean(a6_1)       #mean of a6_1
            ass= statistics.mean(ass)        #mean of assignment1
            avgs=[quiz,a11,a13,a21,a22,a31,a41,a51,a61,\
                  ass]
            plotter.x_axis_label("Name")
            plotter.y_axis_label("Grade")
            plotter.title("My graph")
            for avg in avgs:                #Loops through each avg in avgs
                plotter.add_data_point(avg)
            plotter.plot()
            input("Enter to continue")
    except ValueError:
        print("Usage: cavg <filename>")
    except FileNotFoundError:
        print("No such file:",details[0])

def help():
    print("stu <filename> <first name> <last name> - plot student grades",\
          "cavg <filename> - plot class average",\
          "avg <filename> <number> - prints the average for the grade item",\
          "quit - quits",\
          "help - displays this message",sep="\n")
main()


