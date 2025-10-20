public class App {
    public static int[] bubbleSort(int[] array) throws Exception {

        boolean flag = true;
        int present;
        int next;
        int count = 0;
        
        System.out.println();
        while (flag) {
            flag = false;
            for (int i = 0; i < array.length - 1; i++) {
                present = array[i];
                next = array[i + 1];
                if (present > next) {
                    array[i] = next;
                    array[i + 1] = present;
                }
                flag = true;
            }

            System.out.println(++count + "º Passada");
        };

        return array;
    };

    public static void main(String[] args) throws Exception {

        int[] v = { 5, 4, 3, 2, 1, 0 };

        int[] sorted_v = App.bubbleSort(v);

        System.out.print("\nsorted_v = { ");
        for (int num : sorted_v) {
            System.out.print(num + ", ");
        }
        System.out.print("\b\b }\n\n");
    }
}
