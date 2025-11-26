#include <iostream>
//#include <string>

/* README
*  Welcome to C++! 
*  Below you'll find the exercise function declarations (so they can be defined later). 
*  You'll also see the declaration for the C++ class Student. You'll get to define this late in exercise 5.
*  
*  Have a go at the exercises below the main file, and remember to call the functions in main (you'll see the comments).
*/

class Student;
void exercise1();
void exercise2();
void exercise3();
void exercise4();
void exercise5();

/* to save having to repeatedly refer to functions in the std library, uncomment the below */
using namespace std;

int main() {
    cout << "Welcome to your exercises in C++ !\n" << endl;

    //exercise1();
    exercise2();
    //exercise3();
    //exercise4();
    //exercise5();

    return 0;
}

/*
* Exercise 1: 
* Write C++ code that will ask the user to enter their name and age. 
* Store these values entered from the keyboard in variables and then output them to the screen.
* 
* If you've already written this in C, will it compile and run using C++ or do you have to make modifications?
*
* Remember types and semi-colons in C/C++! 
*/

void exercise1(){
    std::cout<< "\nExercise 1: I/O" << std::endl;

    char name[32];
    string name_; 
    int age; 

    cout << "Enter age: \n" << endl;
    cin >> age;
    cout << "Enter name: \n" << endl;
    cin >> name;

    cout << "Your name is " << name << endl;
    cout << "Your age is " << age << endl;
}


/*
* Exercise 2: 
* Now write a for loop in C++ that will repeat five times and print the value of the loop counter to the screen.
* 
* Print the values on the same line: 1,2,3,4,5
* Then also modify the loop so it prints each value on a new line: 
* 1
* 2
* 3
* 4 
* 5
*
*/

void exercise2(){
    std::cout<< "\nExercise 2: Iteration and formatting" << std::endl;

    for(int i = 1; i <=5; i++)
    {
        cout << i << " ";
    }

    int i = 1; 
    while(i < 6)
    {
        cout << i << " ";
        i++;
    }

}

/*
* Exercise 3: 
* Write a series of conditional statements that will output the lettergrade for a mark between 0 to 100.
* You may have already written this in Python (or C), so feel free to translate the code into C++!
* 
* Extension: Create a C++ function that will also convert lettergrades (e.g. 'A', 'B', 'C') 
* to University degree classifications (e.g. "1st", "2:1", "2:2"). Can you write a switch statement to do this?
* If you already have the switch function in C, will it run in C++ as it is or do you have to change it?
*/

void exercise3(){
    std::cout<< "\nExercise 3: Selection" << std::endl;
    int mark = 50;
    if (mark > 0 && mark < 40){
        cout << "Try again!" << endl;
    }
    else if (mark < 50)
    {
        cout << "Pass / D" << endl;
    }
    else
    {

    }

}


/* 
* Exercise 4: 
* 
* Define a C array which is fixed-size and can store 5 integers. 
* Assign the values 1 to 5, each to an indivdiual elememt of the integer array.
* Output the contents of the array to the screen.
* 
* Now write an array which allocate these same values to an array that allocates memory dynamically.
* Hint: use the keyword 'new'.
* 
* To visualise the dynamic memory allocation, print the memory addresses - use the & reference.
* Re-run the function and watch how the memory is allocated in different places each time.
*/

void exercise4(){
    std::cout<< "\nExercise 4: Arrays" << std::endl;

    //Write your solution here.  

}

/* Exercise 5
*  Further to the struct in C, C++ introduced classes which allow attributes 
*  to be encapsulated together with functions (now known as 'methods' in OOP terms).
*  
*  Complete the class definition of Student below. Then instantiate this class to create a student object. 
*  
*  Extension 1: Create objects via calling the constructor directly, and then using the 'new' keyword. 
*  (cont.)    : Print their memory locations and observe whether there are differences.
* 
*  Extension 2: Create an array that stores references (points to) dynamic instances (objects) of the Student class.
*  (cont.)    : Print the memory address for each object referred to by this array. Re-run this function and notice what happens to the memmory locations.
*/

class Student{
    private: 
        int id; 
        std::string name;

    public: 
        Student(){} //default constructor 
        Student(std::string name, int id){ //non-default constructor 
            this->name = name;
            this->id = id;
        }
        void print(){
            cout << "Name: " << name << endl;
            cout << "id: " << id << endl;
        }
};


void exercise5(){
    
    std::cout << "Exercise 5: Classes & Objects" <<std::endl;

    Student student("nick", 345678);
    student.print();

}
