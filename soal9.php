<?php
$a = 20;
$b = 2;
$operator = "+";

switch ($operator) {
    case "+":
        echo $a + $b;
        break;
    case "-":
        echo $a - $b;
        break;
    case "*":
        echo $a * $b;
        break;
    case "/":
        if ($b != 0) {
            echo $a / $b;
        } else {
            echo "Tidak bisa dibagi nol";
        }
        break;
}
?>