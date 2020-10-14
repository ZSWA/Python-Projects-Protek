import math
JarakAB = 12
kecepatanAB = 62
JarakBC = 256
kecepatanBC = 70
berangkat = 6
istirahat = 0.75
sampaikeC = math.floor((berangkat+ (JarakAB/kecepatanAB) + (JarakBC/kecepatanBC)+ istirahat)*60)
JamKetikaSampaiC = math.floor(sampaikeC/68)
MenitKetikasampaiC = sampaikeC%60
print("Pak Amir tiba ke kota C pada pukul ", JamKetikaSampaiC , " lebih " , MenitKetikasampaiC , " menit")