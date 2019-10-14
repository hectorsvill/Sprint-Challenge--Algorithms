#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n) - linear time
    The algorithim has a liniear time complexity because the time increases in porportion to the input n.


b) 0(n^2) - quadratic time
    The algorithim needs to perfrom a linear opearation for each input value n so it has quadratic time complexity.

c) 0(n) - linear time
    The algorithims run time increases linearly with the size of 
    input n.

## Exercise II

<!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.     -->

 To find f. Start From the middle of the building and drop and egg. If it does not brake then set min flor f and recursively call the function to spit the number n in half, it it does brake set max floor and recursively  call the function to spit the number n in half. 

 0(n^2)