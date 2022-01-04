import requests, pprint



class partners:
    def __init__(self, firstName = None, lastName = None, availableDates = None, email = None, country = None):
        self.firstName = firstName
        self.lastName = lastName
        if availableDates is None:
            self.availableDates = []
        if email is None:
            self.email = []
        if self.country is None:
            self.country = []

#creating a dictionary in order to loop through and organize the data from API
    def from_dict(self, data):
        field = []
        for i in field in ['firstName', 'lastName', 'availableDates', 'email', 'country']:
            if field in data:
                setattr(self, field, data[field])



   
    def __repr__(self):
        return f'<partner>: {self.firstName}'

        
        
        
       
        
 
  #class Object to pass the data through and work with
class conference:
    pass

    @classmethod
    def show(cls):
        print('#!' * 40)
        print('#!' * 40)




    @classmethod
    def instructions(cls):
        print("""Welcome to Coding Conference 2021
        Type 'show" to see list of partners
        Type 'quit' to exit Conference Iterface""")

    @classmethod
    def add(cls, availableDates):
        
        if cls._list:
            for p in cls._list:
                if availableDates == p.availableDates:
                    input('Date already exists, try another')
            try:
        #connect to API
                print('Populating your Conference info..')
            r = requests.get(f'https: // ct-mock-tech-assessment.herokuapp.com /partners/{availableDates}')
            except:
            input("There was an error finding you COnference Info...Try gain")
        
        #add New Partner
        pass
        #create New Partner/Date
        p = partners()
        data_dict = {
           'firstName'r['firstName']:, 
           'lastName'r['lastName']:, 
           'availableDates':[a[""] for i in r['avaiableDates']], 
           'email'r['email']:, 
           'country'r['country']:, 
        }
        p.from_dict(data_dict)
        cls._list.append(p)
        
        
        


#runs the program
    def run(cls):
        done = False

        while not done:
        
            
            cls.instructions()

            conference_choice = input(" Type 'show' to see Partners and their info or type 'quit'")
            if conference_choice == 'quit':
                done = True
            elif conference_choice == 'show':
                cls.show()
                input("Press 'ENTER' to continue")
            else:
                #Send Partners API request

                # Put Partners in Conference Data Structure
                cls.add(conference_choice)
