from abc import abc, abstractmethod
 
class computer(abc):
    
    def run(self,app):
        self.process(app)
        
    @abstractmethod
    def process(self,app):
        pass  
    
class mobile(computer):
    def process(self,app):
        print("mobile is running,",app)
        
class laptop("computer"):
     def process(self,app):
        print("laptop is running,",app)     
        
        
samsung=mobile()
samsung.run("pubg")