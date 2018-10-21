#!/usr/bin/env sh

headstr="https://gibs.earthdata.nasa.gov/image-download?TIME="
footstr="&extent=-2170028.8892296343,-478197.6886162932,-1907884.8892296343,-216053.6886162932&epsg=3413&layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines&opacities=1,1&worldfile=false&format=image/jpeg&width=1024&height=1024"
for year in {2010..2017};
do
	for d in {001..365};
	do
		url=$headstr$year$d$footstr
		#echo $url
		img=$year$d.jpg
		#echo $img
		curl $url -o $img
	done
done