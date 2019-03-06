import pandas as pd
import time
from PIL import Image
import os,array

os.chdir("E://Telugu Character Recogniton//Resized_Vowel_Dataset")

columnNames = list()

for i in range(784):
    columnNames.append('pixel'+str(i))
#columnNames.append('Class')

train_data = pd.DataFrame(columns = columnNames)

start_time = time.time()
for i in range(1,1201):
    t = i
    img_name = str(t)+'.jpg'
    img = Image.open(img_name)
    
    k = 0
        #print data
    data_with_class=list(img.getdata())

        
    train_data.loc[i] = data_with_class



train_data.to_csv("E://Telugu Character Recogniton//CSV_datasetsix_vowel_dataset.csv",index = False)

print( "Done", time.time()-start_time)
