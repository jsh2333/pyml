visit_ip = []

with open('access_log', 'r') as f:
   logs = f.readlines()
   for log in logs:
      log = log.split()
      ip = log[0]
      if ip not in visit_ip:
         visit_ip.append(ip)

print('고유 방문자수: [%d]' %len(visit_ip))
