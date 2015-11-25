#philosophers problem
#Cat Felts
#W01032567
#Assignment 4

##P: (eating[i]&&eating[i+1%M])!= True;                                #no two philosophers who are sitting directly next to each other are eating at the same time at any given time
M = 5;
sem e = 1;
philoSems = [new Semaphore(0) for k in range 1 to M];               #array of philosophers
eating = [False for i in range 1 to M];
waiting = [False for j in range 1 to M];

procedure Philosopher[ i=0 to M-1]{
        while (true){
                think;
                acquire_forks(i);
                eat;
                release_forks(i);
        }
}

procedure acquire_forks(int i){
    P(e);                       #get the entry mutex
    waiting[i] = True;          #waiting to eat
    check(i);                   #check to see if you dont have to wait anymore
    V(e);                       #replace entry mutex
    P(philoSems[i])             #if check fails, blocks philosopher
}



void check(int i){
    if(eating[i+1%M] == False && eating[i-1%M] == False){      #if both of your neighbors are not eating
            if(waiting[i] == True){                            #and if you are waiting to eat
                    waiting[i] = False;                        #stop waiting
                    eating[i] = True;                          #start eating
                    V(philoSems[i])                            #releases philosopher if blocked
            }
    }
}

void release_forks(int i){
    P(e);                           #grab mutex
    eating[i] = false;                  #done eating
    check(i+1);                         #after I'm done eating, check to see if my neighbors are waiting to eat
    check(i-1);     
    V(e);                             #release mutex
}
                
