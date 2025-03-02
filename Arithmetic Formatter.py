def arithmetic_arranger(problems, show_answers=False):
    top = []
    bottom = []
    line = []
    solution = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for item in problems:
        problem = item.split()
        align = max(len(problem[0]),len(problem[2])) + 2
        
        if problem[1] != '+' and problem[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not (problem[0].isdigit() and problem[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if not (len(problem[0]) and len(problem[2]) <= 4):
            return "Error: Numbers cannot be more than four digits."
        
        calculation = str(eval(item))
        top.append(problem[0].rjust(align))
        bottom.append(problem[1] + " " + problem[2].rjust(align-2))
        line.append('-'*align)
        solution.append(calculation.rjust(align))
    
    print(top)
    print(bottom)
    print(line)
    print(solution)
    result = ""

    if top: 
        result += '    '.join(top) + '\n'
    if bottom:
        result += '    '.join(bottom) + '\n'
    if line and show_answers == True:
        result += '    '.join(line) + '\n'
    else:
        result += '    '.join(line)
    if show_answers:
        result += '    '.join(solution)

    return result

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')