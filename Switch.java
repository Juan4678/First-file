public class Switch 

{ 

	public static void main(String[] args)
	{

		int n=6;    // String n=6 (puedes también usar un valor char o también string)

		switch(n)
		{
		case 1:
			System.out.println("One");
			break;
		case 2:
			System.out.println("Two");
			break;
		case 3:
			System.out.println("Three");
			break;
		case 4:
			System.out.println("Four");
			break;
		case 5: 
			System.out.println("Five");
			break;
		default:
			System.out.println("No match");
		}

	}
}
