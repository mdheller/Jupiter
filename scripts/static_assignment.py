dag=['localpro',
 {'aggregate0': ['1',
                 'true',
                 'simpledetector0',
                 'astutedetector0',
                 'dftdetector0',
                 'teradetector0'],
  'aggregate1': ['1',
                 'true',
                 'simpledetector1',
                 'astutedetector1',
                 'dftdetector1',
                 'teradetector1'],
  'aggregate2': ['1',
                 'true',
                 'simpledetector2',
                 'astutedetector2',
                 'dftdetector2',
                 'teradetector2'],
  'astutedetector0': ['1', 'true', 'fusioncenter0'],
  'astutedetector1': ['1', 'true', 'fusioncenter1'],
  'astutedetector2': ['1', 'true', 'fusioncenter2'],
  'dftdetector0': ['1',
                   'true',
                   'fusioncenter0',
                   'dftslave00',
                   'dftslave01',
                   'dftslave02'],
  'dftdetector1': ['1',
                   'true',
                   'fusioncenter1',
                   'dftslave10',
                   'dftslave11',
                   'dftslave12'],
  'dftdetector2': ['1',
                   'true',
                   'fusioncenter2',
                   'dftslave20',
                   'dftslave21',
                   'dftslave22'],
  'dftslave00': ['1', 'false', 'dftslave00'],
  'dftslave01': ['1', 'false', 'dftslave01'],
  'dftslave02': ['1', 'false', 'dftslave02'],
  'dftslave10': ['1', 'false', 'dftslave10'],
  'dftslave11': ['1', 'false', 'dftslave11'],
  'dftslave12': ['1', 'false', 'dftslave12'],
  'dftslave20': ['1', 'false', 'dftslave20'],
  'dftslave21': ['1', 'false', 'dftslave21'],
  'dftslave22': ['1', 'false', 'dftslave22'],
  'fusioncenter0': ['4', 'true', 'globalfusion'],
  'fusioncenter1': ['4', 'true', 'globalfusion'],
  'fusioncenter2': ['4', 'true', 'globalfusion'],
  'globalfusion': ['3', 'true', 'home'],
  'localpro': ['1', 'false', 'aggregate0', 'aggregate1', 'aggregate2'],
  'simpledetector0': ['1', 'true', 'fusioncenter0'],
  'simpledetector1': ['1', 'true', 'fusioncenter1'],
  'simpledetector2': ['1', 'true', 'fusioncenter2'],
  'teradetector0': ['1', 'true', 'fusioncenter0', 'teramaster0'],
  'teradetector1': ['1', 'true', 'fusioncenter1', 'teramaster1'],
  'teradetector2': ['1', 'true', 'fusioncenter2', 'teramaster2'],
  'teramaster0': ['1', 'false', 'teraworker00', 'teraworker01', 'teraworker02'],
  'teramaster1': ['1', 'false', 'teraworker10', 'teraworker11', 'teraworker12'],
  'teramaster2': ['1', 'false', 'teraworker20', 'teraworker21', 'teraworker22'],
  'teraworker00': ['1', 'false', 'teraworker00'],
  'teraworker01': ['1', 'false', 'teraworker01'],
  'teraworker02': ['1', 'false', 'teraworker02'],
  'teraworker10': ['1', 'false', 'teraworker10'],
  'teraworker11': ['1', 'false', 'teraworker11'],
  'teraworker12': ['1', 'false', 'teraworker12'],
  'teraworker20': ['1', 'false', 'teraworker20'],
  'teraworker21': ['1', 'false', 'teraworker21'],
  'teraworker22': ['1', 'false', 'teraworker22']},
 {'aggregate0': 'node12',
  'aggregate1': 'node1',
  'aggregate2': 'node11',
  'astutedetector0': 'node5',
  'astutedetector1': 'node13',
  'astutedetector2': 'node8',
  'dftdetector0': 'node9',
  'dftdetector1': 'node11',
  'dftdetector2': 'node10',
  'dftslave00': 'node39',
  'dftslave01': 'node39',
  'dftslave02': 'node70',
  'dftslave10': 'node79',
  'dftslave11': 'node23',
  'dftslave12': 'node81',
  'dftslave20': 'node73',
  'dftslave21': 'node63',
  'dftslave22': 'node48',
  'fusioncenter0': 'node11',
  'fusioncenter1': 'node1',
  'fusioncenter2': 'node12',
  'globalfusion': 'node1',
  'localpro': 'node1',
  'simpledetector0': 'node6',
  'simpledetector1': 'node12',
  'simpledetector2': 'node7',
  'teradetector0': 'node4',
  'teradetector1': 'node1',
  'teradetector2': 'node3',
  'teramaster0': 'node23',
  'teramaster1': 'node81',
  'teramaster2': 'node57',
  'teraworker00': 'node7',
  'teraworker01': 'node61',
  'teraworker02': 'node84',
  'teraworker10': 'node19',
  'teraworker11': 'node63',
  'teraworker12': 'node62',
  'teraworker20': 'node35',
  'teraworker21': 'node71',
  'teraworker22': 'node63'}]
