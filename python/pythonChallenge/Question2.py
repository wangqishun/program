
#question_2
val = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''
'''
beg, end = ord('a'),ord('z')
val_new = []
for ch in range(len(val)):
    if ord(val[ch]) < beg or ord(val[ch]) > end:
        val_new.append(val[ch])
        continue
    ch_new = ord(val[ch]) + 2
    if ch_new > end:
        ch_new = beg + ch_new - end - 1
    val_new.append(chr(ch_new))
print(''.join(val_new))
'''

import string

strtrans_new = str.maketrans(string.ascii_lowercase[:], string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
#frm = [chr(x) for x in range(ord('a'),ord('z') + 1)]
#to = [chr(ord(frm[x]) + 2) for x in range(len(frm))]
#to = frm[2:] + frm[:2]
#strtrans = str.maketrans(''.join(frm), ''.join(to))
val_new = val.translate(strtrans_new)
print(val_new)
print("map".translate(strtrans_new))

