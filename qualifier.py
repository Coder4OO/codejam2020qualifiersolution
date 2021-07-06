#TABLE WRITER - CODER400
import math

#DEFINE TABLE CHARACTERS FOR BORDERS
HORI_LINE = "─"
VERT_LINE = "|"

TOP_LEFT = "┌"
TOP_RIGHT = "┐"
TOP_CONNECTOR = "┬"

BOTTOM_LEFT = "└"
BOTTOM_RIGHT = "┘"
BOTTOM_CONNECTOR = "┴"

LEFT_CONNECTOR = "├"
TITLE_CONNECTOR = "┼"
RIGHT_CONNECTOR = "┤"

def clean_rows(rows):
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            rows[y][x] = " "+str(rows[y][x])+" "
    return rows

def clean_labels(labels):
    for x in range(len(labels)):
        labels[x] = " "+labels[x]+" "
    return labels

def get_highest_length_in_rows(rows):
    #initialise highest with smallest number possible
    highest = math.inf*-1
    # go through each row in labels
    for row in rows:
        # go through each string in row
        for string in row:
            # if length of string is greater than highest
            if len(string) > highest:
                # set highest to new highest length
                highest = len(string)
    #return the highest length
    return highest

def get_highest_length_in_labels(labels):
    #if labels is None, return 0
    if labels == None:
        return 0
    #initialise highest with smallest number possible
    highest = math.inf*-1
    # go through each value in labels
    for value in labels:
        # if length of string is greater than highest
        if len(value) > highest:
            # set highest to new highest length
            highest = len(value)
    #return the highest length
    return highest


#function for writing line to table.
def write_line_with_newline(table, line, maxlength, start=True):
    if start:
        table += VERT_LINE + line + " " * (maxlength-len(line)) + VERT_LINE + "\n"
    else:
        table += line + " " * (maxlength-len(line)) + VERT_LINE + "\n"
    return table

def write_centered_line_with_newline(table, line, maxlength, start=True):
    l1 = maxlength+1
    midpos = int(math.floor(l1/2))
    #create variable which store the length of the text
    textsize = len(line)
    #create variable which stores the text.
    #calculate our gap between string and border
    gap = int(midpos-math.floor(textsize/2))
    #if it is odd, reduce the final gap by one
    if textsize % 2 == 1:
        if start:
            table += VERT_LINE + " "*gap + line + " "*(gap-1) + VERT_LINE + "\n"
        else:
            table += " "*gap + line + " "*(gap-1) + VERT_LINE + "\n"
    else:
        #else keep it the same.
        if start:
            table += VERT_LINE + " "*gap + line + " "*gap + VERT_LINE + "\n"
        else:
            table += " "*gap + line + " "*gap + VERT_LINE + "\n"
    return table

#function for writing line to table.
def write_line_no_newline(table, line, maxlength, start=True):
    if start:
        table += VERT_LINE + line + " " * (maxlength-len(line)) + VERT_LINE
    else:
        table += line + " " * (maxlength-len(line)) + VERT_LINE
    return table

def write_centered_line_no_newline(table, line, maxlength, start=True):
    l1 = maxlength+1
    midpos = int(math.floor(l1/2))
    #create variable which store the length of the text
    textsize = len(line)
    #create variable which stores the text.
    #calculate our gap between string and border
    gap = int(midpos-math.floor(textsize/2))
    #if it is odd, reduce the final gap by one
    if textsize % 2 == 1:
        if start:
            table += VERT_LINE + " "*gap + line + " "*(gap-1) + VERT_LINE
        else:
            table += " "*gap + line + " "*(gap-1) + VERT_LINE
    else:
        #else keep it the same.
        if start:
            table += VERT_LINE + " "*gap + line + " "*gap + VERT_LINE
        else:
            table += " "*gap + line + " "*gap + VERT_LINE
    return table


