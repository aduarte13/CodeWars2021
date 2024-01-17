/*
Write a program to calculate the volume of a
pizza given its height and radius on a single line.
Round to nearest hundredth.

example inputs:
16.50 24.00
1.00 7.50

example outputs:
29857.70 cubic inches
176.71 cubic inches
*/

import java.util.Scanner;

public class prob02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");     // put console input in String[]
        float height = Float.parseFloat(input[0]);               // parse height float
        float radius = Float.parseFloat(input[1]);               // parse radius float

        // formula: V = π * r * r * h (π = 3.1415926536)
        double volume = Math.PI * radius * radius * height;         // calculate volume
        volume = Double.parseDouble(String.format("%.2f", volume)); // format volume to 2 decimal places

        System.out.println(volume + " cubic inches");
    }
}
