 %stimuli
Alist={'BOOK','TELEPHONE','BAG','SHY','SURPRISED','BEACH','APPLE','CAR','FOOTBALL','SKIRT'};
Blist={'DOG','RIVER','BREAD','BORED','HAPPY','CINEMA','ORANGE','BUS','SWIMMING','JEANS'};
Clist={'TELEVISION','BICYCLE','DESK','DARING','FRUSTRATED','PUB','GARLIC','SHIP','RUNNING','PYJAMAS'};

s = RandStream.create('mt19937ar','seed',sum(100*clock));
RandStream.setGlobalStream(s);


a=randperm(numel(Alist));randa=Alist(a)
b=randperm(numel(Blist));randb=Blist(b)
c=randperm(numel(Clist));randc=Clist(c)

out={};
out2={};
out3={};
    instr=['In the followings you will see some words one by one. \n \n Your task is to remember something \n \n in connection with this word that happened to you. \n \n You should think about something \n \n that occured over a period of minutes, hours \n \n but not longer than one day. \n \n Try to think of memories older than one week! \n \n When you have the memory in mind press Space! \n \n For an example press Space!'];
    instr2=['Example: if the cue word was "success" \n \n and you press Space as soon as you think of A-Levels \n \n that would be INCORRECT. \n \n Instead you should recall something more specific, \n \n like the moment you opened the letter \n \n informing you about your grades. \n \n If nothing comes to mind, just wait\n \n after 60 seconds, and the program will continue. \n \n If you are ready press Space \n \n and the first word will appear.'];
    valasz=['Please tell the word and your memory to the experimenter briefly \n \n and then press ESCAPE.'];
    name='Please type in your name and then press ESCAPE!';
    name='Please type in your name and then press ESCAPE!';
    gender='Please type in your gender (female\male) \n \n and then press ESCAPE!';
    bday='Please type in your birthday (dd\mm\yyyy) \n \n and then press ESCAPE!';
    med='Do you have any diagnosed psychological problems?  \n \n Do you get any medication? If yes, please specifiy!';
    
    goodby2='The experiment is over. \n \n Thank you for participating! \n \n Press Space and wait for the instructions of the experimenter!' 
    instr3=['In the followings you will have a second task \n \n to complete together with the original task. \n \n Your task will be to say numbers aloud. \n \n  You should say the numbers 1-9, one per second. \n \n A ticking sound will help you keep the peace. \n \n You should say the numbers in a random order. \n \n Try to avoid repeated or familiar sequences! \n \n Press Space for more instructions!'];
    instr4=['After some time a word will appear on the screen, \n \n so while you are saying the numbers keep your eyes on the screen! \n \n When you see the word retrieve a memory! But in the same time \n \n keep up with the random numbers! \n \n When you have a memory in mind press Space! \n \n  You can stop with the numbers then \n \n and tell your memory! \n \n Press Space!'];
    instr5=['Press Space and start \n \n saying the numbers in a random order!'];
   instr6=['In the followings you will have a second task \n \n to complete together with the original task. \n \n Your task will be to search for a letter T among letter L-s. \n \n If you found the letter T press T!\n \n In some cases there are not going to be a T among the L-s \n \n If you look through all the symbols and you think they are all L-s, press L! \n \n Press Escape for more instructions!'];
    instr7=['After some time you will see a word. \n \n Retrieve a memory in connection with this word! But in the same time \n \n keep up with looking for the T-s! \n \n When you have a memory in mind press ESCAPE \n \n  You can stop with the searching then \n \n and write down your memory! \n \n Press Space!'];
    instr8=['In the followings you will see  \n \n just as before and you will have to  \n \n remember memories just as before.  \n \n But from now on you have no second task.  \n \n If you are ready, please press ESCAPE \n \n and the first word appaers!'];
     
     beepDuration = .1; %100ms
    fillerDuration = .9 %(1 /frequency1) - beepDuration;
    beep(1,:) = .5 * MakeBeep(1000, beepDuration, 44100);
    beep(2,:) = beep(1,:);
    filler = zeros(2, 44100*fillerDuration);
    metronome = [beep filler];  
    
