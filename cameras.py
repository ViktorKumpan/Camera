import csv

#cчитываем все данные значения
def check_file(FILENAME):
    inf=list()
    with open(FILENAME, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            k=row['number'],row['district'],row['amount'],row['address']
            inf.append(k)
    return inf
def score(inf):
    i=1#бегунок
    count=0#cчетчик камер
    summ=list()#информация с Районами и количеством камер
    for row in inf:
        check=row[0].split('.')
        if int(check[0])==i:
            count+=int(row[2])
            helper=row[1]
        else:
            count1=helper,count
            summ.append(count1)
            i+=1
            count=0
            count+=int(row[2])
    #Нахождение последнего района
    i=inf[len(inf)-1]
    i=i[0].split('.')
    i=int(i[0])
    #Считаем количество камер в последнем районе
    count=0
    for row in inf:
        check=row[0].split('.')
        if int(check[0])==i:
            count+=int(row[2])
            helper=row[1]
    lastarea=helper,count
    summ.append(lastarea)
    return summ

#Записываем в файл Район и количество камер
def First_write(FILENAME,summ):
    myFile = open(FILENAME, 'w',encoding='utf-8')
    with myFile:
        writer = csv.writer(myFile)
        headers=[['Район','Количество камер']]# шапка
        writer.writerows(headers)
        writer.writerows(summ)  
    print("Writing complete")

# открываем следющий файл  с данными
def merge(FILENAME,summ):
    with open(FILENAME, encoding='utf-8') as file:
        inf1=list()
        inf2=list()
        reader = csv.DictReader(file)
        i=0
        for row in reader:
            value1=summ[i][0],summ[i][1],row['Население'],row['Площадь']
            inf1.append(value1)
            helper=row['Площадь'].split('.')
            helper=int(helper[0])+int(helper[1])/100
            value2=summ[i][0],summ[i][1],row['Население'],row['Площадь'],float(row['Население'])/float(helper)
            inf2.append(value2)
            i+=1
    return inf1,inf2

# записываем в файл
def Second_Write(FILENAME,inf1):
    myFile = open(FILENAME, 'w',encoding='utf-8')
    with myFile:
        writer = csv.writer(myFile)
        headers=[['Район','Число Камер','Население','Площадь']]
        writer.writerows(headers)
        writer.writerows(inf1)
        print("Writing complete")

def Third_Write(FILENAME,inf2):
    myFile = open(FILENAME, 'w',encoding='utf-8')
    with myFile:
        writer = csv.writer(myFile)
        headers=[['Район','Число камер','Население','Площадь','Плотность население']]
        writer.writerows(headers)
        writer.writerows(inf2)
    print("Writing complete")

if __name__=='__main__':
    FILENAME='spb_cameras.csv'
    Data=check_file(FILENAME)
    Score=score(Data)
    FILENAME='number_of_cameras_on_the_street.csv.csv'
    First_write(FILENAME,Score)
    FILENAME='spb_population_by_district.csv'
    Branchsumm=merge(FILENAME,Score)
    FILENAME='Number_of_cameras_and_people.csv'
    Second_Write(FILENAME,Branchsumm[0])
    FILENAME='Population_density_and_cameras.csv'
    Third_Write(FILENAME,Branchsumm[1])