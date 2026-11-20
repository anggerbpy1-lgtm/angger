<?php
$nilai = [
    "Angger" => 100,
    "jokowi" => 95,
    "Albert Enstein" => 98,
    "Roy suryo" => 24,
    "Ahmad Saroni" => 60
];

echo "<h1>DAFTAR NILAI SISWA</h1> <br>";
echo "<table border='1' celpadding='8'>";
echo "<tr><th>nama</th><th>nilai</th></tr>";

foreach($nilai as $nama => $angka) {
    echo "<tr><td>$nama</td><td>$angka</td></tr>";
}

echo "</table>";
$rata = array_sum($nilai) / count($nilai);
echo "Rata-rata nilai: $rata <br>";
echo "Nilai tertinggi: " . max($nilai) . "<br>";
echo "Nilai terendah: " . min($nilai) . "<br>";  