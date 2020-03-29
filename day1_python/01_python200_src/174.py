filename = 'python-3.5.2.exe'
subsize = 1024*1024*3  # 3MB
suffix = 0

with open(filename, 'rb') as f:
    buf = f.read(subsize)
    while buf:
        subfilename = filename + '_' + str(suffix)
        with open(subfilename, 'wb') as h:
            h.write(buf)
            print('[%s] 완료' %subfilename)
 
        buf = f.read(subsize)
        suffix += 1
