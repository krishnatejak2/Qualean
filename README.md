# ReadMe.md

These are the functions implemented in this basic pyhon exercise

# Classes :

## Something 
    this class creates an instance which can have a variable "__something_new"  
## SomethingNew 
    this class creates an instance which can have the following variables :
        "__something"  
        "i"
    this variable "__something" is of type something class

# Functions :

## add_something 
    1. This function creates instances of both classes - Something & SomethingNew
    2. This function accepts 2 parameters 
       a. collection(type : List[Something])
       b. i(type : int)
    3. every time this function is called, the following happens:
       a. something variable ---> memory location of type Something()
       b. something.something_new variable --> memory location of type SomethingNew(i,something) --> memory location of something
       c. append something to the Collection list
    
    This function causes an explosion of memory which does not get collectedc by GC due to cyclical referenes being made by the add-something function

    By making the parent references to weakref, this issue is elimiated and memory is freed up effectively

## clear_memory 
    this clears the contents of the Collections List which frees up a lot of memory

## critical_function 
  * this function calls add_something fucntion for range(1,1024 * 128) = 131072-1 = 131071 times
  * which adds all the objects created to a list which has cyclical  references
  * this is  a fucntion which creates cyclical references - a lot of them!

## compare_strings_old 
    This function compares 2 large strings as is and tries to check if a particular word is in the string by storing it in a list

## compare_strings_new 
    This function compares 2 large strings with the help of python interning and tries to check if a particular word is in the string by storing the string as set instead of a list
    
## sleep 
    This function is not used for now in my code but this is mainly usewd to induce some custom delay into the execution

## char_list 
    char_list is a list/set for storing the string which is used for peeping
    In compare_strings_old function, this is set to a list type
    In compare_strings_new function, this is set to a set type

    By inherent advantages of sets over lists, the peeping functionality executes much faster in case of "compare_strings_new" than in "compare_strings_old"

## collection 
    This list contains all the instances of the objects being created in the ctitical function
    But when it is passed to clear_memory/critical_function it is used as a type of List[Someting], which can be used innterchagebly

## __init__
    We want to define the attributes of an instance right after its creation. __init__ is a method which is immediately and automatically called after an instance has been created. This name is fixed and it is not possible to chose another name. __init__ is one of the so-called magic methods,we will get to know it with some more details later. The __init__ method is used to initialize an instance. There is no explicit constructor or destructor method in Python, as they are known in C++ and Java. The __init__ method can be anywhere in a class definition, but it is usually the first method of a class, i.e. it follows right after the class header.