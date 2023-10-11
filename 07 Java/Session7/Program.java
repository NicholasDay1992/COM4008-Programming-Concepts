/**
 * Welecome to Java
 * The static main method in this class is where the application starts.
 * A comment above the class like this would be a class comment. 
 * Also see the '@' tags below for JavaDoc attributes. Feel free to update these with your details. 
 * 
 * @author Nick Day
 * @version 1.0 
 */

public class Program {

    public static void main(String[] args){
        System.out.println("Welcome to Java!"); //PS. you don't have to manually write 'x:' - this is added by VSC.
        exercise1();
        //exercise2();
        //exercise3();
        //exercise4(); 

        //Write your solution to exercise 5 here. 
    }

    /**
     * Exercise 1: 
     * Capture the user's name and age from the keyboard. 
     * Store these inputs in appropriate variables and then output them to the screen. 
     * Input in Java is not as straight forward as it is in other languages... 
     * You'll need to create an object of the Scanner class and call it's methods to capture data entered via the keyboard.
     */

    public static void exercise1(){
        System.out.println("Exercise 1: I/O in Java");
        //Write your solution here.

    }

    /**
     * Exercise 2: 
     * Now write a for loop in Java that will repeat five times and print the value of the loop counter to the screen.
     * 
     * Print the values on the same line: 1,2,3,4,5
     * Then also modify the loop so it prints each value on a new line: 
     * 1
     * 2
     * 3
     * 4
     * 5
     * 
     * Question: Is the for loop structure identical across C, C++, C# and Java? Do you spot any differences?
     * 
     */


    public static void exercise2(){
        System.out.println("Exercise 2: Iteration");
        //Write your solution here.
    }

    /**
     * Exercise 3: 
     * Ask the user to enter a mark from the keyboard (another opportunity to use the Scanner).
     * Write a series of conditional statements that will output the lettergrade for a mark between 0 to 100.
     * 
     * If you have attempted this exercise in one of the other languages, you should be able to reuse the conditional structure. 
     * 
     * Extension: Now create a Java function that will also convert lettergrades (e.g. 'A', 'B', 'C')
     * to University degree classifications (e.g. "1st", "2:1", "2:2").
     * Can you write a switch statement to do this? 
     * 
     * Hint: if you are passing and returning values to and from a static function, 
     * remember that Java differentiates between char data ' ' and string data " ".
     * 
     * Extension: If the above was easy for you, add in some user validation to process the user input. 
     * Safely handle any non-digits that might be typed in (exception handling). 
     * You may also need to add a type of loop to prevent the program from continuing until the right input is made.
     * 
     */

    public static void exercise3(){
        System.out.println("Exercise 3: Selection");
        //Write your solution here.

    }


    /**
     * Exercise 4: 
     * Define an array which is fixed-size and can store 5 integers. 
     * Assign the values 1 to 5, each to an indivdiual elememt of the integer array.
     * Output the contents of the array to the screen.
     * 
     * Extension 1: Now import the ArrayList class and create an ArrayList of 'Integers'. 
     * 'Integer' is a 'wrapper class' for the primitive type 'int' in Java.
     * 
     * Extension 2: Create a function that can print the contents of an ArrayList. 
     * Question: are values passed by value or reference in Java?
     * 
     * Extension 3: Instantiate another Collecion classe (e.g. HashMap, LinkedList, Set).
     * Populate the collection and print the contents to the screen. 
     * Question: What similarities do notice between the Collection classes?
     * 
     */

    public static void exercise4(){
        System.out.println("Exercise 4: Arrays and ArrayLists");
        //Write your solution here.

    }

    /**
     * Exercise 5
     * Create a Student class in a separate .java file (Student.java) within the same folder as this Program.cs file.
     * When creating a new .java file remember that the namespace name should reflect the folder name that the .java file resides in.
     * Specify private attributes for student's id and name in the Student class. Assign these via the non-default constructor. 
     * Also specify a Print method that will print the data stored in all attributes of a student object.
     * Instantiate an object of this class in the Main method above.
     * 
     * Extension 1: Create an ArrayList of Student objects. 
     * Add at least three student objects to the ArrayList and then print their details using a for each loop. 
     * 
     * 
     */

}
