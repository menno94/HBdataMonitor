from beheertoolHB import BeheertoolHB
'''
input
'''

## database
## plot lines
## variable x
## oosterschelde
## checks
if __name__=='__main__':
    
    example=1
    
    if example==1:
        '''
        IJsselmeer
        '''
        ## database
        myDatabase = 'd:\InspectietoolHB\data\GR2017_IJsselmeer_6-1_v01.sqlite'
        ## open inspectietoolHB class
        HBtool = BeheertoolHB()
        ## show general info - input variables are written to file
        HBtool.get_DB_info(myDatabase)
        ## input variables  
        variables = {'WINDS':[0.0, 14.0], 'MEERP':['all'], 'WindDir':[225.0], 'loc':['YM_2_6-1_dk_00997', 'YM_1_6-1_dk_01000'],'ClosingSituation':[1], 'DB':[myDatabase]}
        ## extract data - data is written to a file
        HBtool.HBinput('Hsign', variables)
        
        ## plot results based on the text file
        HBtool.create_plot(X='loc',Y='Hsign',Z1='MEERP',Z2='WINDS')
    
    if example==2:
        '''
        Boven Maas
        '''
        ## database
        myDatabase = 'd:\\InspectietoolHB\\data\\BovenMaas\\WBI2017_Bovenmaas_36-3_v03.sqlite'
        
        ## 
        DBtool = BeheertoolHB()
        ## show general info
        DBtool.get_DB_info(myDatabase)
        ## input variables  
        variables = {'Wind speed Deelen':[5.0,0.0,10.0,20.0,15.0],
                     'Discharge Borgharen':[1300.0, 2260.0],
                     'WindDir':[45],
                     'loc':['MA_1_36-3_dk_00447'],
                     'ClosingSituation':[1],
                     'DB':[myDatabase]}
        ## extract data
        DBtool.HBinput('Wave height', variables)
        
        ## plot results
        DBtool.create_plot(Z1='Discharge Borgharen')
    
    if example==3:
        '''
        BenedenMaas
        '''
        ## database
        myDatabase = 'd:\InspectietoolHB\data\BenedenMaas\Copy_WBI2017_Benedenmaas_35-1_v03.sqlite'
        
        ## 
        DBtool = BeheertoolHB()
        ## show general info
        DBtool.get_DB_info(myDatabase)
        ## input variables  
        variables = {'Discharge Maas':[55.0, 377.0 , 884.0, 1284.0, 1708.0],
                     'Wind speed':[20.0],
                     'Waterlevel HvH':[6.04, 7.04, 8.04],
                     'WindDir':[225.0, 247.5, 270.0, 292.5, 315.0],
                     'loc':['BM_1_35-1_dk_00103'],
                     'ClosingSituation':[1],
                     'DB': [myDatabase]}
        ## extract data
        DBtoolHBinput('Hs', variables)
        
        ## plot results
        DBtool.create_plot(X='Discharge Maas', Y='Hs', Z1='Waterlevel HvH', Z2='WindDir')
    
    if example==4:
        '''
        Europoort
        '''
        ## database
        myDatabase = 'd:\InspectietoolHB\data\Europoort\Copy_WBI2017_Europoort_20-1_v03.sqlite'
        
        ## 
        DBtool = BeheertoolHB()
        ## show general info
        DBtool.get_DB_info(myDatabase)
        ## input variables  
        variables = {'ZMAXMAMO':[1.33],
                     'QBR':['all'],
                     'MAXWINDS':['all'],
                     'WindDir':['all'],
                     'loc':['CK_1_20-1_dk_00005'],
                     'ClosingSituation':[1],
                     'DB':[myDatabase]}
        ## extract data
        DBtool.HBinput('Zmax', variables)
        
        ## plot results
        DBtool.create_plot(X='QBR',Y='Zmax',Z1='WindDir',Z2='MAXWINDS')
    
    if example==5:
        '''
        Boven rivieren hoge keringen
        '''
        ## database
        myDatabase = 'd:\InspectietoolHB\data\BovenMaasHogeKeringen\WBI2017_Bovenmaas_hoge_keringen_54-1_55-1_56-1_58-1_v03.sqlite'
        
        ## 
        DBtool = BeheertoolHB()
        ## show general info
        DBtool.get_DB_info(myDatabase)
        ## input variables  
        variables = {'Wind speed Deelen':['all'],
                     'Discharge Borgharen':['all'],
                     'WindDir':[45,90],
                     'loc':['MA_1_58-1_dk_00012'],
                     'ClosingSituation':[1],
                     'DB':[myDatabase]}
        ## extract data
        DBtoolHBinput('Wave height', variables)
        
        ## plot results
        DBtool.create_plot(X='Wind speed Deelen',Y='Wave height',Z2='Discharge Borgharen',Z1='WindDir')

    if example == 6:
        '''
        Oosterschelde
        '''
        ## database
        myDatabase = 'd:\InspectietoolHB\data\WBI2017_Oosterschelde_26-2_v02\WBI2017_Oosterschelde_26-2_v02.sqlite'

        ##
        DBtool = BeheertoolHB()
        ## show general info
        DBtool.get_DB_info(myDatabase)
        ## input variables
        variables = {'MAXWINDS': ['all'],
                     'ZMAX': [4],
                     'WindDir': [30],
                     'loc': ['OS_1_26-2_dk_00006','OS_1_26-2_dk_00008','OS_1_26-2_dk_00011','OS_1_26-2_dk_00013','OS_1_26-2_dk_00016','OS_1_26-2_dk_00018'],
                     'ClosingSituation': [1],
                     'DB': [myDatabase]}
        ## extract data
        DBtool.HBinput('Dir', variables)

        ## plot results
        DBtool.create_plot(X='loc', Y='Dir', Z1='MAXWINDS')
    
    
    
