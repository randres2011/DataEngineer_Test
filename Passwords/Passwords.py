import pandas as pd

def reorderColumns(df, digit1, digit2, digit3):
    
    while (df.columns.get_loc(digit1) < df.columns.get_loc(digit2) < df.columns.get_loc(digit3)) == False:
        #If position of digit 1 is after digit2
        if df.columns.get_loc(digit1) > df.columns.get_loc(digit2):
            #If position of digit 1 is after digit3
            if df.columns.get_loc(digit1) > df.columns.get_loc(digit3):
                reorderColumn(df, digit1, df.columns.get_loc(digit2))
            #else
            else:
                reorderColumn(df, digit1, df.columns.get_loc(digit2)-1)
        #If position of digit 1 is after digit3 and after digit2
        elif df.columns.get_loc(digit1) > df.columns.get_loc(digit3):
            reorderColumn(df, digit3, df.columns.get_loc(digit2))
    return df

def reorderColumn(df, digit, position):
    if position < 0:
        position = 0
    elif position > df.shape[1]:
        position = df.shape[1]
    column = df.pop(digit)
    df.insert(position, digit, column)  

def main():
    #Read file
    pswd = pd.read_csv('keylog.txt', delimiter="\t", header=None)
    #Create empty dataframe
    column_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    df = pd.DataFrame(columns = column_names)
    for index, row in pswd.iterrows():
        #Get digits of the number
        digit1 = int((row[0]/100)%10)
        digit2 = int((row[0]/10)%10)
        digit3 = int(row[0]%10)
        #Reorder columns
        df = reorderColumns(df, digit1, digit2, digit3)
        #Create a row of dataframe
        dfRow = pd.DataFrame(columns = df.columns)
        dfRow.append(pd.Series(dtype='float64'), ignore_index=True)
        dfRow.loc[index, digit1] = digit1
        dfRow.loc[index, digit2] = digit2
        dfRow.loc[index, digit3] = digit3
        df = df.append(dfRow)
    #Export result
    df.to_excel("Result.xlsx")
    #Get password
    df = df.dropna(axis=1, how='all')  
    password = ''.join(df.columns.map(str))
    print("Password: ", password)

if __name__ == "__main__":
    main()


