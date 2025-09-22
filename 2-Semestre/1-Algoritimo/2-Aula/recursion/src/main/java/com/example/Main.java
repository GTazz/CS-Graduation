package com.example;

public class Main {

    public static int selfMultiplierAndSum(int n) {
        return selfMultiplierAndSum(n, 0); // Calls the overloaded method with a default value
    }

    public static int selfMultiplierAndSum(int n, int sum) {
        if (n > 0) {
            System.out.println(n + "x" + n + " = " + n * n);
            return selfMultiplierAndSum(n - 1, sum + n * n);
        } else {
            System.out.println("Soma das multiplicações: " + sum);
            return sum;
        }
    };

    public static float sqrtAndSum(int n) {
        return sqrtAndSum(n, 0); // Calls the overloaded method with a default value
    }

    public static float sqrtAndSum(int n, float sum) {
        if (n > 0) {
            System.out.println("Sqrt(" + n + ") = " + Math.sqrt(n));
            return sqrtAndSum(n - 1, sum + (float) Math.sqrt(n));
        } else {
            System.out.println("Soma das raízes: " + sum);
            return sum;
        }
    }

    public static void countRange(int start, int end) {
        if (start < end) {
            System.out.println(start);
            countRange(start + 1, end);
        } else if (start > end) {
            System.out.println(start);
            countRange(start - 1, end);
        } else {
            System.out.println(end);
            System.out.println("Contagem finalizada.");
        }
    }

    public static boolean isPrime(int n) {
        if (n > 1) {
            for (int i = 2; i < n; i++) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        } else {
            return false;
        }
    }

    public static void primeNumbersUpTo(int n) {
        if (n > 1) {
            if (isPrime(n)) {
                System.out.println(n);
            }
            primeNumbersUpTo(n - 1);
        }
    }

    public static void main(String[] args) {
        int sumMultiplier;
        float sumSqrt;

        System.out.println();
        sumMultiplier = Main.selfMultiplierAndSum(10);
        System.out.println();

        System.out.println();
        sumSqrt = Main.sqrtAndSum(50);
        System.out.println();

        System.out.println();
        Main.countRange(0, 10);
        System.out.println();
        
        System.out.println("Números primos:");
        Main.primeNumbersUpTo(50);
        System.out.println();
    }
}