
<!DOCTYPE html>
<html>
<head>
    <title>Menghitung Jari-jari Lingkaran</title>
</head>
<body>

<h2>Menghitung Jari-jari Lingkaran</h2>

<form method="POST">
    Masukkan Luas Lingkaran:
    <input type="number" name="luas" step="any" required>
    <button type="submit" name="hitung">HITUNG</button>
</form>

<?php
if (isset($_POST['hitung'])) {
    $luas = $_POST['luas'];
    $phi = 3.14;

    if ($luas > 0) {
        $jari = sqrt($luas / $phi);

        echo "<h3>Hasil Perhitungan</h3>";
        echo "Luas Lingkaran = $luas <br>";
        echo "Jari-jari Lingkaran = " . round($jari, 2);
    } else {
        echo "Luas harus lebih dari 0!";
    }
}
?>

</body>
</html>