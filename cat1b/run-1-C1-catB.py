import os
import shutil


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

def copyexe(file,processnum):
	ori=file+'.exe'
	new=file+'_'+str(processnum)+'.exe'
	if(os.path.exists(new)):
		os.remove(new)
	shutil.copyfile(ori, new)
	return new
encoder = dirpath + 'tmc3'
encoder1 = dirpath + 'pc_error'
copyexe(encoder,scriptsname[1])
copyexe(encoder1,scriptsname[1])

catA_lst = list([
				'basketball_player_vox11_00000200',
				'boxer_viewdep_vox12',
				'dancer_vox11_00000001',
				'egyptian_mask_vox12',
				'facade_00009_vox12',
				'facade_00015_vox14',
				'facade_00064_vox11',
				'frog_00067_vox12',
				'head_00039_vox12',
				'house_without_roof_00057_vox12',
				'longdress_viewdep_vox12',
				'loot_viewdep_vox12',
				'redandblack_viewdep_vox12',
				'shiva_00035_vox12',
				'soldier_viewdep_vox12',
				'thaidancer_viewdep_vox12',
				'ulb_unicorn_vox13',
				'citytunnel_q1mm',
				'overpass_q1mm',
				'tollbooth_q1mm',
])

catB_lst = list([				
				'Truck_vox15',
				'QQdog_vox15',
				'Ignatius_vox11',
				'Courthouse_vox16',
				'Church_vox16',
				'stanford_area_4_vox20',
				'stanford_area_2_vox20',
				
])	

catA_normal5_lst = list([
				'longdress_vox10_1300',
				'loot_vox10_1200',
				'queen_0200',
				'redandblack_vox10_1550',
				'soldier_vox10_0690',
])


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
	
dataset = list([
				catB_lst,
				[],
				[],
				[],
				[],
        ])	
#运行start

#C1
cond = 'lossless-geom-lossy-attrs'
name1 = cond + '_'
C1_lst = catB_lst
for name2 in C1_lst:
	for num in C1_num_lst:
		name3 = ('_' + num)
		codname = (name1 + name2 + name3)
		encconfig =(cfgpath  + cond + '\\' + name2 + '\\' + num + '\\encoder.cfg')
		decconfig =(cfgpath  + cond + '\\' + name2 + '\\' + num + '\\decoder.cfg')
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
		Resolution = getResolution(name2,num)
		os.system(pce + ' -a ' + seq + ' -b ' + dirpath + dec + ' -c 1 -l 1 -d 1 --nbThreads=10 --dropdups=2  --neighborsProc=1 -r '+ Resolution + ' >' + pcelog)
		getPointCount(dec,declog,enclog)
		os.remove(dec)
		os.remove(bin)
