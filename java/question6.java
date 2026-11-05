// public class Main {
 
//   // Create a fullThrottle() method
//   public void fullThrottle() {
//     System.out.println("The car is going as fast as it can!");
//   }

//   // Create a speed() method and add a parameter
//   public void speed(int maxSpeed) {
//     System.out.println("Max speed is: " + maxSpeed);
//   }

//   // Inside main, call the methods on the myCar object
//   public static void main(String[] args) {
//     Main myCar = new Main();   // Create a myCar object
//     myCar.fullThrottle();      // Call the fullThrottle() method
//     myCar.speed(200);          // Call the speed() method
//   }
// }

public class question6{
    public void fullThrottle(){
        System.out.print("Car is going fast!");
    }
    public void speed(int maxSpeed){
        System.out.print("Max speed is " + maxSpeed);
    } 

    public static void main(String[] args){
        question6 myCar = new question6();
        myCar.fullThrottle();
        myCar.speed(100);
    }
}