import os
import pandas
import shutil

df = pandas.read_excel('path_to sheet')


df = df[df['criterion_column'] == 'value']


photo_ids = df['IDs_column'].tolist()

src_folder = 'path_source_folder'
dst_folder = 'path_destination_folder'


for photo_id in photo_ids:
   
    for filename in os.listdir(src_folder):
        
        if str(photo_id) in filename:
            
            src_path = os.path.join(src_folder, filename)

           
            dst_path = os.path.join(dst_folder, filename)

            shutil.copy2(src_path, dst_path)
