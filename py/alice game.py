T = int(input())
for i in range(T):
    start = input().split(' ')
    alice=start[0]
    bob = start[1]
    times = int(start[2])
    dicwinn = {'Scissors':['Paper','Lizard'],'Paper':['Rock','Spock'],'Rock':['Scissors','Lizard'],'Lizard':['Spock','Paper'],
            'Spock':['Scissors','Rock']}
    dicloose = {'Scissors':['Rock','Spock'],'Paper':['Scissors','Lizard'],'Rock':['Paper','Spock'],'Lizard':['Scissors','Rock'],
            'Spock':['Paper','Lizard']}
    win=""
    bobwin=0
    alicewin=0
    ties=0
    falice=alice
    fbob=bob
    count=0
    
    while(times!=0):
        if(bob in dicwin[alice]):
            if(bob=='Spock'):
                bob='Paper'
            else:
                bob='Spock'
            win = 'alice'
            alicewin=alicewin+1

            
        elif(alice in dicwin[bob]):
            b_arr = dicl[bob]
            if(b_arr[0] in dicwin[b_arr[1]]):
                alice=b_arr[1]
            elif(b_arr[1] in dicwin[b_arr[0]]):
                alice=b_arr[0]
                
            if(bob=='Spock'):
                bob = 'Rock'
            else:
                bob='Spock'
            win='bob'
            bobwin=bobwin+1

            
        else:
            b_arr = dicloose[alice]
            if(b_arr[0] in dicwin[b_arr[1]]):
                alice=b_arr[1]
            elif(b_arr[1] in dicwin[b_arr[0]]):
                alice=b_arr[0]
            if(bob=='Spock'):
                bob='Lizard'
            else:
                bob='Spock'
            win = 'tie'
            ties=ties+1
        times = times - 1
        count = count +1
        

    if(alicewin > bobwin):
        print('Alice'+' wins, by winning '+str(alicewin) +' game(s) and tying '+str(ties)+' game(s)')
    elif(alicewin<bobwin):
        print('Bob'+' wins, by winning '+str(bobwin) +' game(s) and tying '+str(ties)+' game(s)')
    else:
        print('Alice and Bob tie, each winning '+str(bobwin)+' game(s) and tying '+str(ties)+' game(s)')
