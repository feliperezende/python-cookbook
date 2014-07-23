import os

base_path = '/Users/zeroum/Desktop/OPTIM/jacarelvis/image/iphone/interaction'

for dirname, dirnames, filenames in os.walk(base_path):

    for filename in filenames:

        if '.png' in filename:
            print 'comprimindo %s' % filename 
            command = 'pngquant -f -ext .png 128 %s/%s' % (dirname, filename)
            # print command
            os.system(command)