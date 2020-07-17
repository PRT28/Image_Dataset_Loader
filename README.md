# Image_Dataset_Loader
This program loads image datasets to the corresponding features and labels

This function works over an image dataset with any number of categories. As the actual code is very tedious and hectic, so we build a module in order to cut down this code for you. All you have to do is just seperate image according to categories and save that in different folders and rest everything this code will do for you from processing to normalization and flattening of the image and finally appending it to X and Y accordingly.


# Packages you need to install for this function to work are as follows:
  os  
  
  numpy 
  
  cv2

# Syntax of the function you will be calling:
   
   load_dataset(path,mode,size=(64,64)):
   
   path : Path will be the complete location address to your dataset
   
   size Can be of the form tuple as well as list with (width,height) as the input format and in default 64,64 size would be used.
   
   mode: There will be three modes that will be available for you to use 
              
              gray: for grayscale images
              
              rgb: for rgb format
              
              and by default bgr will be used
              
to reuse this code:
  
    pip install -e Image_Dataset_Loader
