import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from functools import reduce
import time
from numpy import genfromtxt
from pathlib2 import Path

totalStart = time.time()

def removeFirstComma(pathToFile):
    linesResult = []
    # Opening the file using the Path function
    file = open(pathToFile, 'r')
    
  
    # Reading and storing the content of the file in
    # a data variable
    lines = file.readlines()
    lineLen = lines[0]
# Replacing the text using the replace function
    if len(lineLen) >= 56:
        
        for line in lines:
            print(len(lineLen))
            line = line.replace(",", "", 1)
            print(line)
            linesResult.append(line)
    
    # Writing the replaced data
    # in the text file
        file = open(pathToFile, 'w')
        file.writelines(linesResult)
        file.close()
        print('Done !')
    return True

def replaceText(search_text, replace_text, pathToFile):
    # Opening the file using the Path function
    file = Path(pathToFile)
  
    # Reading and storing the content of the file in
    # a data variable
    data = file.read_text()
    
    # Replacing the text using the replace function
   
    data = data.replace(search_text, replace_text)
  
    # Writing the replaced data
    # in the text file
    file.write_text(data)
    print('Done !')
    return True
print('Removing  colons')
replaceText(':', '00', './USDJPY5.csv')
print('Removing dots')
replaceText('.', '', './USDJPY5.csv')
print('Removing first comma')
removeFirstComma('./USDJPY5.csv')

date,bid,high,low,ask,volume = np.loadtxt('./USDJPY5.csv', unpack=True,
                            delimiter=',',
                            converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})



print(date)



def percentChange(startPoint, currentPoint):
    try:
        x =((float(currentPoint)-startPoint)/abs(startPoint))*100.00
        if x == 0.0:
            return 0.0000000001
        else:
            return x
    except:
        return 0.0000000001

def patternStorage():
    patStartTime = time.time()
    x = len(avgLine)-60
    y = 31
    while y < x :
        pattern = []
        p1 = percentChange(avgLine[y-30], avgLine[y-29])
        p2 = percentChange(avgLine[y-30], avgLine[y-28])
        p3 = percentChange(avgLine[y-30], avgLine[y-27])
        p4 = percentChange(avgLine[y-30], avgLine[y-26])
        p5 = percentChange(avgLine[y-30], avgLine[y-25])
        p6 = percentChange(avgLine[y-30], avgLine[y-24])
        p7 = percentChange(avgLine[y-30], avgLine[y-23])
        p8 = percentChange(avgLine[y-30], avgLine[y-22])
        p9 = percentChange(avgLine[y-30], avgLine[y-21])
        p10 = percentChange(avgLine[y-30], avgLine[y-20])
        p11 = percentChange(avgLine[y-30], avgLine[y-19])
        p12 = percentChange(avgLine[y-30], avgLine[y-18])
        p13 = percentChange(avgLine[y-30], avgLine[y-17])
        p14 = percentChange(avgLine[y-30], avgLine[y-16])
        p15 = percentChange(avgLine[y-30], avgLine[y-15])
        p16 = percentChange(avgLine[y-30], avgLine[y-14])
        p17 = percentChange(avgLine[y-30], avgLine[y-13])
        p18 = percentChange(avgLine[y-30], avgLine[y-12])
        p19 = percentChange(avgLine[y-30], avgLine[y-11])
        p20 = percentChange(avgLine[y-30], avgLine[y-10])
        p21 = percentChange(avgLine[y-30], avgLine[y-9])
        p22 = percentChange(avgLine[y-30], avgLine[y-8])
        p23 = percentChange(avgLine[y-30], avgLine[y-7])
        p24 = percentChange(avgLine[y-30], avgLine[y-6])
        p25 = percentChange(avgLine[y-30], avgLine[y-5])
        p26 = percentChange(avgLine[y-30], avgLine[y-4])
        p27 = percentChange(avgLine[y-30], avgLine[y-3])
        p28 = percentChange(avgLine[y-30], avgLine[y-2])
        p29 = percentChange(avgLine[y-30], avgLine[y-1])
        p30 = percentChange(avgLine[y-30], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        try:
            avgOutcome = reduce((lambda x, y: x+y), outcomeRange) / len(outcomeRange)
        except Exception as e:
            print(type(e))    
            print(e.args)     
            print(e)
            avgOutcome=0

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)
        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)
        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)
        patternAr.append(pattern)

        featureOutcome = percentChange(currentPoint, avgOutcome)
        performanceAr.append(featureOutcome)
        
        y += 1
    patEndTime = time.time()
    print('Pattern is :', len(patternAr), 'units long')
    print('Pattern storage took :', patEndTime - patStartTime, 'seconds')

