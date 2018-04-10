#!/bin/sh

# If you get "UnsatisfiedLinkError: /tmp/usb4java... failed to map segment from shared object: Operation not permitted",
# add the following line to the command below:
# -Djava.io.tmpdir=~/tmpdir/

JHOME="/home/nicolas/jaer-old"
java -classpath "${JHOME}/dist/jAER.jar:${JHOME}/jars/*:${JHOME}/jars/javacv/*:${JHOME}/jars/jogl/*:${JHOME}/jars/usb4java/*" -Dsun.java2d.noddraw=true -Dsun.java2d.opengl=false net.sf.jaer.util.avioutput.DvsSliceAviWriter "$@"
