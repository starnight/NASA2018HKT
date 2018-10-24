# Go Polar Bear!

## Image Processing for Finding Ice (with OpenCV, Matplotlib and NumPy)
Photographers always check the histogram after they take the pictures.  The histogram shows the brightness distribution of the picture.  Photographers can adjust the exposure to get proper brightness distribution.

This the original image from NASA EOSDIS Worldview
![Original image](https://images-2018.spaceappschallenge.org/stream-images/bFL81KIhRZhjccN5At4BNgOFZPo=/4045/width-800/)

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