try
    
     %intiate screen
   %Screen('Preference','SkipSyncTests', 1);
   HideCursor;
   [ablak,rect]=Screen('OpenWindow',0); 
   Screen('TextSize', ablak, 30);
   
   %participant info
   nameinfo=GetEchoStringnl(ablak,name,200,500);
   Screen('Flip',ablak); 
   WaitSecs(1.000);
   genderinfo=GetEchoStringnl(ablak,gender,200,500);
   Screen('Flip',ablak); 
   WaitSecs(1.000);
   bdayinfo=GetEchoStringnl(ablak,bday,200,500);
   Screen('Flip',ablak); 
   WaitSecs(1.000);
   medinfo=GetEchoStringnl(ablak,med,200,500);
   Screen('Flip',ablak); 
   WaitSecs(1.000);
    
    %instr, cues, memories
   DrawFormattedText(ablak, instr, 'center','center');
   Screen('Flip',ablak); 
   [secs, keyCode, deltaSecs] = KbWait
   WaitSecs(1.000);
   DrawFormattedText(ablak, instr2, 'center','center');
   Screen('Flip',ablak); 
   [secs, keyCode, deltaSecs] = KbWait 
   WaitSecs(1.000);
    
   
   % practice trial single
   
   DrawFormattedText(ablak, '+', 'center','center');   
   Screen('Flip',ablak);
   WaitSecs(0.500);
   DrawFormattedText(ablak,'CAT', 'center','center'); 
   Screen('Flip',ablak);
   time0=GetSecs;
   tEnd=GetSecs+60;
   WaitSecs(1.000);
   DrawFormattedText(ablak, '', 'center','center');   
   Screen('Flip',ablak);
   
   
  while ~KbCheck & GetSecs<tEnd
    WaitSecs(0.001);
  end
  secs=GetSecs;
   reac=secs-time0
   
   val=GetEchoStringnl(ablak,valasz,700,500);
   Screen('Flip',ablak);
   WaitSecs(1.000);
   
   %real trials single
    for k=1:length(randa)
        
         bla=randa{k}
       DrawFormattedText(ablak, '+', 'center','center');   
   Screen('Flip',ablak);
   WaitSecs(0.500);
   DrawFormattedText(ablak, bla, 'center','center'); 
   Screen('Flip',ablak);
   time0=GetSecs;
   tEnd=GetSecs+60;
   WaitSecs(1.000);
   DrawFormattedText(ablak, '', 'center','center');   
   Screen('Flip',ablak);
   
   
  while ~KbCheck & GetSecs<tEnd
    WaitSecs(0.001);
  end
  secs=GetSecs;
   reac=secs-time0;
   
   val=GetEchoStringnl(ablak,valasz,700,500);
   Screen('Flip',ablak);
   WaitSecs(1.000);
     
    %output cell array
   out{k+1,1}=bla;
   out{k+1,2}=reac;
   out
    end
     %creating output
   out{1,1}=nameinfo;
   
   out{1,2}=genderinfo;
   out{1,3}=bdayinfo;
   out{1,4}=medinfo;
   namee = [strtok(nameinfo),'_single'];
   xlswrite(namee, out);
    
    %practice trial visual
    DrawFormattedText(ablak, instr6, 'center','center');
   Screen('Flip',ablak); 
   [secs, keyCode, deltaSecs] = KbWait
   WaitSecs(1.000);
   DrawFormattedText(ablak, instr7, 'center','center');
   Screen('Flip',ablak); 
   [secs, keyCode, deltaSecs] = KbWait 
   WaitSecs(1.000);
    
    bla='DOOR'
  
  [rea,bil,ido,ta]=runVisualSearchen2222(bla,ablak,rect);
    
  val=GetEchoStringnl(ablak,valasz,700,500);
   Screen('Flip',ablak);
   WaitSecs(1.000);
   
   % real trials visual
    for j=1:length(randb)
        
         bla=randb{j}
   [rea,bil,ido,ta]=runVisualSearchen2222(bla,ablak,rect);
    
  val=GetEchoStringnl(ablak,valasz,700,500);
   Screen('Flip',ablak);
   WaitSecs(1.000);
   out2{j+1,1}=bla;
   out2{j+1,2}=rea;
   out2
    end
    %creating output
   nameee = [strtok(nameinfo),'_visual'];
   xlswrite(nameee, out2);
    
    % practice trial rng
    DrawFormattedText(ablak, instr3, 'center','center');
   Screen('Flip',ablak); 
   [secs, keyCode, deltaSecs] = KbWait
   WaitSecs(1.000);
   DrawFormattedText(ablak, instr4, 'center','center');
   Screen('Flip',ablak); 
   [secs, keyCode, deltaSecs] = KbWait 
   WaitSecs(1.000);
    
     DrawFormattedText(ablak, instr5, 'center','center');
   Screen('Flip',ablak);
   [secs, keyCode, deltaSecs] = KbWait;
   DrawFormattedText(ablak, '', 'center','center');
   Screen('Flip',ablak);
   WaitSecs(1.000);
   InitializePsychSound(1); %Initialise sound driver