def currentPattern():
    cp1 = percentChange(avgLine[-31],avgLine[-30])
    cp2 = percentChange(avgLine[-31],avgLine[-29])
    cp3 = percentChange(avgLine[-31],avgLine[-28])
    cp4 = percentChange(avgLine[-31],avgLine[-27])
    cp5 = percentChange(avgLine[-31],avgLine[-26])
    cp6 = percentChange(avgLine[-31],avgLine[-25])
    cp7 = percentChange(avgLine[-31],avgLine[-24])
    cp8 = percentChange(avgLine[-31],avgLine[-23])
    cp9 = percentChange(avgLine[-31],avgLine[-22])
    cp10 = percentChange(avgLine[-31],avgLine[-21])
    cp11 = percentChange(avgLine[-31],avgLine[-20])
    cp12 = percentChange(avgLine[-31],avgLine[-19])
    cp13 = percentChange(avgLine[-31],avgLine[-18])
    cp14 = percentChange(avgLine[-31],avgLine[-17])
    cp15 = percentChange(avgLine[-31],avgLine[-16])
    cp16 = percentChange(avgLine[-31],avgLine[-15])
    cp17 = percentChange(avgLine[-31],avgLine[-14])
    cp18 = percentChange(avgLine[-31],avgLine[-13])
    cp19 = percentChange(avgLine[-31],avgLine[-12])
    cp20 = percentChange(avgLine[-31],avgLine[-11])
    cp21 = percentChange(avgLine[-31],avgLine[-10])
    cp22 = percentChange(avgLine[-31],avgLine[-9])
    cp23 = percentChange(avgLine[-31],avgLine[-8])
    cp24 = percentChange(avgLine[-31],avgLine[-7])
    cp25 = percentChange(avgLine[-31],avgLine[-6])
    cp26 = percentChange(avgLine[-31],avgLine[-5])
    cp27 = percentChange(avgLine[-31],avgLine[-4])
    cp28 = percentChange(avgLine[-31],avgLine[-3])
    cp29 = percentChange(avgLine[-31],avgLine[-2])
    cp30 = percentChange(avgLine[-31],avgLine[-1])

    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)
    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)
    patForRec.append(cp21)
    patForRec.append(cp22)
    patForRec.append(cp23)
    patForRec.append(cp24)
    patForRec.append(cp25)
    patForRec.append(cp26)
    patForRec.append(cp27)
    patForRec.append(cp28)
    patForRec.append(cp29)
    patForRec.append(cp30)
    
    #print(patForRec)

