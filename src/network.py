import speedtest

s = speedtest.Speedtest()
s.get_best_server()
down = s.download()
up = s.upload()

result = s.results.dict()
down_mb = down / 1000000
up_mb =  up / 1000000

print(result["ping"])
print('Download: %.2f Mbps' % down_mb)
print('Upload: %.2f Mbps' % up_mb)