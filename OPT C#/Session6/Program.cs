using System;

namespace Session6 //namespace should reflect the folder name
{
    /// <summary>
    /// The static Main method in this class is where the application starts.
    /// Please follow the instructions listed above the static methods underneath this Main method.
    /// 
    /// This template C# project file authored by Nick Day
    /// </summary>
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Welcome to C#");
            Exercise1();
            //Exercise2();
            //Exercise3();
            //Exercise4();
            
            //Write your solution for Exercise 5 here (see instructions below Exercise4() method definition)

        }

        /// <summary>
        /// Exercise 1: 
        /// Capture the user's name and age from keyboard, store them in variables and then output them to the screen.
        /// Hint: Remember that you will need to undergo a 'conversion' process from one type to another in C#...
        /// Extension: What is the effect of converting to a 16 bit integer or a 64 integer? 
        /// </summary>
        public static void Exercise1()
        {
            Console.WriteLine("Exercise 1: I/O and types:");
            
            // Write your solution here.

        }

        /// <summary>
        /// Exercise 2: 
        /// Now write a for loop in C# that will repeat five times and print the value of the loop counter to the screen.
        /// Print the values on the same line: 1,2,3,4,5
        /// Then also modify the loop so it prints each value on a new line: 
        /// 1
        /// 2
        /// 3
        /// 4 
        /// 5
        /// 
        /// Question: So is the for loop structure identical across C, C++ and C#? Are there any differences?
        /// </summary>

        public static void Exercise2()
        {
            Console.WriteLine("\nExercise 2: Iteration and formatting");
            
            //Write your solution here.
        }

        /// <summary>
        /// Exercise 3: 
        /// Write a series of conditional statements that will output the lettergrade for a mark between 0 to 100.
        /// You may have already written this in Python (or C/C++), so feel free to translate the code into C#!
        /// 
        /// Extension: Create a C# function that will also convert lettergrades (e.g. 'A', 'B', 'C') 
        /// to University degree classifications (e.g. "1st", "2:1", "2:2"). 
        /// Can you write a switch statement to do this?
        /// 
        /// Hint: if you are passing and returning values to a static function, remember that C# treats char data ' ' differently to string data " " 
        /// 
        /// Extension: If the above was easy for you, add in some user validation to prevent non digits being entered as the value for 'mark'.
        /// 
        /// </summary>

        public static void Exercise3()
        {
            Console.WriteLine("\nExercise 3: Selection and static functions");
            
            //Write your solution here. 

        }

 

        /// <summary>
        /// Define a C# array which is fixed-size and can store 5 integers. 
        /// Assign the values 1 to 5, each to an indivdiual elememt of the integer array.
        /// Output the contents of the array to the screen.
        /// 
        /// Question: Are there any differences between the C++ array and the C# array of integers?
        /// 
        /// Extension 1: Why not write one function that can output all the values of any array passed in.
        /// Remember to pass in a reference to the array itself (reference of the first value), and also the size of the array (how many elements).
        /// 
        /// Extension 2: Is there an Array Class? How does this differ to the array of primitive type integers?
        /// If you declare an array of 'Objects', you can use a for each loop to print out the values. Similar to Python's for... in ... 

        /// </summary>
        public static void Exercise4()
        {
            Console.WriteLine("\nExercise 4: Arrays in C#");
            
            //Write your solution here.

        }

        /// <summary>
        /// Exercise 5
        /// Create a Student class in a separate .cs file (Student.cs) within the same folder as this Program.cs file.
        /// When creating a new .cs file remember that the namespace name should reflect the folder name that the .cs file resides in.
        /// 
        /// Specify private attributes for student's id and name in the Student class. 
        /// Assign these via the non-default constructor. 
        /// Also specify a Print method that will print the data stored in all attributes of a student object.
        /// Instantiate an object of this class in the Main method above.
        /// 
        /// Extension: To illustrate the namespace feature of C#, create a duplicate Student class in a different namespace (different folder). 
        /// Check that you can create a new object of this duplicate class from this other namespace. 
        /// Remember to include a 'using' reference to this duplicate class in another folder. 
        /// 
        /// </summary>

        
    }


}