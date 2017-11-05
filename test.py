#!/usr/bin/python2.7

import os, sys, platform, string, struct

if len(sys.argv) != 2:
  print "usage: ./test.py FILENAME"
  exit()

DEFINE =  [  ]
DYNASM = os.path.basename(sys.argv[1]).find(".dasc") > 0

if DYNASM:
    if platform.system() == "Windows": DEFINE += [ "WIN" ]
    if os.uname()[4] == "x86_64": DEFINE += [ "X64" ]
    dynasm = {
      "compiler"  : "luajit",
      "output"    : sys.argv[1].replace(".dasc", ".c"),
      "source"    : sys.argv[1],
      "define"    : " ".join(map(lambda x:"-D " + x, DEFINE)),
    }

compile = {
  "compiler"  : "gcc",
  "output"    : os.path.basename(sys.argv[1]).replace(".dasc" if DYNASM else ".c", ".exe" if os.name == "nt" else ""),
  "source"    : sys.argv[1].replace(".dasc", ".c") if DYNASM else sys.argv[1],
  "link"      : "",
  "flags"     : " ".join([ "-g", "-Wall", "-Wextra", "--std=c99", "-fno-strict-aliasing" ]),
  # "flags"     : " ".join([ "-O3", "-Wall", "-Wextra", "--std=c99", "-fno-strict-aliasing" ]),
}


if DYNASM: template0 = "$compiler src/dynasm/dynasm.lua -N $define -o $output $source"
template1 = "$compiler -o bin/$output $source $link $flags"

if not os.path.exists("bin"):
    os.makedirs("bin")

if DYNASM:
    print string.Template(template0).substitute(dynasm)
    # os.system(string.Template(template0).substitute(dynasm))
# os.system(string.Template(template1).substitute(compile))
print string.Template(template1).substitute(compile)


# if DYNASM: os.remove(sys.argv[1].replace(".dasc", ".c"))
