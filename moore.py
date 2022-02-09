# Moore makinası

dizin = "C:/Users/ali ihsan/Desktop/Çocuklar/Bahaeddin/moore/"

fGecisTablosu = 'Gecistablosu.txt'
fOutputTablosu = 'Output.txt'

GecisTablosu = {}
OutputTablosu = {}

#ilk giriş state'ini bu değişkende tutalım
ilkgiris = ''

# Geçiş tablosunun okunup, oluşturulması
with open(dizin+fGecisTablosu) as f:
    muhteva = f.readlines()

    baslik = muhteva[0]
    girdiler = baslik.strip().split(sep='\t')[1:]

    GirdiAdedi = len(girdiler)

    say = 0
    for line in muhteva[1:]:
        satir = line.strip().split(sep='\t')
        print(satir)
        d = {girdiler[i]:satir[i+1] for i in range(GirdiAdedi)}
        print(d)
        GecisTablosu[satir[0]] = d
        print(GecisTablosu)
        if say == 0:
            ilkgiris = satir[0]
        say = say + 1

        
# Output tablosunun okunup, oluşturulması
with open(dizin+fOutputTablosu) as f:
    muhteva = f.readlines()

    for line in muhteva[1:]:
        satir = line.strip().split(sep='\t')
        OutputTablosu[satir[0]] = satir[1]
        print(OutputTablosu)

# Kullanıcıdan giriş stringinin istenmesi
giris = input('Lütfen giriş stringini giriniz:')
giris="aaababbaabb"

print('\n'*2)
print('Adım Adım Gösterim')
print('==================')
stateler = []
ciktilar = []
stateler.append(ilkgiris)
ciktilar.append(OutputTablosu[ilkgiris])

state =  ilkgiris

for g in giris:
    state = GecisTablosu[state][g]
    cikti = OutputTablosu[state]
    print('Girdi:',g, 'State:',state, 'Çıktı:',cikti)
    stateler.append(state)
    ciktilar.append(cikti)

print('\n'*2)
print('Toplu Gösterim:')
print('===============')
print('Girdi:',giris)
print('Stateler:', stateler)
print('Outputlar:',ciktilar)
print('Çıktı:',''.join(ciktilar))