def make_table(rows, labels=None, centered=False):
    #define table
    table = ""
    #initialise length of table
    length = 0
    #clean all data to make it strings
    rows = clean_rows(rows)
    labels = clean_labels(labels)
    #get maximum length of table
    l1 = get_highest_length_in_rows(rows)
    l2 = get_highest_length_in_labels(labels)
    #set the length to the greatest length out of l1 and l2
    if l1 > l2:
        length = l1
    else:
        length = l2
    #if there are no labels
    if l2 == 0 or labels == None:
        #create top line of the table.
        table += TOP_LEFT + HORI_LINE*length + TOP_RIGHT + "\n"
        # if text does not need to be centered
        if not centered:
            # loop through all values in rows
            for value in range(len(rows)):
                #format rows onto table
                table = write_line_with_newline(table, rows[value][0], length)
        else:
            for value in range(len(rows)):
                table = write_centered_line_with_newline(table, rows[value][0], length)
        #add bottom to our table.
        table += BOTTOM_LEFT + HORI_LINE*length + BOTTOM_RIGHT + "\n"
    else:
        #if there labels then...
        #create our top line
        nolabels = len(labels)
        #define our row gap
        rowgap = length*HORI_LINE
        table += TOP_LEFT
        #loop through number of labels minus one
        for i in range(nolabels-1):
            #add in space and then connector
            table += rowgap + TOP_CONNECTOR
        #finish our top with the right corner and new line escape char
        table += rowgap+TOP_RIGHT+"\n"
        #check if we need to center our text.
        if not centered:
            # loop through all labels
            for x in range(len(labels)):
                # if index is the last
                if x == len(labels)-1:
                    # write our line with a new line at the end, and skip the start character.
                    table = write_line_with_newline(table, labels[x], length, start=False)
                else:
                    #otherwise, check if x is greater than 0
                    if x > 0:
                        #if it is, write the line with no new line and skip the start character
                        table = write_line_no_newline(table, labels[x], length, start=False)
                    else:
                        #if x is 0, write the line with new line and with start character
                        table = write_line_no_newline(table, labels[x], length)
        else:
            #if we don't, loop through all labels.
            for x in range(len(labels)):
                if x == len(labels)-1:
                    table = write_centered_line_with_newline(table, labels[x], length, start=False)
                else:
                    if x > 0:
                        table = write_centered_line_no_newline(table, labels[x], length, start=False)
                    else:
                        table = write_centered_line_no_newline(table, labels[x], length)
        table += LEFT_CONNECTOR
        #loop through number of labels minus one
        for i in range(nolabels-1):
            #add in space and then connector
            table += rowgap + TITLE_CONNECTOR
        #finish our top with the right corner and new line escape char
        table += rowgap + RIGHT_CONNECTOR+"\n"
        #go through each row
        for y in range(len(rows)):
            #go through each label in rows
            for x in range(len(rows[y])):
                #if text needs to be centered
                if centered:
                    #if index equals length of labels minus 1
                    if x == len(rows[y])-1:
                        table = write_centered_line_with_newline(table, rows[y][x], length, start=False)
                    else:
                        #if it does not
                        if x > 0:
                            table = write_centered_line_no_newline(table, rows[y][x], length, start=False)
                        else:
                            table = write_centered_line_no_newline(table, rows[y][x], length)
                else:
                    #if index equals length of labels minus 1
                    if x == len(rows[y])-1:
                        table = write_line_with_newline(table, rows[y][x], length, start=False)
                    else:
                        #if it does not
                        if x > 0:
                            table = write_line_no_newline(table, rows[y][x], length, start=False)
                        else:
                            table = write_line_no_newline(table, rows[y][x], length)
        table += BOTTOM_LEFT
        #loop through number of labels minus one
        for i in range(nolabels-1):
            #add in space and then connector
            table += rowgap + BOTTOM_CONNECTOR
        #finish our top with the right corner and new line escape char
        table += rowgap + BOTTOM_RIGHT +"\n"
                
    return table