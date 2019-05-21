from scrapy import cmdline
try:
    name = 'huangling'
    cmd = 'scrapy crawl {0}'.format(name) 
    cmdline.execute(cmd.split())
except Exception as err:
    print(err)
else:
    print('work complete')