import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)
c = int(input('doğum günü: '))
b = int(input('doğum ayı: '))
a = int(input('doğum yılı: '))
bday = datetime.date(a, b, c)

d = tıll_bday = tday - bday
print(tıll_bday)

with open('dogum tarihi.txt','w') as f:
    f.write('dogum tarihin {} {} {} dir {} gun yaşadın.'.format(c,b,a,d))
