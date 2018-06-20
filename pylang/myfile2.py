import os
import sys
 
output_file  = sys.argv[1]
shortvin = sys.argv[2]
longvin = sys.argv[3]
start = sys.argv[4]
end = sys.argv[5]
 

template = '''
insert into  CDContract  (ShortVIN,LongVIN,OfferId,OfferName,StartDate,EndDate)
values('{0}','{1}','CN0007',        'NBT 6AK Retail - Premium Package CN',  '2018-05-10','{2}') ,
	  ('{0}','{1}','CNN008',		'E.Nav Retail - Premium Package',		'2018-05-10','{3}') , 
	  ('{0}','{1}','BMPHEV_BASE_CN','BMW Phev Entry Package',				'2018-05-10','{4}') , 
	  ('{0}','{1}','BMW_PREMIUM_CN','1Y Premium Package Upselling',			'2018-05-10','{5}');
'''

f1 = open(output_file,"w+")
f1.write(template)
f1.close()
 