set output "data1.png"
set term png enhanced size 640, 480
set title "diffrence time1"
set xlabel "N"
set ylabel "time(s)"
set xrange [0:10000000]
set yrange [0:6]
set ytics 0, 1
plot "data1.txt" u 1:2 t "numpy" w lp, "data1.txt" u 1:3 t "python" w lp 