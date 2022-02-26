# *************** HOMEWORK 3 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE
def verify_row(row, constraint):
    """
    checks if the number of Trues are correct in the row and that they all appear together -> no False separating them

    :param row: row from the board (list[bool])
    :param constraint: how many Trues need to be in the row and together (int)
    :return: True if the condition is applied to the row (bool)
    """
    count_true = 0  # number of True in the sentence

    for square in row:
        if square is True:
            if count_true < constraint:
                count_true += 1
            else:  # more True than required
                return False
        elif count_true < constraint and count_true != 0:  # if the sequence isn't complete then the brad is not correct
            return False

    return True


def change_columns_to_list(board):
    """
    gets a board and flips it so that the original rows are now the flipped boards columns
    and the original columns are now the flipped boards rows.

    :param board: the original board (list[list[bool]])
    :return: flipped board (list[list[bool]])
    """
    columns_as_list = []  # keeps the values that will be the new row

    for row in range(len(board)):
        cur_column = []  # column in broad that is being changed
        for square in range(len(board[row])):
            cur_column.append(board[square][row])
            if square == len(board[row]) - 1:  # adds the column to the new board when reaching the end of the column
                columns_as_list.append(cur_column)

    return columns_as_list  # new board with column as rows


def verify_nonogram_board(board, rows_constraints, columns_constraints):
    """
    checks if the board is filled according to the conditions -> number of Trues are aligned at the same
    length as stated in the constraints

    :param board: board to be checked (list[list[bool]])
    :param rows_constraints: how many trues must appear together in a row. fist value= first row.. (list[int])
    :param columns_constraints: how many trues must appear together in a column. fist value= first column.. (list[int])
    :return: if the board is correct -> True, if noe -> False. (bool)
    """

    """ checking end-point conditions"""
    if not board and not rows_constraints and not columns_constraints:
        return True  # empty board, empty constraints (empty list)

    if len(board) == 1 and not rows_constraints and not columns_constraints and len(board[0]) == 0:
        return False  # empty board, empty constraints (row constraint length is not 1)

    if len(board) == 1 and rows_constraints[0] == 0 and not columns_constraints and len(board[0]) == 0:
        return True  # empty board, empty constraints (empty list in empty list)

    if len(board) >= 1 and (not rows_constraints and not columns_constraints):  # board with no conditions
        return False

    """ checking the rows"""
    for row in range(len(board)):  # checks if rows are correct
        if verify_row(board[row], rows_constraints[row]) is False:
            return False
        row += 1

    """ if the rows are correct, then checking the columns"""
    if len(board) != 1:  # if the board is not only one row
        new_board = change_columns_to_list(board)  # flips board

    else:  # if the board is only one row
        new_board = []
        for column in range(len(board[0])):
            temp_vale_as_list = [board[0][column]]
            new_board.append(temp_vale_as_list)

    for column in range(len(new_board)):  # checks if columns are correct
        if verify_row(new_board[column], columns_constraints[column]) is False:
            return False
        column += 1

    return True  # if everything is correct then the function will return True.


# ************************ QUESTION 2a **************************
### WRITE CODE HERE
def get_all_capital_letters(text):
    """
    gets a text and returns a list of all the capital lettres in the order they appear

    :param text: the text needed to be checked (string)
    :return: all the capital letters (list[string])
    """
    temp_text = list(text)  # converts the string to a list
    capital_list = []  # new list of only capital letters

    for letter in temp_text:  # checks if the letter is a capital one and adds to the new list
        if 65 <= ord(letter) <= 90:
            capital_list.append(letter)

    return capital_list


