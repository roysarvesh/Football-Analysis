import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df=pd.read_csv('Worldcup2018.csv')
df1=pd.read_csv('ASSIST.csv')
df2=pd.read_csv('GOALS.csv')
df3=pd.read_csv('PENALITIES.csv')


Ye=df['Year']
dt=df['datetime']
se=df['stage']
sm=df['stadium']
ct=df['city']
htn=df['home_team_name']
htg=df['home_team_goals']
atg=df['away_team_goals']
atn=df['away_team_name']
re=df['referee']
a1=df['assistant_1']
a2=df['assistant_2']
md=df['matchid']
at=df['attendance']
p=df3['PENALTIES SCORED']
g=df2['GOALS']
a3=df1['ASSISTS']

def abc(s):
    d = Counter()
    l = []
    for i in s:
        a = ' ' * d[i] + i
        d[i] += 1
        l.append(a)
    return l 

def mainmenu():
    choice=0
    while choice !='x':
        print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
        print('!    Football World Cup 2018        !')
        print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
        print('!1} Display Data                    !')
        print('!-----------------------------------!')
        print('!2} Data Visualization              !')
        print('!-----------------------------------!')
        print('!3} Data Analysis                   !')
        print('!-----------------------------------!')
        print('!4} Exit                            !')
        print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
        choice=input('Your Option:')
        if choice=='1':
            print('Displaying Data')
            print(df)
            print(df.stadium)
            print(df.city)
            print(df.home_team_name)
            print(df.home_team_goals)
            print(df.away_team_goals)
            print(df.away_team_name)
            print(df.referee)
            print(df.assistant_1)
            print(df1)
            print(df2)
            print(df3)
            print(df.assistant_2)
        elif choice=='2':
            submenu2()
        elif choice=='3':
            submenu3()
        elif choice=='4':
            print('Prompted to main menu')
            quit()
        else:
            print('input a valid option!')
