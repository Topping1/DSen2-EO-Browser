from osgeo import gdal_array
from osgeo import gdal, osr
import numpy as np
import os

# --------------------------------------------------------------
# Open the input raster file B5
input_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B05.tiff"
input_1 = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B05.tiff")

# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B05-R.tiff"

# Define the resampling factor
resampling_factor = 2

# Get raster info
gt =input_1.GetGeoTransform()
pixelSizeX = gt[1]
pixelSizeY =-gt[5]
aa=pixelSizeX * resampling_factor
bb=pixelSizeY * resampling_factor

# Create the output file with the desired resampling factor
command = f'gdalwarp -s_srs EPSG:3857 -t_srs EPSG:3857 -r bilinear -tr {aa} {bb} -overwrite "{input_file}" "{output_file}"'
os.system(command)

# --------------------------------------------------------------
# Open the input raster file B6
input_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B06.tiff"
input_2 = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B06.tiff")

# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B06-R.tiff"

# Define the resampling factor
resampling_factor = 2

# Get raster info
gt =input_2.GetGeoTransform()
pixelSizeX = gt[1]
pixelSizeY =-gt[5]
aa=pixelSizeX * resampling_factor
bb=pixelSizeY * resampling_factor

# Create the output file with the desired resampling factor
command = f'gdalwarp -s_srs EPSG:3857 -t_srs EPSG:3857 -r bilinear -tr {aa} {bb} -overwrite "{input_file}" "{output_file}"'
os.system(command)

# --------------------------------------------------------------
# Open the input raster file B7
input_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B07.tiff"
input_3 = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B07.tiff")

# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B07-R.tiff"

# Define the resampling factor
resampling_factor = 2

# Get raster info
gt =input_3.GetGeoTransform()
pixelSizeX = gt[1]
pixelSizeY =-gt[5]
aa=pixelSizeX * resampling_factor
bb=pixelSizeY * resampling_factor

# Create the output file with the desired resampling factor
command = f'gdalwarp -s_srs EPSG:3857 -t_srs EPSG:3857 -r bilinear -tr {aa} {bb} -overwrite "{input_file}" "{output_file}"'
os.system(command)

# --------------------------------------------------------------
# Open the input raster file B8A
input_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B8A.tiff"
input_4 = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B8A.tiff")

# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B8A-R.tiff"

# Define the resampling factor
resampling_factor = 2

# Get raster info
gt =input_4.GetGeoTransform()
pixelSizeX = gt[1]
pixelSizeY =-gt[5]
aa=pixelSizeX * resampling_factor
bb=pixelSizeY * resampling_factor

# Create the output file with the desired resampling factor
command = f'gdalwarp -s_srs EPSG:3857 -t_srs EPSG:3857 -r bilinear -tr {aa} {bb} -overwrite "{input_file}" "{output_file}"'
os.system(command)


# --------------------------------------------------------------
# Open the input raster file B11
input_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B11.tiff"
input_5 = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B11.tiff")

# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B11-R.tiff"

# Define the resampling factor
resampling_factor = 2

# Get raster info
gt =input_5.GetGeoTransform()
pixelSizeX = gt[1]
pixelSizeY =-gt[5]
aa=pixelSizeX * resampling_factor
bb=pixelSizeY * resampling_factor

# Create the output file with the desired resampling factor
command = f'gdalwarp -s_srs EPSG:3857 -t_srs EPSG:3857 -r bilinear -tr {aa} {bb} -overwrite "{input_file}" "{output_file}"'
os.system(command)

# --------------------------------------------------------------
# Open the input raster file B12
input_file = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B12.tiff")
input_6 = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B12.tiff")

# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B12-R.tiff"

# Define the resampling factor
resampling_factor = 2

# Get raster info
gt =input_6.GetGeoTransform()
pixelSizeX = gt[1]
pixelSizeY =-gt[5]
aa=pixelSizeX * resampling_factor
bb=pixelSizeY * resampling_factor

# Create the output file with the desired resampling factor
command = f'gdalwarp -s_srs EPSG:3857 -t_srs EPSG:3857 -r bilinear -tr {aa} {bb} -overwrite "{input_file}" "{output_file}"'
os.system(command)

# --------------------------------------------------------------
# Open the input raster file B1
input_file = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B01.tiff")



# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B01-R.tiff"

# Define the resampling factor
resampling_factor = 6

# Create the output file with the desired resampling factor
gdal.Warp(output_file, input_file, xRes=input_file.RasterXSize / resampling_factor, yRes=input_file.RasterYSize / resampling_factor, resampleAlg='bilinear')


# Open the input raster file B9
input_file = gdal.Open("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B09.tiff")

# Define the output file name and format
output_file = "/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B09-R.tiff"

# Define the resampling factor
resampling_factor = 6

# Create the output file with the desired resampling factor
gdal.Warp(output_file, input_file, xRes=input_file.RasterXSize / resampling_factor, yRes=input_file.RasterYSize / resampling_factor, resampleAlg='bilinear')


# Open the GeoTIFF files

# Load the raster data into numpy arrays - 10m bands
file1_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B02.tiff")
file2_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B03.tiff")
file3_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B04.tiff")
file4_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B08.tiff")

# Load the raster data into numpy arrays - 20m bands (bilinear resampled)
file5_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B05-R.tiff")
file6_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B06-R.tiff")
file7_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B07-R.tiff")
file8_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B8A-R.tiff")
file9_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B11-R.tiff")
file10_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B12-R.tiff")

# Load the raster data into numpy arrays - 60m bands (bilinear resampled)
# band B10 is too noisy and it is not super-resolved
file11_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B01-R.tiff")
file12_data = gdal_array.LoadFile("/media/rick/DataDrive/satSR/EOtest/EO_Browser_images/2022-10-23-B09-R.tiff")


# Combine the 4 arrays into a single 3D array - 10m bands
data10 =  np.dstack((file1_data, file2_data, file3_data, file4_data))

# Combine the 6 arrays into a single 3D array - 20m bands
data20 =  np.dstack((file5_data, file6_data, file7_data, file8_data, file9_data, file10_data))

# Combine the 2 arrays into a single 3D array - 60m bands
data60 =  np.dstack((file11_data, file12_data))

print(data10.shape)
print(data20.shape)
print(data60.shape)