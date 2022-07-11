# release-builder-utils

Commands and scripts I use to automate long repetitive tasks when it comes to handle release files, be it for final release or unzipping them for some reason (change the content, updates, etc).

## fast-zip.sh
Multithread zip for many releases. Can't recall how to use it exactly :)

## folders and names

Commands that I use when building martyr⁠— 2.0. Just a messy cheatsheet of commands.

```bash
# making dirs and moving stuff
for i in files/*; do
   mkdir $i/Textures
   mv $i/*.png $i/Textures
done

# to change names
for i in *; do mv -- "$i" "displacement_$i"; done

# making dirs
for dir in */; do cd $dir ; mkdir Mockups ; cd .. ; done

# unzip
for ((i=1;i<=12;i++)); do unzip plastic-$i-martyr.zip -d files/$i ; done

# move stuff
for dir in */; do cd $dir ; mv *.psd ../../square ; cd .. ; done
for dir in */; do cd $dir ; mv *.psd Mockups/ ; mv *.jpg Mockups/ ; cd .. ; done
```