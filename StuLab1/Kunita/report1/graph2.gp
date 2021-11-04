#graph2.gp 
set term png enhanced size 640,480
set output "graph2.png"
set xlabel "x" font "Arial, 20" 
set ylabel "y" font "Arial, 20" 
set xrange [-2:2]
set yrange [-6:6]
set xtics -2, 1
set ytics -6, 3
plot 2*x**3+2*x**2+x-1 t"dataA", 3*sin(2*x)-1 t"dataB"