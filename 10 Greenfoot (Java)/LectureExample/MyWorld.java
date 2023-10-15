import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{

    /**
     * Create a new world with 24 x 20 cells
     * with a cell size of 30 x 30 pixels.
     */
    public MyWorld()
    {    
        super(24, 20, 30); 
        prepare();
    }
    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add 
     * them to the world.
     */
    private void prepare()
    {
        Animal animal = new Animal();
        addObject(animal,4,8);
        Animal animal2 = new Animal();
        addObject(animal2,10,12);
        Animal animal3 = new Animal();
        addObject(animal3,15,4);
    }
}
