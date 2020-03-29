services = {}

with open('access_log', 'r') as f:
   logs = f.readlines()
   for log in logs:
      log = log.split()
      ip = log[0]
      servicebyte = log[9]
      if servicebyte.isdigit():
         servicebyte = int(servicebyte)
      else:
         servicebyte = 0

      if ip not in services:
         services[ip] = servicebyte
      else:
         services[ip] += servicebyte

ret = sorted(services.items(), key=lambda x: x[1], reverse=True)

print('사용자IP – 서비스용량')
for ip, b in ret:
   print('[%s] – [%d]' %(ip, b))
