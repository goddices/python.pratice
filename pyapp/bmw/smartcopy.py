import os
import shutil

src_root = 'C:\\Users\\qxu8502\\workspace\\bmwcode\\mapgateway\\WebHosts\\'

src_files = [ 
            'Common\\CommonConst.cs',
            'Core\\FilteredHttpResponseActionResult.cs',
            'Core\\HttpClientX.cs',
            'CWInfrastructure\\Installers\\MotoristServiceInstaller.cs',
            'CWInfrastructure\\Installers\\HttpClientInstaller.cs',
            'Extensions\\ProxyServiceExtensions.cs',
            'MessageHandler\\UsidAuthorizationMessageHandler.cs',
            'Services\\IProxyService.cs',
            'Services\\ApiKeyProxyService.cs',
            'Services\\ContextMotoristProxyService.cs',
            'Services\\ContextServerHttpProxyService.cs',
            'Services\\EventHubProxyService.cs',
            'Services\\GcdmApiKeyAuthorizedProxyService.cs',
            'Services\\GcdmTokenProxyService.cs',
            'Services\\SimpleProxyServcie.cs',
            'Services\\UserLoginSyncService.cs',
            'Utilities\\HttpResponseActionResult.cs']

dest_root = 'C:\\Users\\qxu8502\\Desktop\\NewSource\\'

print('ready to work..')
if not os.path.exists(src_root):
    print('path %s does not exist',src_root)
    exit(1)

if not os.path.exists(dest_root):
    os.makedirs(dest_root) 

for file in src_files:
    srcfile = src_root + file
    desfile = dest_root + file
    inner_dir =  os.path.split(desfile)
    if not os.path.exists(inner_dir[0]):
        os.makedirs(inner_dir[0])
    shutil.copy(srcfile,desfile)
print('work complete..')