schedule=['localpro',
 {'aggregate0': ['1',
                 'true',
                 'simpledetector0',
                 'astutedetector0',
                 'dftdetector0',
                 'teradetector0'],
  'aggregate1': ['1',
                 'true',
                 'simpledetector1',
                 'astutedetector1',
                 'dftdetector1',
                 'teradetector1'],
  'aggregate2': ['1',
                 'true',
                 'simpledetector2',
                 'astutedetector2',
                 'dftdetector2',
                 'teradetector2'],
  'astutedetector0': ['1', 'true', 'fusioncenter0'],
  'astutedetector1': ['1', 'true', 'fusioncenter1'],
  'astutedetector2': ['1', 'true', 'fusioncenter2'],
  'dftdetector0': ['1',
                   'true',
                   'fusioncenter0',
                   'dftslave00',
                   'dftslave01',
                   'dftslave02'],
  'dftdetector1': ['1',
                   'true',
                   'fusioncenter1',
                   'dftslave10',
                   'dftslave11',
                   'dftslave12'],
  'dftdetector2': ['1',
                   'true',
                   'fusioncenter2',
                   'dftslave20',
                   'dftslave21',
                   'dftslave22'],
  'dftslave00': ['1', 'false', 'dftslave00'],
  'dftslave01': ['1', 'false', 'dftslave01'],
  'dftslave02': ['1', 'false', 'dftslave02'],
  'dftslave10': ['1', 'false', 'dftslave10'],
  'dftslave11': ['1', 'false', 'dftslave11'],
  'dftslave12': ['1', 'false', 'dftslave12'],
  'dftslave20': ['1', 'false', 'dftslave20'],
  'dftslave21': ['1', 'false', 'dftslave21'],
  'dftslave22': ['1', 'false', 'dftslave22'],
  'fusioncenter0': ['4', 'true', 'globalfusion'],
  'fusioncenter1': ['4', 'true', 'globalfusion'],
  'fusioncenter2': ['4', 'true', 'globalfusion'],
  'globalfusion': ['3', 'true', 'home'],
  'localpro': ['1', 'false', 'aggregate0', 'aggregate1', 'aggregate2'],
  'simpledetector0': ['1', 'true', 'fusioncenter0'],
  'simpledetector1': ['1', 'true', 'fusioncenter1'],
  'simpledetector2': ['1', 'true', 'fusioncenter2'],
  'teradetector0': ['1', 'true', 'fusioncenter0', 'teramaster0'],
  'teradetector1': ['1', 'true', 'fusioncenter1', 'teramaster1'],
  'teradetector2': ['1', 'true', 'fusioncenter2', 'teramaster2'],
  'teramaster0': ['1', 'false', 'teraworker00', 'teraworker01', 'teraworker02'],
  'teramaster1': ['1', 'false', 'teraworker10', 'teraworker11', 'teraworker12'],
  'teramaster2': ['1', 'false', 'teraworker20', 'teraworker21', 'teraworker22'],
  'teraworker00': ['1', 'false', 'teraworker00'],
  'teraworker01': ['1', 'false', 'teraworker01'],
  'teraworker02': ['1', 'false', 'teraworker02'],
  'teraworker10': ['1', 'false', 'teraworker10'],
  'teraworker11': ['1', 'false', 'teraworker11'],
  'teraworker12': ['1', 'false', 'teraworker12'],
  'teraworker20': ['1', 'false', 'teraworker20'],
  'teraworker21': ['1', 'false', 'teraworker21'],
  'teraworker22': ['1', 'false', 'teraworker22']},
 {'aggregate0': ['aggregate0',
                 'ubuntu-s-1vcpu-3gb-sgp1-01',
                 'root',
                 'PASSWORD'],
  'aggregate1': ['aggregate1', 'ubuntu-2gb-sfo1-05', 'root', 'PASSWORD'],
  'aggregate2': ['aggregate2', 'ubuntu-2gb-sfo1-02', 'root', 'PASSWORD'],
  'astutedetector0': ['astutedetector0',
                      'ubuntu-2gb-fra1-01',
                      'root',
                      'PASSWORD'],
  'astutedetector1': ['astutedetector1',
                      'ubuntu-s-1vcpu-3gb-sgp1-02',
                      'root',
                      'PASSWORD'],
  'astutedetector2': ['astutedetector2',
                      'ubuntu-2gb-nyc2-03',
                      'root',
                      'PASSWORD'],
  'dftdetector0': ['dftdetector0', 'ubuntu-2gb-nyc2-04', 'root', 'PASSWORD'],
  'dftdetector1': ['dftdetector1', 'ubuntu-2gb-sfo1-02', 'root', 'PASSWORD'],
  'dftdetector2': ['dftdetector2', 'ubuntu-2gb-sfo1-01', 'root', 'PASSWORD'],
  'dftslave00': ['dftslave00',
                 'ubuntu-s-1vcpu-3gb-lon1-03',
                 'root',
                 'PASSWORD'],
  'dftslave01': ['dftslave01',
                 'ubuntu-s-1vcpu-3gb-lon1-03',
                 'root',
                 'PASSWORD'],
  'dftslave02': ['dftslave02',
                 'ubuntu-s-1vcpu-3gb-tor1-10',
                 'root',
                 'PASSWORD'],
  'dftslave10': ['dftslave10',
                 'ubuntu-s-1vcpu-3gb-fra1-01',
                 'root',
                 'PASSWORD'],
  'dftslave11': ['dftslave11',
                 'ubuntu-s-1vcpu-3gb-nyc1-04',
                 'root',
                 'PASSWORD'],
  'dftslave12': ['dftslave12',
                 'ubuntu-s-1vcpu-3gb-fra1-03',
                 'root',
                 'PASSWORD'],
  'dftslave20': ['dftslave20',
                 'ubuntu-s-1vcpu-3gb-tor1-07',
                 'root',
                 'PASSWORD'],
  'dftslave21': ['dftslave21',
                 'ubuntu-s-1vcpu-3gb-sfo2-02',
                 'root',
                 'PASSWORD'],
  'dftslave22': ['dftslave22',
                 'ubuntu-s-1vcpu-3gb-sgp1-07',
                 'root',
                 'PASSWORD'],
  'fusioncenter0': ['fusioncenter0', 'ubuntu-2gb-sfo1-02', 'root', 'PASSWORD'],
  'fusioncenter1': ['fusioncenter1', 'ubuntu-2gb-sfo1-05', 'root', 'PASSWORD'],
  'fusioncenter2': ['fusioncenter2',
                    'ubuntu-s-1vcpu-3gb-sgp1-01',
                    'root',
                    'PASSWORD'],
  'globalfusion': ['globalfusion', 'ubuntu-2gb-sfo1-05', 'root', 'PASSWORD'],
  'home': ['home', 'ubuntu-2gb-ams2-04', 'root', 'PASSWORD'],
  'localpro': ['localpro', 'ubuntu-2gb-sfo1-05', 'root', 'PASSWORD'],
  'simpledetector0': ['simpledetector0',
                      'ubuntu-2gb-fra1-02',
                      'root',
                      'PASSWORD'],
  'simpledetector1': ['simpledetector1',
                      'ubuntu-s-1vcpu-3gb-sgp1-01',
                      'root',
                      'PASSWORD'],
  'simpledetector2': ['simpledetector2',
                      'ubuntu-2gb-nyc2-02',
                      'root',
                      'PASSWORD'],
  'teradetector0': ['teradetector0', 'ubuntu-2gb-ams2-03', 'root', 'PASSWORD'],
  'teradetector1': ['teradetector1', 'ubuntu-2gb-sfo1-05', 'root', 'PASSWORD'],
  'teradetector2': ['teradetector2', 'ubuntu-2gb-sfo1-03', 'root', 'PASSWORD'],
  'teramaster0': ['teramaster0',
                  'ubuntu-s-1vcpu-3gb-nyc1-04',
                  'root',
                  'PASSWORD'],
  'teramaster1': ['teramaster1',
                  'ubuntu-s-1vcpu-3gb-fra1-03',
                  'root',
                  'PASSWORD'],
  'teramaster2': ['teramaster2',
                  'ubuntu-s-1vcpu-3gb-blr1-01',
                  'root',
                  'PASSWORD'],
  'teraworker00': ['teraworker00', 'ubuntu-2gb-nyc2-02', 'root', 'PASSWORD'],
  'teraworker01': ['teraworker01',
                   'ubuntu-s-1vcpu-3gb-blr1-05',
                   'root',
                   'PASSWORD'],
  'teraworker02': ['teraworker02',
                   'ubuntu-s-1vcpu-3gb-fra1-06',
                   'root',
                   'PASSWORD'],
  'teraworker10': ['teraworker10',
                   'ubuntu-s-1vcpu-3gb-blr1-11',
                   'root',
                   'PASSWORD'],
  'teraworker11': ['teraworker11',
                   'ubuntu-s-1vcpu-3gb-sfo2-02',
                   'root',
                   'PASSWORD'],
  'teraworker12': ['teraworker12',
                   'ubuntu-s-1vcpu-3gb-sfo2-01',
                   'root',
                   'PASSWORD'],
  'teraworker20': ['teraworker20',
                   'ubuntu-s-1vcpu-3gb-ams3-07',
                   'root',
                   'PASSWORD'],
  'teraworker21': ['teraworker21',
                   'ubuntu-s-1vcpu-3gb-tor1-09',
                   'root',
                   'PASSWORD'],
  'teraworker22': ['teraworker22',
                   'ubuntu-s-1vcpu-3gb-sfo2-02',
                   'root',
                   'PASSWORD']}]
