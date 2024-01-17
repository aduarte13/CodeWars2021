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

import kotlin.math.PI

fun main(){
    val (height, radius) = readln().split(' ').map(String::toFloat) // read input from console

    // formula: V = π * r * r * h (π = 3.1415926536)
    var volume = PI * radius * radius * height          // calculate volume using formula
    volume = String.format("%.2f", volume).toDouble()   // round to 2 decimal places
    // NOTE: couldn't figure out how to include trailing zeroes

    print("$volume cubic inches")
}