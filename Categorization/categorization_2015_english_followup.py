#Imports
from psychopy import visual, core, event, gui
import time, random, os
from random import shuffle

# Participant name
exp_info = {'participant':'participant_name', 'date_of_birth':'date', 'gender': 'gender', 'training stimuli directory': 'C:\\', 'logfile directory':'C:\\' }


# Present a dialogue to change parameters
dlg = gui.DlgFromDict(exp_info, title='Categorization')
if not dlg.OK: # quit on Cancel
    core.quit()

# Stimuli
kodok = ["0000v1", "0000v2", "0000v3", "0001v1", "0001v2", "0001v3", "0002v1", "0002v2", "0002v3", "0010v1", "0010v2", "0010v3", "0011v1", "0011v2", "0011v3", "0012v1", "0012v2", "0012v3", "0020v1", "0020v2", "0020v3", "0021v1", "0021v2", "0021v3", "0022v1", "0022v2", "0022v3", "0100v1", "0100v2", "0100v3", "0101v1", "0101v2", "0101v3", "0102v1", "0102v2", "0102v3", "0110v1", "0110v2", "0110v3", "0111v1", "0111v2", "0111v3", "0112v1", "0112v2", "0112v3", "0120v1", "0120v2", "0120v3", "0121v1", "0121v2", "0121v3", "0122v1", "0122v2", "0122v3", "0200v1", "0200v2", "0200v3", "0201v1", "0201v2", "0201v3", "0202v1", "0202v2", "0202v3", "0210v1", "0210v2", "0210v3", "0211v1", "0211v2", "0211v3", "0212v1", "0212v2", "0212v3", "0220v1", "0220v2", "0220v3", "0221v1", "0221v2", "0221v3", "0222v1", "0222v2", "0222v3", "1000v1", "1000v2", "1000v3", "1001v1", "1001v2", "1001v3", "1002v1", "1002v2", "1002v3", "1010v1", "1010v2", "1010v3", "1011v1", "1011v2", "1011v3", "1012v1", "1012v2", "1012v3", "1020v1", "1020v2", "1020v3", "1021v1", "1021v2", "1021v3", "1022v1", "1022v2", "1022v3", "1100v1", "1100v2", "1100v3", "1101v1", "1101v2", "1101v3", "1102v1", "1102v2", "1102v3", "1110v1", "1110v2", "1110v3", "1111v1", "1111v2", "1111v3", "1112v1", "1112v2", "1112v3", "1120v1", "1120v2", "1120v3", "1121v1", "1121v2", "1121v3", "1122v1", "1122v2", "1122v3", "1200v1", "1200v2", "1200v3", "1201v1", "1201v2", "1201v3", "1202v1", "1202v2", "1202v3", "1210v1", "1210v2", "1210v3", "1211v1", "1211v2", "1211v3", "1212v1", "1212v2", "1212v3", "1220v1", "1220v2", "1220v3", "1221v1", "1221v2", "1221v3", "1222v1", "1222v2", "1222v3", "2000v1", "2000v2", "2000v3", "2001v1", "2001v2", "2001v3", "2002v1", "2002v2", "2002v3", "2010v1", "2010v2", "2010v3", "2011v1", "2011v2", "2011v3", "2012v1", "2012v2", "2012v3", "2020v1", "2020v2", "2020v3", "2021v1", "2021v2", "2021v3", "2022v1", "2022v2", "2022v3", "2100v1", "2100v2", "2100v3", "2101v1", "2101v2", "2101v3", "2102v1", "2102v2", "2102v3", "2110v1", "2110v2", "2110v3", "2111v1", "2111v2", "2111v3", "2112v1", "2112v2", "2112v3", "2120v1", "2120v2", "2120v3", "2121v1", "2121v2", "2121v3", "2122v1", "2122v2", "2122v3", "2200v1", "2200v2", "2200v3", "2201v1", "2201v2", "2201v3", "2202v1", "2202v2", "2202v3", "2210v1", "2210v2", "2210v3", "2211v1", "2211v2", "2211v3", "2212v1", "2212v2", "2212v3", "2220v1", "2220v2", "2220v3", "2221v1", "2221v2", "2221v3", "2222v1", "2222v2", "2222v3", "0000v4", "0001v4", "0002v4", "0010v4", "0011v4", "0012v4", "0020v4", "0021v4",  "0022v4", "0100v4",  "0101v4", "0102v4", "0110v4", "0111v4", "0112v4", "0120v4", "0121v4", "0122v4", "0200v4", "0201v4",  "0202v4", "0210v4", "0211v4", "0212v4", "0220v4", "0221v4", "0222v4", "1000v4", "1001v4", "1002v4",  "1010v4", "1011v4", "1012v4", "1020v4", "1021v4", "1022v4", "1100v4", "1101v4", "1102v4", "1110v4", "1111v4", "1112v4", "1120v4", "1121v4", "1122v4", "1200v4", "1201v4", "1202v4", "1210v4", "1211v4", "1212v4", "1220v4", "1221v4", "1222v4", "2000v4", "2001v4", "2002v4", "2010v4", "2011v4", "2012v4", "2020v4", "2021v4", "2022v4", "2100v4", "2101v4", "2102v4", "2110v4", "2111v4", "2112v4", "2120v4", "2121v4", "2122v4", "2200v4", "2201v4", "2202v4", "2210v4", "2211v4", "2212v4", "2220v4", "2221v4", "2222v4"]
nevek=[]
for i in range(1,325):  
    nevek.append(str(i))
