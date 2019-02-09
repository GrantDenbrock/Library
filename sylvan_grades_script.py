#~~
#This script is meant to create and manage a dataframe of student grade tracking data.
#It should be easily usable by people with little/no experience with python.
#It requires an input csv file and writes out to the same file once operations are completed.
#~~
# updated version should include an add_grades function that automatically references a new df for each student,
#contining classes and graded and automatically populated with todays date at top of each column.
#~~
import pandas as pd
import argparse
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def parse_args():
    parser = argparse.ArgumentParser(
        description="This script takes an input file generated from chromstats, and creates a dataframe and plots.")

    parser.add_argument(
        '--input_file', required = True, default = 'sylvan_gradebook.csv',  help = 'A csv file of student data.')

    args = parser.parse_args()

    return args
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def begin():
    prompt = input('What would you like to do? 1. Inquire for student, 2. Add student, 3. Print entire dataframe.')
    if prompt == '1':
        inquire()
    if prompt == '2':
        name = input('enter students name')
        username = input('enter their username')
        password = input('enter their password')
        site = input('enter the url of the gradebook')
        add_student(str(name),str(username),str(password),str(site))
    if prompt == '3':
        print(df)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ok so now that I can store all this in a dataframe I want to be able to inquire by first and last name.
def inquire(df):
    name = input('Enter name to search for: ')
    for index, row in df.iterrows():
        if name in row['StudentList']:
            print(row['StudentList'],row['Password'], row['Username'])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_student(studentname, username, password, url):
    #new_df = pd.DataFrame([[studentname, username,password,url]])
    new_row = [studentname, username, password, url]
    return(new_row)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def merge_dfs(df_1,new_row):
    #df = df_1.append(df_2)
    df_1.loc[len(df_1)] = new_row
    return(df_1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#StudentList,Username,Password,URL
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def remove_student(df,studentname):
    df = df[~df.StudentList.str.contains(str(studentname))]
    return(df)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    args = parse_args()
    input_file = args.input_file
    old_df = pd.read_csv(input_file, sep = ',') #read in the input file
    prompt = input('What would you like to do? 1. Inquire for student, 2. Add student, 3. Print entire dataframe, 4. Remove student from dataframe.  ')
    if prompt == '1':
        inquire(old_df)
    if prompt == '2':
        name = input('enter students name: ')
        username = input('enter their username: ')
        password = input('enter their password: ')
        site = input('enter the url of the gradebook: ')
        new_df = add_student(str(name),str(username),str(password),str(site)) #returns new_df to merge onto old_df
        df = merge_dfs(old_df,new_df) #merges both old_df and new_df
        df.to_csv('sylvan_gradebook.csv',mode = 'w', index=False) #FIXME looks really gross
        print(df) #show me that it did it.
    if prompt == '3':
        print(old_df) #just needs to show the df.
    if prompt == '4':
        student = input('Enter the name of the student to be removed: ')
        df = remove_student(old_df,student)
        df.to_csv('sylvan_gradebook.csv',mode = 'w', index=False) #FIXME looks really gross

if __name__ == "__main__":
    main()
