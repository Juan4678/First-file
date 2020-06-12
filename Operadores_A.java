
public class Operadores_A {

	/*
	*
	*
	*Arithmetic +,-,*,/,% <- este operador encuentra el reminder de un número (redondea)
	*Bitwise
	*Relational
	*Logical
	*
	*
	*/

	public static void main(String[] args)

	{
		int m = 6, n = 4;
		int r1= m+n;       //10
		int r2= m-n;	   //2
		int r3= m*n;       //24
		double r4= (double)m/n;       //1.5 (si se asigna r4 como int no tomará en cuenta la parte decimal, hay que poner el valor como double)

		int r5= m%n;

		System.out.println(r1);
		System.out.println(r2);
		System.out.println(r3);
		System.out.println(r4);
		System.out.println(r5);


	}


}