# For packages that have >1 in one individual zip
getfolder() {
   folder="$1"
   zip_name="sealed_bag-$(basename $folder)-martyr.zip"
   #zip $zip_name -j common/* $folder/*
   #zip $zip_name -j common/*
   (cd common; zip -r ../$zip_name *)
   #(cd $folder; zip -u ../../$zip_name Textures/*)
   (cd $folder; zip -u -r ../../$zip_name *)
   
}

# For packages that have 1 item in one individual zip
getfolder2() {
   file="$1"
   filename_noext="$(basename $1 | sed 's/\(.*\)\..*/\1/')"
   filename="$(basename $1)"
   zip_name="$filename_noext-martyr.zip"
   #zip $zip_name -j common/* $folder/*
   zip $zip_name -j common/*
   #(cd $folder; zip -u ../../$zip_name Textures/*)
   #(cd $folder; zip -u -r ../../$zip_name *)
   (cd files; zip -u -j ../$zip_name $filename)
   
}
zip_update() {
   zip_name="$1"
   folder_name="$(basename $1 .zip)"
   mkdir $folder_name
   unzip $zip_name -d $folder_name
   rm -rf $folder_name/Shadow\ Overlays
   (cd add; zip -r ../output/$zip_name *)
   (cd $folder_name; zip -u -r ../output/$zip_name *)

}


export -f getfolder
export -f getfolder2
export -f zip_update

#ls -1v files | parallel getfolder2 {}
#ls -1 *.zip | parallel zip_update {}

# -r is recursive while preserving subfolders structure
# -j will place the files irrespective from the directory that was called. Will NOT preserve subfolder structure
# can't be used together. Use the (cd etc etc) thing

# find . -type d -path '*/files/*' -prune | parallel getfolder {}
find . -type f -path '*/files/*' -prune | parallel getfolder2 {}

for f in *.zip; do
    x="$(zipinfo -t "$f" | awk '{print $1}')"
    echo "$f: contains $x files" 
done

