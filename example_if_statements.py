while True:
    print('which example do you want? (paper, computer, grade_average, days_since_purchase )')
    example_name = input()
    match example_name:
        case 'paper':     
    #paper count example
            print('How much paper do you have? (int only)')
            paper_count = int(input())

            if paper_count < 10:
                print('Get more paper!')
            else:
                print('Enough paper')
    #paper count end
            
        case 'computer':
    #computer age example
            print('How old is the computer? (int only)')
            computer_age = int(input())
        
            if computer_age >= 3:
                print('Buy new computer')
            else:
                print('Computer is ok')
    #computer age end
    
        case 'grade_average':
    #grade average example
            print('What is your grade average? (int only)')
            grade_average = int(input())
        
            if grade_average >= 90:
                print('Grade of A')
            else:
                print('Not an A')
    #grade example end
            
        case 'days_since_purchase':
    #days since return example
            print('How many days since item was purchased? (int only)')
            days_since_purchase = int(input())
        
            if days_since_purchase <= 90:
                print('return allowed')
            else:
                print('return forbidden')
    
        case _:
            print('unknown keyword')
    print('\n')