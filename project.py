#ip project
import pandas as pd
import matplotlib.pyplot as pl
while True:
    print('\nHARYANA GENERAL STATISTICS')
    print('**************************************************************************')
    print('A. GRAPHS \nB. DATA \nC. EXIT')
    
    c=input('enter choice ')
    
    if c=='A':
        print('Main Menu\n RAINFALL\n 1.1 district wise rainfall trends\n',
              '1.2 Year wise rainfall data \n 1.3 Month wise rainfall data\n\n',
              'POPULATION\n 2.1 District wise population\n 2.2 Age wise population\n',
              '2.3 Area wise(Rural and Urban)\n\n',
              'SEX RATIO\n 3.1 Year wise (Urban and Rural)\n 3.2 District wise(Urban and Rural)',
              '\n\n 4 EXIT')
        
        o=float(input('enter your choice '))
        
        if o==1.1:
            rain=pd.read_csv('rain.csv',index_col='year')
            while True:
                city=input('enter district in haryana or All')
                if city=='All':
                    rain.plot(kind='line',marker='d')
                    pl.ylabel('Rainfall in mm')
                    pl.xlabel('Year')
                    pl.title('District wise rainfall trends of every district in haryana')
                    pl.show()
                    break
                elif city in ['Ambala','Panchkula','Yamunanagar','Kurukshetra','Kaithal','Karnal',
                              'Panipat','Sonipat','Rohtak','Jhajjar','Faridabad','Palwal',
                              'Gurgaon','Mewat','Rewari','Mahendragarh','Bhiwani','Jind',
                              'Hisar','Fatehabad','Sirsa']:
                    rain[city].plot(kind='line',marker='d',label=city)
                    pl.xlabel('Year')
                    pl.ylabel('Rainfall in mm')
                    pl.title('District wise rainfall trends')
                    pl.legend()
                    pl.show()
                    break
                else:
                    print('district not found, make sure first letter is capital')
                    
        elif o==1.2:
            yearlyrain=pd.read_csv('rain_year.csv')
            while True:
                y=str(input('choose year from[1966,1970,1975,1980,1985,1990,1995,2000,2005,2010,2012]'))
                if y in yearlyrain.columns:
                    yearlyrain[y].plot(kind='bar',label="Rainfall in mm,\nwhere no graph,data doesn't exist")
                    pl.legend()
                    pl.ylabel('Rainfall in mm')
                    pl.xticks(yearlyrain.index,yearlyrain.District)
                    pl.xlabel('districts')
                    pl.title('Year wise rainfall data')
                    pl.show()
                    break
                else:
                    print('year not found,try again')
                    
        elif o==1.3:
            monthlyrain=pd.read_csv('rainmonth.csv')
            while True:
                m=input('choose month from[January,February,March,April,May,June,July,August,September,October,November,December,Annual 2012]')
                if m in monthlyrain.columns:
                    monthlyrain[m].plot(kind='bar',label=m)
                    pl.legend()
                    pl.ylabel('Rainfall in mm')
                    pl.xlabel('District')
                    pl.title('Month wise rainfall data')
                    pl.xticks(monthlyrain.index,monthlyrain.District)
                    pl.show()
                    break
                else:
                    print('month not found,try again')
                    
        elif o==2.1:
            popu=pd.read_csv('population.csv')
            while True:
                d=input('enter district name or All')
                if d in popu.columns:
                    popu[d].plot(kind='line',marker='d',label=d)
                    pl.xticks(popu.index,popu.year,rotation=90)
                    pl.legend()
                    pl.xlabel('Year')
                    pl.ylabel('Population in thousands')
                    pl.title('District wise population')
                    pl.show()
                    break
                elif d=='All':
                    popu.plot(kind='line',marker='d')
                    pl.xticks(popu.index,popu.year,rotation=90)
                    pl.xlabel('Year')
                    pl.legend()
                    pl.ylabel('Population in thousands')
                    pl.title('District wise population')
                    pl.show()
                    break
                else:
                    print('district not found, make sure first letter is capital')
                    
        elif o==2.2:
            popage=pd.read_csv('popu_age.csv',index_col='Age Group')
            popage.plot(kind='bar')
            pl.legend()
            pl.xlabel('Age Group')
            pl.ylabel('population in Millions')
            pl.title('Age wise population')
            pl.show()
            
        elif o==2.3:
            popar=pd.read_csv('poparea.csv',index_col='District')
            while True: 
                a=input('enter area name, Rural or Urban')
                if a=='Rural':
                    popar[['Rural Total','Rural Males','Rural Females']].plot(kind='bar')
                    pl.legend()
                    pl.xlabel('District')
                    pl.ylabel('Population in Millions')
                    pl.title('Rural Population of Haryana')
                    pl.show()
                    break
                elif a=='Urban':
                    popar[['Urban Total','Urban Males','Urban Females']].plot(kind='bar')
                    pl.legend()
                    pl.xlabel('District')
                    pl.ylabel('Population in Millions')
                    pl.title('Urban Population of Haryana')
                    pl.show()
                    break
                else:
                    print('invalid, try again')
        
        elif o==3.1:
            ysr=pd.read_csv('sryear.csv',index_col='Year')
            ysr.plot(kind='bar')
            pl.xlabel('year')
            pl.ylabel('Males per 100 Females')
            pl.title('Year wise Sex Ratio')
            pl.ylim(100,160)
            pl.show()
            
        elif o==3.2:
            dsr=pd.read_csv('sr.csv',index_col='District')
            dsr.plot(kind='bar')
            pl.ylabel('Males per 100 Females')
            pl.xlabel('District')
            pl.title('District wise Sex Ratio')
            pl.ylim(100,150)
            pl.show()
            
        elif o==4:
            break
        
        else:
            print('invalid input, try again')

            
    elif c=='B':
        print('Menu\n RAINFALL\n 1.1 district wise rainfall data\n',
              '1.2 Year wise rainfall data \n 1.3 Month wise rainfall data\n\n',
              'POPULATION\n 2.1 District wise population\n 2.2 Age wise population\n',
              '2.3 Area wise(Rural and Urban)\n\n',
              'SEX RATIO\n 3.1 Year wise (Urban and Rural)\n 3.2 District wise(Urban and Rural)',
              '\n\n 4 EXIT')
        o=float(input('enter your choice '))
        
        if o==1.1:
            rain=pd.read_csv('rain.csv',index_col='year')
            print(rain)
        elif o==1.2:
            yearlyrain=pd.read_csv('rain_year.csv')
            print(yearlyrain)
        elif o==1.3:
            monthlyrain=pd.read_csv('rainmonth.csv')
            print(monthlyrain)
        elif o==2.1:
            popu=pd.read_csv('population.csv')
            print(popu)
        elif o==2.2:
            popage=pd.read_csv('popu_age.csv',index_col='Age Group')
            print(popage)
        elif o==2.3:
            popar=pd.read_csv('poparea.csv',index_col='District')
            print(popar)
        elif o==3.1:
             ysr=pd.read_csv('sryear.csv',index_col='Year')
             print(ysr)
        elif o==3.2:
             dsr=pd.read_csv('sr.csv',index_col='District')
             print(dsr)
        elif o==4:
            break
        else:
            print('invalid input, try again')
            
    elif c=='C':
        break
        
    else:
        print('invalid input, try again')
