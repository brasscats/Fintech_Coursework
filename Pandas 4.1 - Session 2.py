# Summary stats
NameOfVariable.describe()

#Re-order columns
#>>Crate a list of lists

#Save the DataFrame to the 'Resources' folder
Name_of_df.to_csv(./../New_File_name.csv")

                 
#Cleanse data by dropping duplicates
Name_of_df.drop_duplicates(subset=["Last"])

#Select the 1st, 3rc, 5th, 7th rows of the 2nd, 4th, and 6th columns.
Name_of_df.iloc([0,2,4], [1,3,5])

#Assign Values to Specific Rows and Columns Using Index Assignment with iLoc
# Modify the 'first_name' column value of the first row
Name_of_df



#Sort dataframe in ascending order
Name_of_df.sort_value("Column name", ascending=False)


##Concatenating Pandas DataFrames
#>>Concatentate data by columns using concat funtion and inner join

column_appended_data = pd.concat(Name_of_df, ____)



###


