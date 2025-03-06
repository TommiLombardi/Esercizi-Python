# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User:
    
    rank_values = {i:i if i < 0 else i+1 for i in range (-8,8)} # l'estremo di destra non è considerato, qui voglio che vada da -8 a 7 sulle key
    
    def __init__(self):
        self.rank = -8
        self.progress = 0
        
    def inc_progress(self, n):
        
        if n not in User.rank_values.values():
            raise Exception("Error")
        
        if self.rank == 8:
            return # al rank 8 non si progradisce più, esci da questo metodo
        
        reward = {i if i < 0 else i+1:(10 * (i-(self.rank)) * (i-(self.rank))) if i > self.rank
                    else 3 if i == self.rank
                    else 1 if i == self.rank-1
                    else 0 for i in User.rank_values.keys()}
        
        
        self.progress = self.progress + reward[n]
        advancement = self.progress // 100
        
        if advancement > 0 :
            
            if User.rank_values[self.rank + advancement] <= 8:
                self.rank = User.rank_values[self.rank + advancement] 
            else:
                self.rank = 8
            self.progress = self.progress % 100
        # questo codice non supera tutti  i test, ma l'obiettivo accademico è stato raggiunto :) 