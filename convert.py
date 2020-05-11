import xml.etree.ElementTree as ET
from os import listdir
from tqdm import tqdm
from os.path import isfile, join
def fun(fname):
	tree = ET.parse('/content/drive/My Drive/workspace/11march/ann/'+fname)
	root = tree.getroot()

	f = open('/content/drive/My Drive/workspace/11march/txts/'+fname.replace(".xml",".txt"), "w")
	for child in root:
		if(child.tag == 'object'):
			f.write(child[0].text + ' ' + child[1][0].text + ' ' + child[1][1].text + ' ' + child[1][2].text + ' ' + child[1][3].text+ '\n')

	f.close()

mypath = '/content/drive/My Drive/workspace/11march/ann/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
for p in tqdm(onlyfiles):
	fun(p)
  
  
  
#xml in form  
#<annotation>
#<filename>000144_r.jpg</filename>
#<folder>BLR-2018-03-22_17-39-26_2_frontNear_right_2</folder>
#<size>
#<width>1920</width>
#<height>1080</height>
#<depth>3</depth>
#</size>
#<object>
#<name>car</name>
#<bndbox>
#<xmin>987</xmin>
#<ymax>624</ymax>
#<xmax>999</xmax>
#<ymin>611</ymin>
#</bndbox>
#</object>
#<object>
#<name>car</name>
#<bndbox>
#<xmin>995</xmin>
#<ymax>640</ymax>
#<xmax>1024</xmax>
#<ymin>617</ymin>
#</bndbox>
#</object>
#</annotation>
  