def submenu2():
        print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
        print('!                        DATA VISUALISATION MENU                         !')
        print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
        print('!1) Line Graph of home team goals and away team goals                    !')
        print('!------------------------------------------------------------------------!')
        print('!2) Bar plot of Total Audience on different date and time                !')
        print('!------------------------------------------------------------------------!')
        print('!3) Horizontal Bar plot of Total Audience on different date and time     !')
        print('!------------------------------------------------------------------------!')
        print('!4) Pie Chart of Penalties                                               !')
        print('!------------------------------------------------------------------------!')
        print('!5) Histogram of Assists                                                 !')
        print('!------------------------------------------------------------------------!')
        print('!6) Horizontal Histogram of Most Goals Scored                            !')
        print('!------------------------------------------------------------------------!')
        print('!7) Go Back to the Mainmenu                                              !')        
        print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
    
        h1=int(input('Choose Your Option:'))
        if h1==1:
            plt.plot(abc(htn),htg,color='#59114D',marker='o',markerfacecolor='black',label='Home Team Goals',markersize=5,linewidth=1)
            plt.title('Goal database',fontsize=15)
            plt.xlabel('Home Team Name',fontsize=10)
            plt.ylabel('Number of goals',fontsize=15)
            plt.legend()
            plt.subplots_adjust(left=None, bottom=0.398, right=None, top=None, wspace=None, hspace=None)
            plt.xticks(np.arange(0,64,1),fontsize=10,rotation=90)
            fig = plt.gcf()
            fig.set_size_inches(18.5, 3)

            plt.grid(True)
            plt.show()
            plt.plot(abc(atn),atg,color='#E98A15',marker='o',markerfacecolor='black',label='Away Team Goals',markersize=5,linewidth=1)
            plt.title('Goal database',fontsize=15)
            plt.xlabel('Away Team Name',fontsize=5)
            plt.ylabel('Number of goals',fontsize=15)
            plt.subplots_adjust(left=None, bottom=0.398, right=None, top=None, wspace=None, hspace=None)
            plt.legend()
            fig = plt.gcf()
            fig.set_size_inches(18.5, 3)
            plt.xticks(np.arange(0,64,1),fontsize=10,rotation=90)
            plt.grid(True)
            plt.show()
        elif h1==2:
            c=['#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF']
            plt.bar(htn+" vs "+atn,at,label='Total Audience',color=c)
            plt.subplots_adjust(left=None, bottom=0.564, right=None, top=0.924, wspace=None, hspace=None)
            plt.legend
            plt.xlabel('Match between',fontsize=15)
            fig = plt.gcf() 
            fig.set_size_inches(23, 6)
            plt.xticks(fontsize=10,rotation=90)
            plt.ylabel('Number of persons',fontsize=15)
            plt.title('Match audience',fontsize=20)
            plt.show()
        elif h1==3:
            c=['#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF']
            plt.barh(htn+" vs "+atn,at,label='Total Audience',color=c)
            plt.grid(True)
            plt.legend
            fig = plt.gcf()
            fig.set_size_inches(12, 17)
            plt.yticks(fontsize=5,rotation=0)
            plt.xlabel('Number of persons',fontsize=15)
            plt.ylabel('Match between',fontsize=15)
            plt.title('Match Audience',fontsize=20)
            plt.show()
        elif h1==4: 
            plt.pie(df3['PENALTIES SCORED'],labels=df3['TEAM NAME'],radius=1.2,autopct='%0.0f%%',shadow=True,explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
            plt.show()
            
        elif h1==5:
            plt.hist(df1['ASSISTS'],bins=25,weights=df1['ASSISTS'],width=1,label='Rainfall Levels',edgecolor='#EDD382',color='#FC9E4F')
            plt.xlabel('Number of Assist Goals')
            plt.ylabel('Number of Players')
            plt.axis([0,10,0,17])
            plt.title('Histogram of Assist ')
            plt.show()
        elif h1==6:
            plt.hist(df2['GOALS'],bins=[1,2,3,4,5,6,7],edgecolor='#EFAAC4',color='#FFC4D1',orientation='horizontal')
            plt.xlabel('Number of Players',fontsize=15)
            plt.ylabel('Number of Goals',fontsize=15)
            plt.yticks([1,2,3,4,5,6,7])
            plt.title('Histogram of Goals scored',fontsize=20)
            plt.show()
        elif h1==7:
                     mainmenu()
def submenu3():
    print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
    print('!                             DATA ANAYLSIS MENU                           !')
    print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
    print('!1.Display the name of those 5 home teams which have highest goals         !')
    print('!--------------------------------------------------------------------------!')
    print('!2.Display the name of those 5 home teams which have lowest goals          !')
    print('!--------------------------------------------------------------------------!')
    print('!3.Display the name of those 5 away teams which have highest goals         !')
    print('!--------------------------------------------------------------------------!')
    print('!4.Display the name of those 5 away teams which have lowest goals          !')
    print('!--------------------------------------------------------------------------!')
    print('!5.Display the maximum,minimum,mean,sum of - Penalties                     !')
    print('!--------------------------------------------------------------------------!')
    print('!6.Display the name of those 5 teams which have highest penalties          !')
    print('!--------------------------------------------------------------------------!')    
    print('!7.Display the name of those 5 teams which have lowest penalties           !')
    print('!--------------------------------------------------------------------------!')    
    print('!8.Display the maximum,minimum,mean,sum of - Goals                         !')
    print('!--------------------------------------------------------------------------!')
    print('!9.Display the name of those 5 players who have scored lowest Goals        !')
    print('!--------------------------------------------------------------------------!')
    print('!10.Display the name of those 5 players who have scored highest Goals      !')
    print('!--------------------------------------------------------------------------!')
    print('!11.Display the maximum,minimum,mean,sum of - Assists                      !')
    print('!--------------------------------------------------------------------------!')
    print('!12.Display the name of those 2 players who have scored lowest assists     !')
    print('!--------------------------------------------------------------------------!')
    print('!13.Display the name of those 3 players who have scored highest assists    !')
    print('!--------------------------------------------------------------------------!')
    print('!14.I Quantile,II Quantile and III Quantile of PENALTIES SCORED BY TEAMS   !')
    print('!--------------------------------------------------------------------------!')
    print('!15.Pivot Table - Most Goals Scored Analysis                               !')
    print('!--------------------------------------------------------------------------!')
    print('!16.To export the Football Worldcup 2018 csv file                          !')
    print('!--------------------------------------------------------------------------!')
    print('!17.To return to Main menu                                                 !')
    print('!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
    l=int(input('\nEnter a valid opton for data analysis'))
    if l==1:
        print('Name of those 5 home teams which have highest goals')
        print(df.sort_values('home_team_goals',ascending=True).tail(5))
    elif l==2:
        print('Name of those 5 home teams which have lowest goals')
        print(df.sort_values('home_team_goals',ascending=True).head(5))
    elif l==3:
        print('Name of those 5 away teams which have highest goals')
        print(df.sort_values('away_team_goals',ascending=True).tail(5))
    elif l==4:
        print('Name of those 5 home teams which have lowest goals')
        print(df.sort_values('away_team_goals',ascending=True).head(5))
    elif l==5:
        print('maximum,minimum,mean,sum of - Penalties')
        print(df3.aggregate({'PENALTIES SCORED':['max','min','mean','sum']}))
    elif l==6:
        print('Name of those 5 teams which have lowest penalties')
        print(df3.sort_values('PENALTIES SCORED',ascending=True).head(5))
    elif l==7:
        print('Name of those 5 teams which have highest penalties')
        print(df3.sort_values('PENALTIES SCORED',ascending=True).tail(5))
    elif l==8:
        print('maximum,minimum,mean,sum of - Goals')
        print(df2.aggregate({'GOALS':['max','min','mean','sum']}))
    elif l==9:
        print('Name of those 5 players which have scored lowest goals')
        print(df2.sort_values('GOALS',ascending=True).head(5))
    elif l==10:
        print('Name of those 5 players who have scored highest goals')
        print(df2.sort_values('GOALS',ascending=True).tail(5))
    elif l==11:
        print('maximum,minimum,mean,sum of - ASSISTS')
        print(df1.aggregate({'ASSISTS':['max','min','mean','sum']}))
    elif l==12:
        print('Name of those 2 players who have lowest ASSISTS')
        print(df1.sort_values('ASSISTS',ascending=True).head(2))
    elif l==13:
        print('Name of those 3 players who have highest ASSISTS')
        print(df1.sort_values('ASSISTS',ascending=True).tail(3))
    elif l ==14:
             print('I Quantile,II Quantile and III Quantile of PENALTIES SCORED BY TEAMS')
             print(df3['PENALTIES SCORED'].quantile([0.25,0.50,0.75]))              
    elif l ==15:
             print('Pivot Table - Most Goals Scored By Players Analysis')
             print(df2.pivot_table(index= 'PLAYER NAME', values= "GOALS"))    
    elif l==16:
          df.to_csv()
          df1.to_csv(r'C:\Users\user\Desktop\AB1.csv')
          df2.to_csv(r'C:\Users\user\Desktop\AB2.csv')
          df3.to_csv(r'C:\Users\user\Desktop\AB3.csv')          
    elif l==20:
         mainmenu()
        
mainmenu()


