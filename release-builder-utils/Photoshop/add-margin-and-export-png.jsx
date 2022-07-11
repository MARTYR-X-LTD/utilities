// get a reference to the current (active) document and store it in a variable named "doc"
doc = app.activeDocument;  

// change the color mode to RGB.  Important for resizing GIFs with indexed colors, to get better results
//doc.changeMode(ChangeMode.RGB);  

var docName = doc.name.slice(0, -4); // to remove the extension
var newName = docName+'.jpg';







/*

var options = new ExportOptionsSaveForWeb();
options.quality = 70;
options.format = SaveDocumentType.JPEG;
options.optimized = true;

doc.exportDocument(File(doc.path+'/'+newName),ExportType.SAVEFORWEB,options);

*/

// do the resizing.  if height > width (portrait-mode) resize based on height.  otherwise, resize based on width
if (doc.height >= doc.width) {
    var outer = doc.height * 0.15;
    var fHeight =  doc.height + outer;
    var fWidth = doc.width + outer;

    doc.resizeCanvas(UnitValue(fWidth,"px"),UnitValue(fHeight,"px"));
}
else {
    var outer = doc.width * 0.15;
    var fHeight =  doc.height + outer;
    var fWidth = doc.width + outer;

    doc.resizeCanvas(UnitValue(fWidth,"px"),UnitValue(fHeight,"px"));
}

var totalPixels = doc.height*doc.width/1000000;
var ratio = doc.width/doc.height;

if (totalPixels >= 20 ) {
    var reduction = Math.sqrt(19.9 / ratio);
    var newHeight = reduction * 1000;
    doc.resizeImage(null,UnitValue(newHeight,"px"),null,ResampleMethod.BICUBIC);
}

var options_png = new ExportOptionsSaveForWeb();
options_png.format = SaveDocumentType.PNG;
options_png.PNG8 = false;
options_png.interlaced = false;

var export_png = docName + '-cover.png';
doc.exportDocument(File(doc.path+'/'+export_png),ExportType.SAVEFORWEB,options_png);

/*
var layers = doc.artLayers

for (var i = 0; i < layers.length; i++) {
    layers[i].name = i;
}


var options_png = new ExportOptionsSaveForWeb();
options_png.format = SaveDocumentType.PNG;
options_png.PNG8 = false;
options_png.interlaced = false;


for (var i = 0; i < layers.length; i++) {
    layers[i].visible = true;
    for (var d = 0; d < layers.length; d++) {
        if (d === i) {
            continue
        }
        layers[d].visible = false;
    }
    var n = i+1;
    var export_png = docName + '-' + n + '.png';
    doc.exportDocument(File(doc.path+'/'+export_png),ExportType.SAVEFORWEB,options_png);

}

*/

/*

// Makes the default background white
var white = new SolidColor(); 
white.rgb.hexValue = "FFFFFF";
app.backgroundColor = white;

// Convert the canvas size as informed above for the END RESULT
app.activeDocument.resizeCanvas(UnitValue(fWidth,"px"),UnitValue(fHeight,"px"));

// our web export options
var options = new ExportOptionsSaveForWeb();
options.quality = 70;
options.format = SaveDocumentType.JPEG;
options.optimized = true;

var newName = 'web-'+doc.name+'.jpg';

doc.exportDocument(File(doc.path+'/'+newName),ExportType.SAVEFORWEB,options);

*/