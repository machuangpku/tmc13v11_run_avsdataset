import os


#需要修改的参数
homedir = os.getcwd()
dirpath = homedir + '\\'
cfgpath = dirpath + 'cfg\\octree-predlift\\'
datasetpath = 'D:\\AVS\\dataset\\'


scriptsname=(os.path.basename(__file__))
scriptsname=scriptsname.split('-')
tmc3 = 'tmc3_'+scriptsname[1]+'.exe'
pce = 'pc_error_'+scriptsname[1]+'.exe'
#os.mkdir('log')
logpath = 'log\\'


ford_01_file_lst = list()
ford_02_file_lst = list()
ford_03_file_lst = list()

basket_file_lst=list()
dacne_file_lst=list()
exercise_file_lst=list()
model_file_lst=list()


num_lst1 = range(100,1000,1)
num_lst2 = range(1000,1600,1)
num_lst3 = range(200,1000,1)
num_lst4 = range(1000,1700,1)
num_lst5 = range(1,7,1)
num_lst6 = range(1,10,1)
num_lst7 = range(10,65,1)


for name4 in num_lst1:
		ford_01_file_lst.append( 'Ford_01_vox1mm-0' + str(name4))
for name5 in num_lst2:
		ford_01_file_lst.append( 'Ford_01_vox1mm-' + str(name5))
		
for name4 in num_lst1:
		ford_02_file_lst.append( 'Ford_02_vox1mm-0' + str(name4))
for name5 in num_lst2:
		ford_02_file_lst.append( 'Ford_02_vox1mm-' + str(name5))	
		
for name4 in num_lst3:
		ford_03_file_lst.append( 'Ford_03_vox1mm-0' + str(name4))
for name5 in num_lst4:
		ford_03_file_lst.append( 'Ford_03_vox1mm-' + str(name5))

for name4 in num_lst6:
		basket_file_lst.append( 'basketball_player_vox11_0000000' + str(name4))
for name5 in num_lst7:
		basket_file_lst.append( 'basketball_player_vox11_000000' + str(name5))
for name4 in num_lst6:
		dacne_file_lst.append( 'dancer_vox11_0000000' + str(name4))
for name5 in num_lst7:
		dacne_file_lst.append( 'dancer_vox11_000000' + str(name5))
for name4 in num_lst6:
		exercise_file_lst.append( 'exercise_vox11_0000000' + str(name4))
for name5 in num_lst7:
		exercise_file_lst.append( 'exercise_vox11_000000' + str(name5))
for name4 in num_lst6:
		model_file_lst.append( 'model_vox11_0000000' + str(name4))
for name5 in num_lst7:
		model_file_lst.append( 'model_vox11_000000' + str(name5))

			
C1_num_lst = list([
				'r01',
				'r02',
				'r03',
				'r04',
				'r05',
				'r06',
        ])
		
C2_num_lst = list([
				'r01',
				'r02',
				'r03',
				'r04',
				'r05',
				'r06',
        ])
		
CW_num_lst = list([
				'r01',
        ])
		
CY_num_lst = list([
				'r01',
				'r02',
				'r03',
				'r04',
				'r05',
        ])
		



def getResolution(name2,num):
	pcerrorcfg = (cfgpath  + cond + '\\' + name2 + '\\' + num + '\\pcerror.cfg')
	reader = open( pcerrorcfg, 'r')
	Resolution = 0
	for line in reader:
		words = line.split()
		if ('resolution:' == words[0]):
			Resolution = int(words[1])
			break
	return str(Resolution)

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

#运行start

#C1
cond = 'lossless-geom-lossy-attrs'
name1 = cond + '_'
C1_lst = basket_file_lst + dacne_file_lst + exercise_file_lst+ model_file_lst
for name2 in C1_lst:
	for num in C1_num_lst:
		name3 = ('_' + num)
		codname = (name1 + name2 + name3)
		cfgname2 = ('f' + name2[1:8] + 'q1mm')
		encconfig =(cfgpath  + cond + '\\' + 'basketball_player_vox11_00000200' + '\\' + num + '\\encoder.cfg')
		decconfig =(cfgpath  + cond + '\\' + 'basketball_player_vox11_00000200' + '\\' + num + '\\decoder.cfg')
		seq = (datasetpath + name2 + '.ply')
		enc = (name1 + name2 + name3 + '_enc.ply')
		dec = (name1 + name2 + name3 + '_dec.ply')
		bin = (name1 + name2 + name3 + '.bin')
		enclog = (logpath + name1 + name2 + name3  + '_enc.log')
		declog = (logpath + name1 + name2 + name3  + '_dec.log')
		pcelog = (logpath + name1 + name2 + name3  + '_pce.log')
		print(codname + ' finish')
		os.system(tmc3 + ' --config=' + encconfig + ' --uncompressedDataPath=' + seq + ' --compressedStreamPath=' + dirpath + bin + ' >' + enclog) 
		os.system(tmc3 + ' --config=' + decconfig + ' --uncompressedDataPath=' + seq + ' --reconstructedDataPath=' + dirpath + dec + ' --compressedStreamPath=' + dirpath + bin + ' >' + declog) 
		#os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -l 1 -d 1 -d 1 -r 30000 --nbThreads=10 --dropdups=2 --neighborsProc=1 >' + pcelog)
		Resolution = getResolution('basketball_player_vox11_00000200',num)
		os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -c 1 -l 1 -d 1 --nbThreads=10 --dropdups=2  --neighborsProc=1 -r '+ Resolution + ' >' + pcelog)
		getPointCount(dec,declog,enclog)		
		os.remove(dec)
		os.remove(bin)

		


#运行end



			

		
