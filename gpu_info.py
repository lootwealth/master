import re
import sys
import os


def rd_file(fname, re_r):
    with open(str(fname), 'r') as ff:
        res = ff.read()
    re_rule = re.compile(str(re_r))
    result_findall = re.findall(re_rule, res)
    return result_findall


def hard_info(num=0, info="gpu_name"):
        revl = rd_file("amdcovc_meminfo.txt", '{"chip_type": .*?}')
        vl = eval(revl[num])
        print(vl[str(info)])


def hash_info(num_hash='0'):
        revl = rd_file("hash.txt", 'GPU.*?Mh')
        sd = {}
        strsum = '{"'
        strsum2 = '"}'
        for i0 in revl:
            i1 = i0.replace(',', '')
            i2 = i1.replace('GPU', '')
            i3 = i2.replace(' Mh', '')
            i4 = i3.replace(' ', ':')
            i5 = i4.replace(':','":"')
            nstr = strsum+i5+strsum2
            nstrE = eval(nstr)
            sd.update(nstrE)
        print(sd[str(num_hash)])


def get_incorrect(num="0"):
        result_findall = rd_file("hash_Incorrect", 'GPU.*?$')
        sd = {}
        strsum = '{"'
        strsum2 = '"}'
        for i in result_findall:
            i1 = i.replace(', ', '","')
            i2 = i1.replace('GPU', '')
            i3 = i2.replace(' ', ':')
            i4 = i3.replace(':', '":"')
            nstr = strsum + i4 + strsum2
            nstrE = eval(nstr)
            sd.update(nstrE)
        print(sd[str(num)])

"""
hard_info(5)
hash_info(2)
get_incorrect(3)
"""
try:
    for i in range(7):
        hard_info(i)
        hash_info(i)
        get_incorrect(i)
# except (RuntimeError, TypeError, NameError,IndexError):
        # pass
except RuntimeError:
    print("RuntimeError.")
except TypeError:
    print("TypeError.")
except NameError:
    print("NameError.")
except IndexError:
    print("IndexError.")


