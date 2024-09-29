# Chapter 3: Conditional Execution

This chapter focuses on the concept of **conditional execution**, where a program decides which code to run based on certain conditions. The key topics covered include:

- **Boolean expressions**: Understanding expressions that evaluate to either `True` or `False`.
- **Comparison operators**: Using operators like `==`, `!=`, `>`, `<`, `>=`, and `<=` to compare values.
- **Logical operators**: Working with `and`, `or`, and `not` to combine multiple conditions.
- **Conditional statements**: Writing `if`, `elif`, and `else` blocks to control the flow of the program based on conditions.
- **Nested conditionals**: Structuring `if` statements inside other `if` statements to handle more complex logic.
- **Try/Except**: Capturing and handling errors during execution to prevent crashes in the program.

## Exercises Completed:

### 1. Salary Calculation with Overtime Pay
The program calculates the employee's gross salary. If the employee works more than 40 hours, they are paid 1.5 times the hourly rate for the additional hours.

**Input:**
- Hours worked
- Hourly rate

**Output:**
- Gross salary including overtime.

---

### 2. Salary Calculation with Error Handling
An improved version of the previous exercise. This version uses `try` and `except` to handle non-numeric input gracefully.

**Input:**
- Hours worked (must be a number)
- Hourly rate (must be a number)

**Output:**
- Gross salary or an error message if invalid input is entered.

---

### 3. Grade Calculator
A program that asks the user to enter a score between 0.0 and 1.0. Based on the score, it returns the grade according to the following scale:

- `>= 0.9`: Outstanding
- `>= 0.8`: Notable
- `>= 0.7`: Good
- `>= 0.6`: Sufficient
- `< 0.6`: Insufficient

The program also handles invalid input (non-numeric values or out-of-range scores).

**Input:**
- User score (between 0.0 and 1.0)

**Output:**
- Corresponding grade or error message.

---

## Key Learnings:
- **Boolean logic**: Understanding how to compare values and evaluate logical expressions.
- **Conditional logic**: Controlling the flow of the program using `if-elif-else` statements.
- **Error handling**: Using `try` and `except` blocks to handle user input errors and prevent program crashes.
- **Code structure**: Writing clean, organized, and readable conditional code, avoiding deeply nested conditionals when possible.

---

## How to Run the Code
1. Clone the repository:  
   `git clone https://github.com/yourusername/Python_for_Everybody.git`

2. Navigate to the Chapter 3 directory:  
   `cd Python_for_Everybody/python_solutions_en/chapter_3/`

3. Run the exercises using Python:  
   `python3 salary_overtime.py`  
   `python3 salary_with_error_handling.py`  
   `python3 grade_calculator.py`

---

Feel free to contribute by submitting a pull request or opening an issue if you find any bugs or have suggestions for improvements.

---

### Resources:
- [Python for Everybody Textbook](https://www.py4e.com/book.php)
- [Official Python Documentation](https://docs.python.org/3/)

