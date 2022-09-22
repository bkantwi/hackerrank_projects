<?php
// PHP Program to find sum of elements in a given array
 
// function to return sum of elements in an array of size n
function sum( $arr, $n)
{
    // initialize sum
    $sum = 0;
 
    // Iterate through all elements and add them to sum
    for ($i = 0; $i < $n; $i++)
    $sum += $arr[$i];
 
    return $sum;
}
 
// Driver Code
$arr =array(1,2,3,4,10,11);
$n = sizeof($arr);
echo sum($arr, $n);
 
?>
