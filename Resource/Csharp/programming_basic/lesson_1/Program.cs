// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");

using System;

class Program
{
    public static void Main()
    {
        // double myDouble = 3.141595555555555555555555555555555D;
        // float myFloat = (float)myDouble;
        float myFloat = 3.141595555555555555555555555555555f;
        double myDouble = (double) myFloat;
        // Console.WriteLine(myFloat);
        // Console.WriteLine(myDouble);
        Console.WriteLine($"{myFloat:F16}");
        Console.WriteLine($"{myDouble:F16}");


    }
}