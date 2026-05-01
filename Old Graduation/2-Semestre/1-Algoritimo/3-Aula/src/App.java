public class App {

    public static int fibonacci(int n) {

        if (n < 2) {
            return n;
        } else {
            return fibonacci(--n) + fibonacci(--n);
        }
        
    }

    public static int fibonacciLoop(int n) {

        int previous = 1, current = 1;

        for (int i = 2; i < n; i++) {
            int next = previous + current;
            previous = current;
            current = next;
        }
        
        return current;
    }
    
    public static void main(String[] args) throws Exception {
        int fiboOutput;

        fiboOutput = App.fibonacciLoop(11);
        System.out.println(fiboOutput);

    //     int count;

    //     count = 0;
    //     do {
    //         System.out.println(++count);
            
    //     } while (count < 5);
        
    //     count = 0;
    //     while (true) {
    //         System.out.println(++count);

    //         if (!(count < 5)) break;
    //     }
        
    }
}
