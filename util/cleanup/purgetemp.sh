#!/bin/bash
CWD=$PWD
TEMPDIR=$PWD/../../data/Temp

if [ -d $TEMPDIR ]; then
    rm -r $TEMPDIR/* 
else
    echo Cannot find directory $TEMPDIR
fi
