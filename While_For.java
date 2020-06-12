public class While_For{            
	// loops: while, do while, for, for-each
	public static void main(String[] args){

//		System.out.println("Hello"); 
//		System.out.println("Hello"); 
//		System.out.println("Hello");  code written ency (repeat statements is a crime in virtual world)
//		System.out.println("Hello"); 
//		System.out.println("Hello"); 

		int i=1;         // counter
		while(i<=5)      //condition
		{
			System.out.println("Hello");
			i++;    //increment of the value
		}

		int i2=1;
		do                   // This loop first executes the block, then checks the condition, in case it is false the program will do the statement at least one time
		{
			System.out.println("Hello");
			i2++;

		}while(i2<=5);

		
		for (int i3=1;i3<=5;i3++) //puedes resumir todos los elementos en una línea
		{

			System.out.println("Hello");
		}


	}
}