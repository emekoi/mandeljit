luajit dynasm/dynasm.lua -N -D WIN -o jit.c jit.dasc
gcc -c -g -Wall -Wextra --std=c99 -pedantic -fno-strict-aliasing -finline-functions -funroll-loops basic.c -o ../bin/basic.o
gcc -c -g -Wall -Wextra --std=c99 -pedantic -fno-strict-aliasing -finline-functions -funroll-loops jit.c -o ../bin/jit.o
gcc ../bin/basic.o -lm -o ../bin/basic.exe
gcc ../bin/jit.o -lm -o ../bin/jit.exe

# time ../bin/basic *bb+ab > ../bin/basic_out.pgm
# time ../bin/jit *bb+ab > ../bin/jit_out.pgm
