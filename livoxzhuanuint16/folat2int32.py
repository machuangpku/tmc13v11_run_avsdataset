import os


#需要修改的参数
homedir = os.getcwd()
dirpath = homedir + '\\'
cfgpath = dirpath + 'cfg\\octree-predlift\\'
datasetpath = 'D:\\AVS\\dataset\\'
newdatasetpath='D:\\AVS\\livoxuint16\\'

tmc3 = 'tmc3_2.exe'
pce = 'pc_error_2.exe'
logpath = 'log\\'
ford_01_file_lst = list()
ford_02_file_lst = list()
ford_03_file_lst = list()
livox_01_file_lst = list()
livox_02_file_lst = list()
livox_001_file_lst = list()
livox_002_file_lst = list()


num_lst1 = range(100,700,1)
num_lst2 = range(1000,1600,1)
num_lst3 = range(200,1000,1)
num_lst4 = range(1000,1700,1)
num_lst5 = range(1,7,1)
num_lst6 = range(1,10,1)
num_lst7 = range(10,100,1)
num_lst8 = range(100,387,1)
num_lst9 = range(0,1,1)


for name4 in num_lst1:
		ford_01_file_lst.append( 'Ford_01_1mm-0' + str(name4))
for name4 in num_lst1:
		ford_02_file_lst.append( 'Ford_02_1mm-0' + str(name4))
for name4 in num_lst3:
		ford_03_file_lst.append( 'Ford_03_1mm-0' + str(name4))
for name1 in num_lst6:
		livox_01_file_lst.append( 'Livox_01_all_1mm-000' + str(name1))
for name2 in num_lst7:
		livox_01_file_lst.append( 'Livox_01_all_1mm-00' + str(name2))
for name3 in num_lst8:
		livox_01_file_lst.append( 'Livox_01_all_1mm-0' + str(name3))
for name1 in num_lst6:
		livox_02_file_lst.append( 'Livox_02_all_1mm-000' + str(name1))
for name2 in num_lst7:
		livox_02_file_lst.append( 'Livox_02_all_1mm-00' + str(name2))
for name3 in num_lst8:
		livox_02_file_lst.append( 'Livox_02_all_1mm-0' + str(name3))


for name9 in num_lst9:
		livox_001_file_lst.append( 'Livox_01_all_1mm-000' + str(name9))		
for name9 in num_lst9:
		livox_002_file_lst.append( 'Livox_02_all_1mm-000' + str(name9))		

datasetlst=list([
livox_01_file_lst,
livox_02_file_lst,
])
dataset0st=list([
livox_001_file_lst,
livox_002_file_lst,
])
datasetname=list([
'basketball',
'dancer',
'exercise',
'model',
])
oridatasetname=list([
'basketball_player_vox11',
'dancer_vox11',
'exercise_vox11',
'model_vox11',
])
def getPointCount(dec,declog,enclog):
	decfile = open(dec,'r')
	voxelnum = 0
	for line in decfile:
		words = line.split()
		if words[0]=='element' and words[1]=='vertex':
			voxelnum = words[2]
			break
	changedeclog  = open(enclog,'a')
	changedeclog.write('\nTotal point count: ' + voxelnum)
	changedeclog  = open(declog,'a')
	changedeclog.write('\nTotal point count: ' + voxelnum)
	
def readpce(pcelog):
	reader = open( pcelog, 'r')
	D1=0
	for line in reader:
		words = line.split()
		if (('mseF,PSNR' in words) and ('(p2point):' in words)):
			D1=float(words[2])
	reader.close()
	return D1
	
def changeHead(s,d):
	decfile = open(s,'r+')
	newfile = open(d,'w')
	con = decfile.read()
	con1 = con.replace('ushort', 'uint16')
	#con2 = con1.replace('.00000', '')
	decfile.close()
	newfile.write(con1)
	
livox_log = open('livox_log_CW.txt', 'w')
#CW
cond = 'lossless-geom-lossless-attrs'
CW_num_lst=range(2)
for num in CW_num_lst:
	dataset=dataset0st[num]
	seqname=datasetname[num]
	oriseqname=oridatasetname[num]
	for name3 in dataset:
		codname = (cond + name3)
		encconfig =(cfgpath  + cond + '\\' + 'basketball_player_vox11_00000200'  + '\\encoder.cfg')
		decconfig =(cfgpath  + cond + '\\' + 'basketball_player_vox11_00000200'  + '\\decoder.cfg')
		seq = (datasetpath + '\\'+ name3 + '.ply')
		enc = (datasetpath +'ascii_dataset\\'+ seqname+'\\'+name3 + '.ply')
		dec = (logpath + name3 + '_dec.ply')
		bin = (logpath + name3 + '.bin')
		enclog = (logpath + codname  + '_enc.log')
		declog = (logpath + codname  + '_dec.log')
		pcelog = (logpath + codname  + '_pce.log')
		des=(newdatasetpath + '\\'+ name3 + '.ply')
		changeHead(seq,des)
		#os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' +   enc + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
		#os.remove(bin)
		#os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
		#os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -c 1 -l 1 -d 1 -r 2047 --dropdups=2 --neighborsProc=1 >' + pcelog)
		print(codname + ' finish')