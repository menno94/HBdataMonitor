InspectietoolHB
===========
Met de inspectietoolHB kan de data in de SQLite hydraulische randvoorwaarden databases worden weergeven.



Voorbeeld
--------

'''
  import InspectietoolHB from inspectietoolHB

  myDatabase = 'd:\InspectietoolHB\data\GR2017_IJsselmeer_6-1_v01.sqlite'

  DBtool = InspectietoolHB()

  #show general info - input variables are written to file
  DBtool.get_DB_info(myDatabase)

  #input variables  
  variables = {'WINDS':[0.0, 14.0], 'MEERP':['all'], 'WindDir':[225.0], 'loc':['YM_2_6-1_dk_00997',       'YM_1_6-1_dk_01000'],'ClosingSituation':[1], 'DB':[myDatabase]}
  #extract data - data is written to a file
  DBtool.DBinput('Hsign', variables)
  #plot results based on the text file
  DBtool.create_plot(X='loc',Y='Hsign',Z1='MEERP',Z2='WINDS')
  '''
