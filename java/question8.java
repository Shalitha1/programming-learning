// class Vehicle {
//     protected String brand = "Ford";

//     public void honk() {
//         System.out.println("Tuut tuut");
//     }
// }

// class Car extends Vehicle {
//     private String modelName = "Mustang";

//     public void displayDetails() {
//         System.out.println(brand + " " + modelName);
//     }
// }

// public class question8 {

//     public static void main(String[] args) {

//         Car myCar = new Car();

//         myCar.honk();
//         myCar.displayDetails();
//     }
// }

class Vehicle {
    protected String brand = "Ford";
    public void honk(){
        System.out.print("beep beep");
    }
}

class Car extends Vehicle {
    private String modelName = "Mustang";
    public void displayDetails(){
        System.out.println(brand + modelName);
    }
}

public class question8 {
    public static void main(String[] args){
        Car myCar = new Car();
        myCar.honk();
        myCar.displayDetails();
    }
}