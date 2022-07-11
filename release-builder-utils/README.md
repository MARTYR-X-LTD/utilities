# release-builder-utils

Commands and scripts I use to automate long repetitive tasks when it comes to handle release files, be it for final release or unzipping them for some reason (change the content, updates, etc).

## fast-zip.sh
Multithread zip for many releases. Verify the script to change names in releases.

Folders to make: `common` and `files`.

Inside `common` the common files used by every .zip, like manuals and stuff.
Inside `files` should be the individual files, or if the releases contains many files they should be inside numbered folders. Make them using `mkdir {1..50}` where 50 is the number of directories.

`getfolder()` to bundle many files using the numbered folders method
`getfolder2()` to bundle just one file placed in the root of `files`

## folders and names

Commands that I use when building martyr⁠— 2.0. Just a messy cheatsheet of commands.

```bash
# making dirs and moving stuff
for i in files/*; do
   mkdir $i/Textures
   mv $i/*.png $i/Textures
done

# making dirs with numbers
mkdir {1..50}

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