/**
Name :-  Kartikeya Deepak Kumbhar

Title:-  Implement a robust Java calculator program that captures user input 
		dynamically, processes mathematical operations using conditional logic 
		and looping constructs, and ensures efficient error handling.
*/

import java.util.Scanner;
import java.util.InputMismatchException;

public class calculator {
	
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int repeatchoice;

		do {
			double a = 0,b = 0;
			boolean z = false, x = false;
			try {
 	
	 while (!z) {
         try {
             System.out.print("Enter first number: ");
             a = sc.nextInt();
             z = true; 
         } catch (InputMismatchException e) {
             System.out.println("Invalid input. Please enter numbers only.");
             sc.nextLine();
         }
     }
		

		while (!x) {
	         try {
	             System.out.print("Enter second number: ");
	             b = sc.nextInt();
	             x = true; 
	         } catch (InputMismatchException e) {
	             System.out.println("Invalid input. Please enter numbers only.");
	             sc.nextLine();
	         }
		}
		System.out.println("calculator");
		System.out.println("1.add");
		System.out.println("2.sub");
		System.out.println("3.mul");
		System.out.println("4.div");
		System.out.println("5.modulus");
		
		System.out.println("enter your option: ");
		int option=sc.nextInt(); 
				double result;
		
		switch(option){
			case 1: result = a+b;
				System.out.println("result is: " + result);
				break;
			case 2: result = a-b;
				System.out.println("result is: " + result);
				break;
			case 3: result = a*b;
				System.out.println("result is: " + result);
				break;
			case 4: 
				result = a/b;
				System.out.println("result is: " + result);
        		break;
        		
			case 5: 
				result = a%b;				
				System.out.println("result is: " + result);
        		break;
			
        	default:
        		System.out.println("enter valid number");}
	}
		
	catch (InputMismatchException e) {
		System.out.println("Invalid input. Please enter number only");
		sc.nextLine();}
	catch (ArithmeticException e) {
		System.out.println("Cannot divide by zero");}
	
		System.out.println("Do you want to perform another operation?(yes=1 or no=0): ");
		repeatchoice =sc.nextInt();
			
		}
		while(repeatchoice==1);
			System.out.println("Computer closed");
	
		sc.close();
}
}