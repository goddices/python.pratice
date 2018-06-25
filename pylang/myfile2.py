import sys
import datetime

output_file = sys.argv[1]
shortvin = sys.argv[2]
longvin = sys.argv[3]
start_str = sys.argv[4]
end_str = sys.argv[5]

print("output file = %s, short vin = %s\r\n, long vin = %s, start = %s, end = %s" %
      (output_file, shortvin, longvin, start_str, end_str))
template = '''
insert into  CDContract  (ShortVIN,LongVIN,OfferId,OfferName,StartDate,EndDate)
values('{0}','{1}','CN0007',        'NBT 6AK Retail - Premium Package CN',  '2018-05-10','{2}') ,
	  ('{0}','{1}','CNN008',		'E.Nav Retail - Premium Package',		'2018-05-10','{3}') , 
	  ('{0}','{1}','BMPHEV_BASE_CN','BMW Phev Entry Package',				'2018-05-10','{4}') , 
	  ('{0}','{1}','BMW_PREMIUM_CN','1Y Premium Package Upselling',			'2018-05-10','{5}');
'''
start_date = datetime.datetime.strptime(start_str, "%Y/%m/%d")
end_date = datetime. datetime.strptime(end_str, "%Y/%m/%d")

days = end_date - start_date
expire_date = start_date

f1 = open(output_file, "w+")

for i in range(days.days):
    expire_date = expire_date + datetime.timedelta(days=1)
    out = template.format(shortvin, longvin,
                          (expire_date + datetime.timedelta(days=-7)).strftime("%Y-%m-%d"),
                          (expire_date + datetime.timedelta(days=7)).strftime("%Y-%m-%d"),
                          (expire_date + datetime.timedelta(days=30)).strftime("%Y-%m-%d"),
                          (expire_date + datetime.timedelta(days=90)).strftime("%Y-%m-%d"))
						  
    f1.write(out)
    f1.write("\r\n")

f1.close()
