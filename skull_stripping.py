import os
import nipype
import nipype.interfaces.fsl as fsl

data_dir= 'C:\\Users\\musto\\Documents\\workspace\\ADNI_MRI_DL_POC\\data\ADNI\\136_S_0299\\MPR__GradWarp__B1_Correction__N3__Scaled\\2006-11-08_15_19_42.0\\I40303'                                                                                                                              #path to raw image directory
ssdata_dir='C:\\Users\\musto\\Documents\\workspace\\ADNI_MRI_DL_POC\\data\ADNI\\136_S_0299\\MPR__GradWarp__B1_Correction__N3__Scaled\\2006-11-08_15_19_42.0\\I40303'                                                                                                                            #path to skull stripped image directory

for file in os.listdir(data_dir):
    try:
        mybet = nipype.interfaces.fsl.BET(in_file=os.path.join(data_dir,file),out_file=os.path.join(ssdata_dir,file +'_2.nii'), frac=0.2)                #frac=0.2
        mybet.run()                                                                                                                                      #executing the brain extraction
        print(file+'is skull stripped')
    except:
        print(file+'is not skull stripped')