# ************************ QUESTION 2b **************************
### WRITE CODE HERE
def split_text_to_tokens(text):
    """
    cleans text from characters that are not letters in the alphabet

    :param text: the text needed to be cleaned (string)
    :return: list of clean word from the text (list[string])
    """
    temp_text = text.split()  # splits words in text to values in a list
    clean_list = []  # list of clean words

    for word in temp_text:
        new_word = ""  # clean word to add the clean list
        for char in range(len(word)):
            if 65 <= ord(word[char]) <= 90 or 97 <= ord(word[char]) <= 122:  # checks if the char is a letter
                new_word += word[char]
            if char == len(word) - 1 and new_word != "":  # no letters in the clean word -> its not a word
                clean_list.append(new_word)

    return clean_list


# ************************ QUESTION 2c **************************
### WRITE CODE HERE
def grade_text_tone(text):
    """
    get a text and return the grade of tone based on the percentage of capital letters in the text.

    :param text: the text needed to be graded (string)
    :return: grade as a string with 4 digits after the decimal (string)
    """

    text = split_text_to_tokens(text)  # splits text to a list of clean words
    grade_of_text = 0  # begging grading at 0

    for word in text:
        if len(get_all_capital_letters(word)) != 0:
            grade_of_word = len(get_all_capital_letters(word)) / len(word)
        else:
            grade_of_word = 0
        grade_of_text += grade_of_word

    if len(text) == 0:  # if there is no text
        return "0.0000"

    grade_of_text /= len(text)
    grade_of_text = f'{grade_of_text:.5f}'[:-1]
    return format(grade_of_text)  # returns a string with 4 digits after decimal


# ************************ QUESTION 3a **************************
### WRITE CODE HERE
def register_students_submissions(students_raw_submissions):
    """
    gets a list of students submissions and divides it into a dictionary:
    :key is the corrected form of the students name (both first and last name begin with a capital letter) (string)
    :value is the essay the student wrote (string)

    :param students_raw_submissions: list of students submission. each value in this format -> [full name | text] (list)
    :return: dictionary of student submissions (key = full name; value = text) (dict {string:string}))
    """
    dic_of_essays = {}  # new dictionary
    for student in students_raw_submissions:
        beginning_of_text = student.find("|")  # finds where the students name ends
        dic_of_essays.update({student[:beginning_of_text].title(): student[beginning_of_text + 1:]})

    return dic_of_essays


# ************************ QUESTION 3b **************************
### WRITE CODE HERE
def grade_students_submissions(students_submissions):
    """
    grades the submission:
    if the text has less words than 2 and more than 10, the grade will be "F".
    other submission will be grades according to the percentage of capital letters in the text

    :param students_submissions: dictionary of students submissions (key-> full name: value-> essay) (dict {str:str})
    :return: dictionary with students grades (key-> students full name: value-> grade) (dict {string:str})
    """
    grades = {}  # dictionary with students grades
    for submission in students_submissions.keys():
        clean_essay = split_text_to_tokens(students_submissions[submission])  # words that are only tokens dont count
        if 1 < len(clean_essay) < 11:  # checks the length -> 2-10
            grades.update({submission: grade_text_tone(students_submissions[submission])})
        else:
            grades.update({submission: "F"})

    return grades


# ************************ QUESTION 3c **************************
### WRITE CODE HERE
def calculate_tokens_frequencies(students_submissions):
    """
    gets a dictionary of students submissions returns a dictionary with how many times a word appears in all the essays.
    key -> the word in lover cas and without tokens (string)
    value -> number of times the word appears (int)

    :param students_submissions: dictionary of submissions (key-> full name : value-> submission) (dict{str:str})
    :return: dictionary with how many repetitions a word has
    (key-> word in lower case and no tokens : value-> number of repetitions) (dict {string:int}))
    """
    dic_words_repetitions = {}  # new dictionary that hold the amount of repetition

    for submission in students_submissions.values():  # goes over the submissions
        for word in submission.split():  # goes over each word in text
            word = split_text_to_tokens(word)  # cleans word
            if not word:  # if the words were only tokens
                break
            number_of_repetitions = dic_words_repetitions.get(word[0].lower(), 0)  # checks if word is in new dict
            dic_words_repetitions.update({word[0].lower(): number_of_repetitions + 1})  # updates count in dict

    return dic_words_repetitions
