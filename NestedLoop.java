/*

* * * * 
* * * *    (Lo que se quiere imprimir)
* * * *
* * * *


*/

// * * * * (primero una línea)
public class NestedLoop{
	public static void main(String[] args){

		for (int i=1;i<=4;i++)  //nested loop
		{
			for (int j=1;j<=4;j++)
			{
			System.out.print("* ");
			}
			System.out.println();
		}

		for (int i=1;i<=4;i++)  //nested loop
		{
			for (int j=1;j<=4;j++)
			{
			System.out.print(j + " ");
			}
			System.out.println();
		}
	}
}