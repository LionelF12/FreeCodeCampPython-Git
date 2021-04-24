problems = ["999 + 698", "3801 - 3900", "45 + 43", "1233 + 49","2 + 2"]

def arithmetic_arranger(problems,option=False):
    # test1 min 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # test2 reject * and / 
    for problem in problems:
        if problem.find('*') != -1 or problem.find('/') != -1:
            return 'Error: Operator must be \'+\' or \'-\'.'
        
    #test 3 & 4 - only 4 character digits
        problem = problem.split()
        try:
            int(problem[0])
            int(problem[2])
        except:
            return 'Error: Numbers must only contain digits.'

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
    #solution
    solution = ''

    #row1
    for problem in problems:
        item = problem.split()
        num1len = len(item[0])
        num2len = len(item[2])
        if num1len >= num2len:
            biglen = num1len
        else:
            biglen = num2len
        
        solution += (' '*(biglen - num1len + 2) + str(item[0]))
        solution += ' '*4
    
    solution.removesuffix(' '*4)
    #for older python without .removesuffix use 
    #   if solution.endswith (' '):
    #       solution = solution [:-4]
    solution += '\n'

    #row 2
    for problem in problems:
        item = problem.split()
        num1len = len(item[0])
        num2len = len(item[2])
        if num1len >= num2len:
            biglen = num1len
        else:
            biglen = num2len

        solution += item[1] + ' '*(biglen - num2len + 1) + item[2]
        solution += ' '*4
    solution.removesuffix(' '*4)
    solution += '\n'

    #row 3
    for problem in problems:
        item = problem.split()
        num1len = len(item[0])
        num2len = len(item[2])
        if num1len >= num2len:
            biglen = num1len
        else:
            biglen = num2len

        solution += '-'*(biglen + 2)
        solution += ' '*4
    
    solution.removesuffix(' '*4)
    #row 4 (answer)
    if option == True:
        solution += '\n'

        for problem in problems:
            item = problem.split()
            num1len = len(item[0])
            num2len = len(item[2])
            if num1len >= num2len:
                biglen = num1len
            else:
                biglen = num2len
            
            if item[1] == '-':
                answer = str(int(item[0]) - int(item[2]))
            else:
                answer = str(int(item[0]) + int(item[2]))

            solution += ' '*(biglen + 2 - len(answer)) + str(answer)
            solution += ' '*4 
        
        solution.removesuffix(' '*4)


    return solution
        


    


        
print(arithmetic_arranger(problems,True))