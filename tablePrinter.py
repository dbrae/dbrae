#! python3
#printTable()
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)): # find the number of lists in tableData
        for j in range(len(tableData[i])): # find the longest string in each list of tableData
            if colWidths[i] < len(tableData[i][j]): # if the length of the current string is greater than the current value of colWidths[i]
                colWidths[i] = len(tableData[i][j]) # set the value of colWidths[i] to the length of the current string
    for i in range(len(tableData[0])):  # find the number of strings in each list of tableData
        for j in range(len(tableData)): # find the number of lists in tableData
            print(tableData[j][i].rjust(colWidths[j]), end=' ') # rjust() method of string right-justifies the string in a field of a given width by padding it with spaces on the left
        print()

printTable(tableData)