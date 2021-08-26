import sys
import os
import hashlib

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('python get-image-merkle-hash.py <image-dir>')
        sys.exit(1)
    
    image_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), sys.argv[1])

    h = hashlib.sha256()

    for i in range(1, 1560):
        with open(f"{os.path.join(image_dir, str(i) + '.png')}", "rb") as f:
            h.update(f.read())

    print(h.hexdigest())
