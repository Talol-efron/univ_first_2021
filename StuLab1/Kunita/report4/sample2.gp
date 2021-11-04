set output "data2.png"
set term png enhanced size 640, 480
set title "diffrence time2"
set xlabel "M"
set ylabel "time(s)"
set xrange [0:10000]
set yrange [0:160]
set ytics 0,30
plot "data2.txt" u 1:2 t "numpy" w lp, "data2.txt" u 1:3 t "python" w lp 