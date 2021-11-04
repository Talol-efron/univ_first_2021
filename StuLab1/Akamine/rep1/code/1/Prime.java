public class Prime {
    public static void main(String[] args) {
        int x = 1;

        for (int i = 3; i < 1000 * 50; ++i) {
            int dividable = 0;
            for (int j = 2; j < i; ++j) {
                if (i % j == 0) {
                    dividable = 1;
                    break;
                }
            }

            if (dividable == 0) {
                x++;
            }
        }

        System.out.printf("The number of primes = %d \n", x);
    }
}
