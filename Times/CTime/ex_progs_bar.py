from time import sleep
from tqdm import tqdm

##pip install tqdm 
#   1second 20 times------------------5%

##     Progress Meters or Progress Bars. tqdm got its name from the Arabic name taqaddum which means 'progress
from tqdm import tqdm
for i in tqdm(range(20)):
    sleep(.1)


#for i in tqdm(range(10)):
#    pass

