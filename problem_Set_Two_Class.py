#takes a prompt that produces an integer and if value that participant puts is higher than the high or lower than the low will tell user it is an invalid answer and ask the question again
#online help for function below: https://stackoverflow.com/questions/32553941/how-to-redo-an-input-if-user-enters-invalid-answer
def rangedinput(prompt, low, high):
    #starts at true
    while True:
        #where user gives a numbered input
        user_input = int(input(prompt))
        #if users number is in-between the low and high will return the input (basically stop from asking)
        if low <= user_input <= high:
            return user_input
        #prints invalid option if particiapnt puts in a number outside the valid input range, but will produce ValueError if anything other than int
        print('invalid option')    

#creates a personality profile class that takes a score of each personality trait, made it so that it takes input from user but I know I can just put the numbers for each attributes in directly when calling the class
class PersonalityProfile:
    def __init__(self, participantID = 0, Openness = 0, Conscientiousness = 0, Agreeableness = 0, Extraversion = 0, Neuroticism = 0):
        #asks user to enter participant ID, will produce an error if not an integer
        self.participantID = int(input("Enter your participantID: " ))
        #using the rangedinput function created above for the openness attribute askes participants to enter openness from 1-5 and then stores that value in self.Openness
        self.Openness = rangedinput("Enter your Openness from 1-5: ", 1, 5)
        #same is done in rest of attributes
        self.Conscientiousness = rangedinput("Enter your Conscientiousness from 1-5: ", 1, 5)
        self.Agreeableness = rangedinput("Enter your Agreeableness from 1-5: ", 1, 5)
        self.Extraversion = rangedinput("Enter your Extraversion from 1-5: ", 1, 5)
        self.Neuroticism = rangedinput("Enter your Neuroticism from 1-5: ", 1, 5)
    
    #thsi function first prints what the true and false are for and then if extraversion score is smaller tnan 3 will print true
    def is_introvert(self):
        print('introvert (True/False): ')
        #if smaller than 3 - print True to introversion
        if self.Extraversion < 3:
            print(True)
        else: #if larger than 3 print false
            print(False)
            
    #the function below prints each score of each trait and tells you what trait that score belongs to
    def whole_summary(self):
        print("Participant ID is: " + str(self.participantID))    #converted it to a string because can't combine a string and an integer
        print("Openness Score is: " + str(self.Openness))
        print("Conscientiousness Score is: " + str(self.Conscientiousness))
        print("Agreeableness Score is: " + str(self.Agreeableness))
        print("Extraversion Score is: " + str(self.Extraversion))
        print("Neuroticism Score is: " + str(self.Neuroticism))

#this function takes all the personality traits and puts them in a list and then compares each one to see if it is equal to the max of the list
#if it is then it prints what the trait is and whats the score
    def summary(self):
        #creates a list with all the personality traits
        personality_traits = [self.Openness, self.Conscientiousness, self.Agreeableness, self.Extraversion, self.Neuroticism]
        #all if statements because multiple traits can have the highest score and don't want to skip them
        if self.Openness == max(personality_traits): #for each trait if it is equal to the highest score in the list than it prints that it is the highest score and what score it is
            print('Your highest trait is Openness at a score of: ' + str(self.Openness))
        if self.Conscientiousness == max(personality_traits): #I do this for all traits
            print('Your highest trait is Conscientiousness at a score of: ' + str(self.Conscientiousness))
        if self.Agreeableness == max(personality_traits):
            print('Your highest trait is Agreeableness at a score of: ' + str(self.Agreeableness))
        if self.Extraversion == max(personality_traits):
            print('Your highest trait is Extraversion at a score of: ' + str(self.Extraversion))
        if self.Neuroticism == max(personality_traits):
            print('Your highest trait is Neuroticism at a score of: ' + str(self.Neuroticism))
        
#calls the class and stores the data of the users input into a variable called participant 01
participant1 = PersonalityProfile()

#gives me the highest score
participant1.summary()

#gives me a summary of the data for participant 1
participant1.whole_summary()

#tells me if participant is an introvert
participant1.is_introvert()