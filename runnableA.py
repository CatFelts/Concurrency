import time
import threading

M = 5
e = threading.Semaphore(1)
philoSems = [threading.Semaphore(0) for i in range (0, M)]            #used to delay philosophers
eating = [False for i in range (0, M)]
waiting = [False for i in range (0, M)]


class Philosopher (threading.Thread):
    def __init__(self, index):
        super(Philosopher, self).__init__()
        self.index = index
        threading.Thread.__init__(self)
    
    def run(self):
        while(True):
            self.think()
        
            self.acquire_forks()
            self.eat()
        
            self.release_forks()
            print("Philosopher "+str(self.index) +" done eating")

    def think(self):
        print("Thinking Philosopher: "+str(self.index))
        time.sleep(5)

    def eat(self):
        print("Eating Philosopher: "+str(self.index))
        time.sleep(10)

    def check(self, i):
        global eating
        global waiting
        global M
        global philoSems
        global e
        #print ("[self.index+1%5] -> "+str(self.index+1%5))
        #print ("\n5%5 = "+str(5%5))
        if(eating[(i+1)%M] == False and eating[(i-1)%M] == False):
            if(waiting[i] == True):
                assert eating[(i+1)%M] == False and eating[(i-1)%M] == False
                waiting[i] = False
                eating[i] = True
                philoSems[i].release()
            
                
                
        

    def acquire_forks(self):
        global e
        global philoSems
        global waiting
        e.acquire()                                         #P(e) grab mutex
        waiting[self.index] = True
        self.check(self.index)
        e.release()
        philoSems[self.index].acquire()
        
        
    def release_forks(self):
        global e
        global M
        e.acquire()
        eating[self.index] = False
        self.check((self.index +1)%M)           #once done eating, check to see if neighbors can eat
        self.check((self.index-1)%M)
        e.release()


def PhilosophersDine():
    global M
    philosophers = [Philosopher(i) for i in range (0, M)]
    for p in philosophers:
        p.start()

PhilosophersDine()
    
       
       

  
