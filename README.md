# Go Polar Bear!

## Get Original Data Images

### From ArcGIS

We found there are a lot of landform data from [ArcGIS](https://www.arcgis.com/apps/webappviewer/index.html?id=aff5fa8f5d5548c6bff44cc8be385f61).  For example, the GeoTiff which we can open with [QGIS](https://qgis.org) represents altitude in grayscale.

![Altitude in grayscale](https://images-2018.spaceappschallenge.org/stream-images/HmBtu4oorg78jpiwlCQNc59ftDI=/3796/width-800/)

However, most of the data is around the **land**, not the **sea/ocean**, which we are more interested in for the challenge.
![Data distribution of ArcGIS](https://images-2018.spaceappschallenge.org/stream-images/exYYMiuP9gbsAAQND0thhN0WCv4=/5953/width-800/)

Therefore, we put the eyes on NASA EOSDIS Worldview.

### From NASA EOSDIS Worldview

[Worldview](https://worldview.earthdata.nasa.gov/) has a lot of arranged environmental remote sensing images.  We can download a selected frame directly.
![EOSDIS Worldview](https://images-2018.spaceappschallenge.org/stream-images/DLQFkLRZWGqWFcoyX3z880bRuPg=/5955/width-800/)
We even downloaded the images in the same area but on different dates with [cURL](https://curl.haxx.se/) in batches.

## Image Processing for Finding Ice (with OpenCV, Matplotlib, NumPy and Python3)

Install the required tools first.  Arch Linux for example: pacman -S opencv python-numpy python-matplotlib

Photographers always check the histogram after they take the pictures.  The histogram shows the brightness distribution of the picture.  Photographers can adjust the exposure to get proper brightness distribution.

This the original image from NASA EOSDIS Worldview
![Original image](https://gibs.earthdata.nasa.gov/image-download?TIME=2010157&extent=-2170028.8892296343%2C-478197.6886162932%2C-1907884.8892296343%2C-216053.6886162932&epsg=3413&layers=MODIS_Terra_CorrectedReflectance_TrueColor%2CCoastlines&opacities=1%2C1&worldfile=false&format=image%2Fjpeg&width=1024&height=1024&fbclid=IwAR13m97uPlflqZnKFAE9zE4M6t7EXA9NghJzurM7jCS2ksiHVXM2Lp_9iY8)

We try to find the sea/ocean and ice/snow with the same idea:
1. Have the histogram of the original image with OpenCV and plot it with Matplotlib.
2. Sea/ocean is dark blue which is in dark part of the histogram.
3. Ice/snow is white which is in the bright part of the histogram.
![Histogram of original image](https://images-2018.spaceappschallenge.org/stream-images/SB_tnrVf3KY-3XZR39np6u4K6OE=/4068/width-800/)
Red line is the threshold for sea/ocean.
Green line the threshold for ice/snow.

We can get the masks with the binary method: Apply thresholds on the original image in grayscale.

* Mask for removing sea/ocean
![Mask for removing sea/ocean](https://images-2018.spaceappschallenge.org/stream-images/puH6-Y1xSJDtsoFlIJ42-dQqrh4=/4086/width-800/)
* Mask for ice/snow
![Mask for removing sea/ocean](https://images-2018.spaceappschallenge.org/stream-images/G04vMcO6KN3UPOpOjzPZ9pRg1Z4=/4087/width-800/)

We can also find the edges by Canny algorithm.
![Edge detect](https://images-2018.spaceappschallenge.org/stream-images/uppWyLkHhIhD-lUf92i7XmKhUHs=/4091/width-800/)

These methods mentioned above can also be used for Arctic waterway.

We not only distinguish the ice and sea (also land), but also make more varied landform in the game.
1. To have a smoother landform, we blurred the original image in grayscale first. ![Blurred grayscale](https://images-2018.spaceappschallenge.org/stream-images/zJxwRPbvjv8CtTrCHWT82xQNf6w=/4082/width-800/)
2. Set the sea/ocean part as 0 in grayscale. ![Grayscale image without sea](https://images-2018.spaceappschallenge.org/stream-images/f7g4q_xtE6F3bKRd-Qkh3IoQCFQ=/4089/width-800/)
3. Assign the gray value of the modified image in grayscale as the altitude in the game.  We also export the modified image in grayscale as a RAW file for the game with [GIMP](https://www.gimp.org/).

The processes mentioned above could be found at [findice.py](https://github.com/starnight/NASA2018HKT/blob/master/gen-terrain/findice.py).
```python findice.py sample/image-download.jpg test-gray.jpg```
