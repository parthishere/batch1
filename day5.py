# functions

def addition(*args, **kwargs):
    # if (
    #     (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)) 
    #     ):
        
    #     return a + b
    answers = []
    for i in range(0, len(args)-1):
        print(args[i], end=" ")
        print(args[i+1])
        c = args[i] + args[i+1]
        answers.append(c)
        
    print(kwargs)

    return answers
    

 
def main():
    answers = addition(1.1, 5, 10, 1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10, 100, 11, val=200)
    print(answers)


if __name__ == "__main__":
    main()


