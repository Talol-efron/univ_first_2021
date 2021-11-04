#sample.gp
set term png enhanced size 640,480
set output "sample.png"
set xlabel "x" font "Arial,20"
set ylabel "y" font "Arial,20"
set title "Sample" font "Arial,30"
set xrange [30:110]
set yrange [0:12]
set xtics 30,30
set ytics 0,5
plot "data.txt" u 1:2 t "dataA" w lp