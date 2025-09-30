public class App {

    public static int fibonacci(int n) {

        if (n < 2) {
            return n;
        } else {
            return fibonacci(--n) + fibonacci(--n);
        }
        
    }

    public static int fibonacciLoop(int n) {
        int fibo = 1;
        int old_fibo = 1;
        int old_old_fibo;

        for (int i = 2; i < n; i++) {
            old_old_fibo = old_fibo;
            old_fibo = fibo;

            fibo = (old_old_fibo + old_fibo);
        }
        return fibo;
    }
    
    public static void main(String[] args) throws Exception {
        int fiboOutput;

        fiboOutput = App.fibonacciLoop(11);
        System.out.println(fiboOutput);

        // int count;

        // count = 0;
        // do {
        //     System.out.println(++count);
            
        // } while (count < 5);
        
        // count = 0;
        // while (true) {
        //     System.out.println(++count);

        //     if (!(count < 5)) {
        //         break;
        //     };
        // }
        
    }
}