dino_dict={} # a dictionary with entries like key:3 (end of the name of the stimuli file), value:0000v3 (code of the dino)

for i in range(0,len(kodok)):
    dino_dict[kodok[i]]=nevek[i]


output=exp_info['participant']
temp_path = exp_info['logfile directory']+ '\\' + output + '.txt'
lines=[]
with open(temp_path) as f:
    lines.extend(f.readline() for i in xrange(2))


tul_egyA=lines[0][0]
tul_egyB=lines[1][0]
tul_kettoA=lines[0][1]
tul_kettoB=lines[1][1]
tul_haromA=lines[0][2]
tul_haromB=lines[1][2]
tul_negyA=lines[0][3]
tul_negyB=lines[1][3]

    
# lists which are going to be needed
ffpA=[]
ffpA_transfer=[]
ctpA=[]
pA=[]
ffpB=[]
ffpB_transfer=[]
ctpB=[]
pB=[]

for kod in kodok: # going through every code
    a=0 # counters for how many A and B features each exemplar has
    b=0
    if tul_egyA==kod[0]: # if the first feature is like an A exemplar, the A counter goes up one
        a=a+1
    elif tul_egyB==kod[0]: # if the first feature is like an B exemplar, the B counter goes up one
        b=b+1
    if tul_kettoA==kod[1]: # second feature
        a=a+1
    elif tul_kettoB==kod[1]:
        b=b+1
    if tul_haromA==kod[2]: # third feature
        a=a+1
    elif tul_haromB==kod[2]:
        b=b+1
    if tul_negyA==kod[3]: # forth feature
        a=a+1
    elif tul_negyB==kod[3]:
        b=b+1
    if a==2 and b==1 and kod[-1]!='4': # if the exemplar has 2 A and 1 B feature and it's not a version4 than it is added to far from prototype category A list
        ffpA.append(dino_dict[kod])
    elif a==2 and b==1 and kod[-1]=='4': # if the exemplar has 2 A and 1 B feature and it's a version4 than it is added to far from prototype transfer category A list
        ffpA_transfer.append(dino_dict[kod])
    elif a==3 and kod[-1]!='4': # if the exemplar has 3 A features and it's not a version4 than it is added to close to prototype category A list
        ctpA.append(dino_dict[kod])
    elif a==4 and kod[-1]!='4': # and so on
        pA.append(dino_dict[kod])
    elif b==2 and a==1 and kod[-1]!='4':
        ffpB.append(dino_dict[kod])
    elif b==2 and a==1 and kod[-1]=='4':
        ffpB_transfer.append(dino_dict[kod])
    elif b==3 and kod[-1]!='4':
        ctpB.append(dino_dict[kod])
    elif b==4 and kod[-1]!='4':
        pB.append(dino_dict[kod])
ffp=ffpA+ffpB # list of all ffp exemplars
ffp_transfer=ffpA_transfer+ffpB_transfer # list of all transfer exemplars
ctp=ctpA+ctpB # list of all ctp exemplars
p=pA+pB # list of all p exemplars


# list that are going to be needed
feedback = ['Correct', 'Wrong']
test_answers = []
test_RTs=[]

#Window
win = visual.Window([1200,600], allowGUI=True, fullscr=True, waitBlanking=True, color='black', monitor='testMonitor', units='pix')
trial_clock = core.Clock()


#test
instruction_text = visual.TextStim(win, height=20, color = 'white')
instruction_text.setText("Welcome back! In the followings you will see the same type of creatures as you did last time. \n Your task is the same: press button A or L corresponding the type of the creatures!\n Your reaction time will be registered so be as fast and as accurate as possible. \n If you are ready press Enter!")
instruction_text.draw()
win.flip()
event.waitKeys(keyList=['return'])

#test stimuli
teststim=ffp+ctp+p+ffp_transfer # a list of all stimuli 
teAB=random.sample(teststim,len(teststim)) # randomizing the list
test_presented=[]

for dinoo in teAB: # goes through the randomized test stimuli list
	trial_clock.reset()
	stimuli=visual.SimpleImageStim(win, exp_info['training stimuli directory'] + '\stim15_1.jpg') # selects a random stimuli which will be changed
	stimuli.setImage(exp_info['training stimuli directory'] + '\stim15_'+ dinoo + '.jpg') # sets the stimuli
	stimuli.draw()
	win.flip()
	press=event.waitKeys(keyList=['a','l'])
	RT = trial_clock.getTime()
	test_RTs.append(RT) # logs RT
	if (((press[0] == 'a') & ((dinoo in ffpA) |  (dinoo in ctpA) | (dinoo in pA))) | ((press[0] == 'l') & ((dinoo in ffpB) |  (dinoo in ctpB)| (dinoo in pB)))): # checks if answer was correct
		test_answers.append('1') # logs hits
	else:
		test_answers.append('0') # logs misses


