as3 = '0050900866 \
8500800575 \
9900000039 \
9700000041 \
9935080063 \
7712300000 \
7911250009 \
2211130000 \
0421125000 \
0021119000'


def main():
    print(count_zeroes(as3))

def count_zeroes(n):
    return len([z for z in n if z == '0'])

if __name__ == '__main__':
    main()
