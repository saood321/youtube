import os
directory = 'AbuBakar\disgust'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".py"):
        print(os.path.join(directory, filename))
        continue
    else:
        continue