def patternRecognition():
    predictedOutcome = []
    patFound = 0
    plotPatAr = []
    for eachPattern in patternAr:
        sim1 = 100.00 - abs(percentChange(eachPattern[0], patForRec[0]))
        sim2 = 100.00 - abs(percentChange(eachPattern[1], patForRec[1]))
        sim3 = 100.00 - abs(percentChange(eachPattern[2], patForRec[2]))
        sim4 = 100.00 - abs(percentChange(eachPattern[3], patForRec[3]))
        sim5 = 100.00 - abs(percentChange(eachPattern[4], patForRec[4]))
        sim6 = 100.00 - abs(percentChange(eachPattern[5], patForRec[5]))
        sim7 = 100.00 - abs(percentChange(eachPattern[6], patForRec[6]))
        sim8 = 100.00 - abs(percentChange(eachPattern[7], patForRec[0]))
        sim9 = 100.00 - abs(percentChange(eachPattern[8], patForRec[8]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9], patForRec[9]))

        sim11 = 100.00 - abs(percentChange(eachPattern[10], patForRec[10]))
        sim12 = 100.00 - abs(percentChange(eachPattern[11], patForRec[11]))
        sim13 = 100.00 - abs(percentChange(eachPattern[12], patForRec[12]))
        sim14 = 100.00 - abs(percentChange(eachPattern[13], patForRec[13]))
        sim15 = 100.00 - abs(percentChange(eachPattern[14], patForRec[14]))
        sim16 = 100.00 - abs(percentChange(eachPattern[15], patForRec[15]))
        sim17 = 100.00 - abs(percentChange(eachPattern[16], patForRec[16]))
        sim18 = 100.00 - abs(percentChange(eachPattern[17], patForRec[10]))
        sim19 = 100.00 - abs(percentChange(eachPattern[18], patForRec[18]))
        sim20 = 100.00 - abs(percentChange(eachPattern[19], patForRec[19]))

        sim21 = 100.00 - abs(percentChange(eachPattern[20], patForRec[20]))
        sim22 = 100.00 - abs(percentChange(eachPattern[21], patForRec[21]))
        sim23 = 100.00 - abs(percentChange(eachPattern[22], patForRec[22]))
        sim24 = 100.00 - abs(percentChange(eachPattern[23], patForRec[23]))
        sim25 = 100.00 - abs(percentChange(eachPattern[24], patForRec[24]))
        sim26 = 100.00 - abs(percentChange(eachPattern[25], patForRec[25]))
        sim27 = 100.00 - abs(percentChange(eachPattern[26], patForRec[26]))
        sim28 = 100.00 - abs(percentChange(eachPattern[27], patForRec[27]))
        sim29 = 100.00 - abs(percentChange(eachPattern[28], patForRec[28]))
        sim30 = 100.00 - abs(percentChange(eachPattern[29], patForRec[29]))

        howSim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+
                  sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+
                  sim21+sim22+sim23+sim24+sim25+sim26+sim27+sim28+sim29+sim30)/30
        if howSim > 55:
            patFound = 1
            plotPatAr.append(eachPattern)
            predAr = []
            if patFound == 1:
                for eachPatt in plotPatAr:
                    futurePoints = patternAr.index(eachPatt)

                    if performanceAr[futurePoints] > patForRec[28]:
                        pcolor = '#24bc00'
                        predAr.append(1.000)
                    else:
                        pcolor = '#d40000'
                        predAr.append(-1.000)

                    plt.plot(xp, eachPatt)
                    predictedOutcome.append(performanceAr[futurePoints])
                    plt.scatter(50, performanceAr[futurePoints], c=pcolor, alpha=.3)
                    plt.plot(xp, patForRec, linestyle=':', color='r')
                realOutcomeRange = allData[toWhat+20:toWhat+30]
                realAvgOutcome = reduce(lambda x, y: x+y, realOutcomeRange) / len(realOutcomeRange)
                realMovement = percentChange(allData[toWhat], realAvgOutcome)
                predictedAvgOutcome = reduce(lambda x, y: x+y, predictedOutcome) / len(predictedOutcome)
                plt.scatter(60, realMovement, c='#000000', alpha=.3)
                plt.scatter(55, predictedAvgOutcome, c='#000000', alpha=.3)

                print(predAr)
                predAvg = reduce(lambda x, y: x+y, predAr) / len(predAr)
                print(predAvg)
                if predAvg < 0:
                    print('Drop prediction. ')
                    print(patForRec[29])
                    print(realMovement)
                    if realMovement < patForRec[29]:
                        accuracyAr.append(100)
                    else:
                        accuracyAr.append(0)
                if predAvg > 0:
                    print("Rise predicition")
                    print(patForRec[29])
                    print(realMovement)
                    if realMovement > patForRec[29]:
                        accuracyAr.append(100)
                    else:
                        accuracyAr.append(0)


def graphRawFX():
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)    
    plt.subplots_adjust(bottom=.23)
    plt.grid(True)
    #plt.show()

dataLenght = int(bid.shape[0])
print ('Data lenght is ', dataLenght, 'unit long.')

toWhat = 4030
allData = ((bid+ask)/2)
accuracyAr = []
samps = 0

while toWhat < dataLenght:
    xp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    avgLine = allData[:toWhat]
    patternAr = []
    patForRec = []
    performanceAr = []
    patternStorage()
    currentPattern()
    patternRecognition()


    totalTime = time.time() - totalStart
    print('Compute Time :', totalTime, 'sec.')

    samps+=1
    toWhat += 1
    plt.show()
    accuracyAvg = reduce(lambda x, y: x+y, accuracyAr) / len(accuracyAr)
    print('Backtested Accuracy is :',str(accuracyAvg) + '% after '  ,samps,' samples')

