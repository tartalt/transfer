# **📦 Script to Transfer Photos Using Excel File**

This script is designed to transfer photos from one folder to another based on a specific criteria outlined in an Excel file. Specifically, it will sort photos based on their unique ID and the value of a designated column.


### **🛠️ Dependencies**

To run this script are required:

'pandas

To install the dependencies, you can run the following command in your terminal:


`pip install pandas`


### **🚀 Instructions**

Download or clone this repository to your local machine.

Open the Python file Transfer.py.

Update the source and destination folder paths to match your own directory structure.

Update the name of the Excel file to match the file name of your own inventory.

Update the name of the column in the Excel file that you wish to use for sorting the photos.

Run the script.

The script will copy photos from the source folder to the destination folder based on the values in the designated column of the Excel file.


###**📝 Notes**

The script only works for photos with a specific value in the designated column. You can modify the value in the script to match your own criteria.

If you have multiple photos with the same ID, the script will transfer all of them to the destination folder.

The script assumes that all photo files are in the same format, such as .jpg or .png. If you have different file formats, you may need to modify the script to accommodate this.