pahandle = PsychPortAudio('Open'); %Opens default device
PsychPortAudio('FillBuffer', pahandle, metronome); %Sends 'metronome' to the buffer

  PsychPortAudio('Start', pahandle, 0);
   WaitSecs(5);    
           DrawFormattedText(ablak, '+', 'center','center');   
            Screen('Flip',ablak);
            WaitSecs(0.500);
            DrawFormattedText(ablak, 'ROSE', 'center','center'); 
            Screen('Flip',ablak);
            time0=GetSecs;
            tEnd=GetSecs+60;
            WaitSecs(1.000);
            DrawFormattedText(ablak, '', 'center','center');   
            Screen('Flip',ablak);
    
            
            while ~KbCheck & GetSecs<tEnd
            WaitSecs(0.001);
            end
            
            secs=GetSecs;
            reac=secs-time0;
           
            PsychPortAudio('Close',pahandle); 
            val=GetEchoStringnl(ablak,valasz,500,500);
            Screen('Flip',ablak);
            WaitSecs(1.000);
            
   % real trials rng
   for i=1:length(randc)
        
         bla=randc{i}
    DrawFormattedText(ablak, instr5, 'center','center');
   Screen('Flip',ablak);
   [secs, keyCode, deltaSecs] = KbWait;
   DrawFormattedText(ablak, '', 'center','center');
   Screen('Flip',ablak);
   WaitSecs(1.000);
   InitializePsychSound(1); %Initialise sound driver
pahandle = PsychPortAudio('Open'); %Opens default device
PsychPortAudio('FillBuffer', pahandle, metronome); %Sends 'metronome' to the buffer

  PsychPortAudio('Start', pahandle, 0);
   WaitSecs(5);    
           DrawFormattedText(ablak, '+', 'center','center');   
            Screen('Flip',ablak);
            WaitSecs(0.500);
            DrawFormattedText(ablak, bla, 'center','center'); 
            Screen('Flip',ablak);
            time0=GetSecs;
            tEnd=GetSecs+60;
            WaitSecs(1.000);
            DrawFormattedText(ablak, '', 'center','center');   
            Screen('Flip',ablak);
    
            
            while ~KbCheck & GetSecs<tEnd
            WaitSecs(0.001);
            end
            
            secs=GetSecs;
            reac=secs-time0;
           
            PsychPortAudio('Close',pahandle); 
            val=GetEchoStringnl(ablak,valasz,500,500);
            Screen('Flip',ablak);
            WaitSecs(1.000);
   out3{i+1,1}=bla;
   out3{i+1,2}=reac;
   out3
   end 
   DrawFormattedText(ablak, goodby2, 'center','center');
Screen('Flip',ablak);
WaitSecs(5.000);  



   
%creating output
   nameee = [strtok(nameinfo),'_rng'];
   xlswrite(nameee, out3);
   
   Screen('CloseAll');
catch
    Screen('CloseAll');
    rethrow(lasterror)
end  


