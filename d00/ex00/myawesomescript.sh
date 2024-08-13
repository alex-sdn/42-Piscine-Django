#!/bin/sh

if [ $1 ]; then
    # curl: -s = silent mode
    # cut: -d = delimiter, -f = field -> want 2nd field (==after first delimiter)
    curl -s $1 | grep href= | cut -d '"' -f2
fi
