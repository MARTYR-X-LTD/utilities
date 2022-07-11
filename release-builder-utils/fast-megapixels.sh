getmp() {
   file="$1"
   WIDTH=$(identify -format '%w' "$file")
   HEIGHT=$(identify -format '%h' "$file")
   PYTHONC="print($WIDTH*$HEIGHT/1000000.0)"
   MP=$( python -c $PYTHONC )
   echo "$(basename "$file") - $MP - $WIDTH\×$HEIGHT\px"
}

export -f getmp

find . -type f -name "*.png" | parallel getmp {}