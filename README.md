# Ex1

*offline elevators algorithm*


**Literature Survey**

https://web.eecs.umich.edu/~baveja/RLMasses/node2.html

The Elevator Problem

https://www.researchgate.net/publication/31597314_Multiobjective_Optimization_in_Elevator_Group_Control

MULTIOBJECTIVE OPTIMIZATION IN ELEVATOR GROUP
CONTROL

https://www.javastructures.com/design/elevator

**The problen space**

We have a building that contains elevators and a list of calls.
The main target is to allocate an elevator to each call such that the time that passes from the arriving time to the time that the call went to its destination is the minimum time. 
In the first assignment we designed an online algorithm to solve the problem. This time we design an offline algorithm.
to do this we create classes for our most important elements in the program:
Building,Call and Elevator.
Each one has different attributes. the main function of the algorithm is combine all the attributes and also combine the Auxiliary functions.

**The algorithm**

At first we tried to think about comlex algorithm that works on the offline elevator algorithm that we structured in ex.0(attached below) but during the work on this assignment we discovered that it may be complicated because the simulator does not work as planned.
The offline algorithm from ex0:

The idea is based on the Pick-up elevator. We get all the calls and then find the optimal path for every elevator and take all the calls in a range of time at the same action.

Our algorithm works basically on the time and of the directions of the calls.
It checks the next call and decides if to allocate the same elevator or send another elevator to the next call,based on a few parameters such as call type,call destination and more. 
The choice of the specific elevator is based on random choice.
Also, if the distance between the source floor and the destination floor is bigger than half of the floors in the building then it is allocated to the fastest elevator in the building.