#log
ffp_test=[]
ffp_answers=[]
ffp_rt=[]
ffp_order=[]
ffp_transfer_test=[]
ffp_transfer_answers=[]
ffp_transfer_rt=[]
ffp_transfer_order=[]
ctp_test=[]
ctp_answers=[]
ctp_rt=[]
ctp_order=[]
p_test=[]
p_answers=[]
p_rt=[]
p_order=[]

for i in range(len(teAB)): # goes through the randomized test stimuli list
    if  teAB[i] in ffp: # checks is the exemplar was a ffp
        ffp_test.append(teAB[i]) # logs its code
        ffp_answers.append(float(test_answers[i])) # logs if it was a hit
        ffp_rt.append(float(test_RTs[i])) # logs RT
        ffp_order.append(i+1) # logs the presentation order (+1 because the counter starts from 0)
    elif  teAB[i] in ffp_transfer: # checks is the exemplar was a ffp transfer
        ffp_transfer_test.append(teAB[i])
        ffp_transfer_answers.append(float(test_answers[i]))
        ffp_transfer_rt.append(float(test_RTs[i]))
        ffp_transfer_order.append(i+1)
    elif teAB[i] in ctp: # checks is the exemplar was a ctp
        ctp_test.append(teAB[i])
        ctp_answers.append(float(test_answers[i]))
        ctp_rt.append(float(test_RTs[i]))
        ctp_order.append(i+1)
    elif teAB[i] in p: # checks is the exemplar was a p
        p_test.append(teAB[i])
        p_answers.append(float(test_answers[i]))
        p_rt.append(float(test_RTs[i]))
        p_order.append(i+1)

# puts together the presentation order, the code, the hit and the RT for each test exampler arranged by type (ffp, ffp_transfer, ctp, p)
log_ffp = zip(ffp_order, ffp_test, ffp_answers, ffp_rt)
log_ffp_transfer = zip(ffp_transfer_order, ffp_transfer_test, ffp_transfer_answers, ffp_transfer_rt)
log_ctp = zip(ctp_order, ctp_test, ctp_answers, ctp_rt)
log_p = zip(p_order, p_test, p_answers, p_rt)

# calculates averages and std-s for the results
import numpy as np 
ffp_hit=np.mean(ffp_answers)
ffp_reac=np.mean(ffp_rt)
ffp_transfer_hit=np.mean(ffp_answers)
ffp_transfer_reac=np.mean(ffp_rt)
ctp_hit=np.mean(ctp_answers)
ctp_reac=np.mean(ctp_rt)
p_hit=np.mean(p_answers)
p_reac=np.mean(p_rt)

# Making log files
file_name = exp_info['participant'] + 'followup'
temp_path = exp_info['logfile directory']+ '\\' + file_name + '.txt'
file = open(temp_path, 'w')

file.write(tul_egyA + tul_kettoA +tul_haromA + tul_negyA + '\n')
file.write(tul_egyB + tul_kettoB +tul_haromB + tul_negyB + '\n')
file.write('Fent A prototipues, lent B prototipus' + '\n')
file.write('\n')

file.write('Gender:'+ exp_info['gender']+', Date of birth:' + exp_info['date_of_birth']+ '\n')

file.write('Results'+ "\n")
file.write('Your results for prototypes:'+ str(p_hit) + '%' + ' '+str(p_reac) + ' sec'  "\n")
file.write('Your results for close to prototype exemplars:'+ str(ctp_hit) + '%'+ ' ' + str(ctp_reac) + ' sec'"\n")
file.write('Your results for far from prototype exemplars:'+ str(ffp_hit) + '%'+ ' ' + str(ffp_reac) + ' sec'"\n")
file.write('Your results for far from prototype transfer exemplars:'+ str(ffp_transfer_hit) + '%'+ ' ' + str(ffp_transfer_reac) + ' sec'"\n")

file.write('\n')
file.write('Order, Stimuli, Hit, RT'+ "\n")
file.write('Test - FFP'+ "\n")
for order, name, correct, time in log_ffp:
    dinooo=(dino_dict.keys()[dino_dict.values().index(name)])
    file.write("\n".join([" %s %s %s %s" % (order, dinooo, int(correct), time)]) + "\n")
file.write('Test - FFP_transfer'+ "\n")
for order, name, correct, time in log_ffp_transfer:
    dinooo=(dino_dict.keys()[dino_dict.values().index(name)])
    file.write("\n".join([" %s %s %s %s" % (order, dinooo, int(correct), time)]) + "\n")
file.write('Test - CTP'+ "\n")
for order, name, correct, time in log_ctp:
    dinooo=(dino_dict.keys()[dino_dict.values().index(name)])
    file.write("\n".join([" %s %s %s %s" % (order, dinooo, int(correct), time)]) + "\n")
file.write('Test - P'+ "\n")
for order, name, correct, time in log_p:
    dinooo=(dino_dict.keys()[dino_dict.values().index(name)])
    file.write("\n".join([" %s %s %s %s" % (order, dinooo, int(correct), time)]) + "\n")



file.close()








	
	




