Name= "Andrew Hawkins"
Script_Name = "Perfectly Competitive Market Rules of Engagement" 
Date= "5/02/2025"
Class_Name = "ECON202: Principles of Mircoeconomics" 
Teacher_Name = "Dr. Pelkowski" 

print("My Name is", Name) 
print ("My Script is", Script_Name) 
print("The Date is", Date) 
print("My class is", Class_Name) 
print("My teacher is", Teacher_Name) 
print("This script illustrates how an industry may enter or exit a perfectly competitive market") 
print("Let's begin.") 
print("Here is the following logic of my code.") 
print("If price is less than the Average Total Cost, it will exit.") 
print("If price is greater than the Average Total Cost, New Firms will enter and the existing firm will stay open.") 
print("An example of this is Culver's and Freddy's being a monopolistic competititive relationship.")
print("They are in a monopolistic market because they offer the same type of hamburgers.") 
print("However, they have differentiation with their fries. Freddy's offers shoe-string fries.")
print("Culver's, on the other hand, offers straight-style fries.") 
print("If price is equal to Average Total Cost, it will make zero economic profit.") 
print("If price is less than Average Variable Cost, it will shut down.") 
print("If price is equal to or greater than Average Variable Cost, it will remain open.") 
print("let's analyze this by doing a practice problem") 
P= 3.94
AVC= 2.10 
ATC = 3.94
print("let's suppose the price is", P, "dollars", "for farmer Joe that makes eggs") 
print("Let's suppose his Average Variable cost is", AVC,"dollars.")
print("The Average Total Cost is", ATC)
print("What is the if statement would we use?") 
print( "Price is", P)
print("AVC is", AVC)
print("ATC is", ATC) 

if P > AVC: 
    print("Since P (",P,")","is greater than Average Variable Cost (",AVC,")", "it will remain open temporarily.") 
else:
    print("it will shut down temporarily since P is less than AVC.") 
    
if P >= ATC: 
    print("Since P (",P,")","is greater than Average Total Cost (",ATC,")", "other firms will be entering the market.") 
else:
    print("Since P (",P,")","is less than Average Total Cost (",ATC,")", "it will exit in the Long Run since P is less than ATC.") 

if P == ATC: 
    print("Since P (",P,")","is equal to Average Total Cost (",ATC,")", "It is making zero economic profit.")
    print("Even if existing firm is making zero economic profit, It doesn't mean that the existing firm have zero accounting profit") 
else:
    print("See above.")