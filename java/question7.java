// public class Main {
//   int modelYear;
//   String modelName;

//   public Main(int year, String name) {
//     modelYear = year;
//     modelName = name;
//   }

//   public static void main(String[] args) {
//     Main myCar = new Main(1969, "Mustang");
//     System.out.println(myCar.modelYear + " " + myCar.modelName);
//   }
// }

public class question7{
    int modelYear;
    String modelName;

    public question7(int year, String name){
        modelName = name;
        modelYear = year;
    }
    public static void main(String[] args){
        question7 myCar = new question7(2020, "BMW");
        System.out.println("My car is " + myCar.modelName);
        System.out.println("My car year is " + myCar.modelYear);
    }
}