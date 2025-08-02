#Arranging the numbers in line by line and doing arithmetic operations on them
def arithmetic_arranger(problems, display_answers=False):
    # here is the logics we used in the code
    if len(problems) > 5:
        return "Error : Too many problems"
    first_line=""
    second_line=""
    dash_line=""
    answer_line=""
    for i, problem  in enumerate(problems):
        parts = problem.split()

        if len(parts) != 3:
            return "Error : each problem should have two operands and one operator"

        left, operator, right=parts
        if operator not in ['+','-']:
            return "Error :Operator must be '+',or '-'"

        if not left.isdigit() or not right.isdigit(): #"isdigit" checks if the string contains only digits(0-9)
             return "Error : Numbers must only contain digits"

        if len(left)>4 or len(right)>4:
            return "Error : Number cannot be more than four digits"

        #now here we should arrange them in correct format
        width=max(len(left),len(right))+2
        top=left.rjust(width)
        #rjust(width) is a string method that right-aligns a string by adding spaces to the left
        bottom= operator + right.rjust(width-1) 
         
        line= "_" * width
        answer=""
        if display_answers:
            if operator== "+":
                result=str(int(left)+int(right))
            else :
                result=str(int(left)-int(right))
            answer=result.rjust(width)
#spacing
        spacing ="   " if i< len(problems)-1 else ""
        first_line+=top+spacing
        second_line+=bottom+spacing
        dash_line+=line+spacing
        if display_answers:
              answer_line+=answer+spacing
#arrangment 
    arranged_problems= first_line+"\n"+second_line+"\n"+dash_line
    if display_answers:
          arranged_problems+="\n"+answer_line 
    return arranged_problems


problems=["49 + 498","63 - 679"]

print(arithmetic_arranger(problems,True))

