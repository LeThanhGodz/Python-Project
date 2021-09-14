def giai(dau,chan):
    klg='Không có dáp án phù hợp!'
    for i in range(dau+1):
        j=dau-i
        if 2*i+4*j==chan:
            return i,j
    return klg,klg
dau=35
chan=94
dap_an=giai(dau,chan)
print (dap_an)

#VCT Một trang trại thỏ và gà có 35 đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu?