%% Problem 1

%getting into practice of shuffling my seed to get a new seed each time
rng('shuffle');

%inital rts
RT = [520 498 601 1200 450 475 3000 510 490];

%returns a matrix of all the values lower or equal to 1500
RT_clean = RT(RT <= 1500)

%calculate the mean of the clean RTs
mean_RT = mean(RT_clean)

%calculate the median of the clean RTs
median_RT = median(RT_clean)

%number of trials removed - taking the length of RT matrix and subtracting
%with the length of the clean RT matrix
removed_trials = length(RT) - length(RT_clean)

%% Probelm 2

%stimulus intensity - generating random integers from 1 to 100 to determine stimulus intensity
data = randi([1, 100],10, 1)

%conditions - randomly set with 1 for low load and 2 for high load
data(1:end, 2) = randi([1, 2], 10, 1)

%response - which is random integers 1 or 2
data(1:end, 3) = randi([1,2], 10, 1)

%for all the rows in column 2 if the number is equal to 2 produce 1 and if
%it is equal to 1 produce 0
% Online Help: https://www.mathworks.com/matlabcentral/answers/694515-searching-a-table-for-rows-that-meet-specific-criteria
highLoadlogical = data(:, 2) == 2

%mask the data and only put the rows of data that are true in
%highloadLogical in this matrix for only the high load data
%using the logic to index to the original array to the areas that were true
highLoadData = data(highLoadlogical, :)

%taking the mean of stimulus intensity (in column 1) only for the high load
%condition
meanHigh = mean(highLoadData(:, 1))

%doing the same logic technique for low load condition, so this returns a
%logical of true for low load and false for high load
lowLoadlogical = data(:, 2) == 1

%indexes to all the data that has true for low load logical and creates a
%seperate matrix just for low load data
lowLoadData = data(lowLoadlogical, :)

%takes the mean of stimulus intensity (in column 1) for the low load
%condition
meanLow = mean(lowLoadData(:, 1))

%% Problem  3

%criterion to compare to stimulus intensity
criterion = 50;

%for the length of data (so each row in data)
for i = 1:length(data)
    %if the number is row i (current loop number) and column 3 (response column) is equal to 1
    %and number in row i and column 1 (stimulus intensity) is smaller than
    %criterion (50)
    if data(i, 3) == 1 && data(i, 1) < criterion
        %display Correct
        disp('Correct');
    %if the number in row i and column 3 is equal to 2
    %and the number in row i and column 1 is larger or equal to criterion
    elseif data(i, 3) == 2 && data(i, 1) >= criterion
        %display Correct
        disp('Correct');
    %if it is anything else
    else
        %display incorrect
        disp('Incorrect');
    end; %ends the if statement
end; %ends the for loop


%% Problem 4

%shortG format: https://www.mathworks.com/matlabcentral/answers/222584-how-to-avoid-powers-of-10-i-e-1-0e-03-in-answers
format shortG
meanRT = 700

sd = 2
%Online help: https://www.mathworks.com/help/matlab/math/random-numbers-with-specific-mean-and-variance.html
%Additional online help: https://www.mathworks.com/matlabcentral/answers/424853-how-to-add-uniform-noise-with-given-range

%to get non-uniform random variaty multiplying the randn by a number (which
%could also be random could help add randomness and check that it is
%actually working but for this case I am not using this because the
%quetsion is asking for random unfiorm added noise
%dirty_RTs = abs(700.*randn(100,1) + meanRT)

%generate random numbers with the mean around 700ms - making it absoulte to
RTs = meanRT + randn(100,1) 

noise = unifrnd(-400, 400, 100, 1); %generating uniform noise to add to my generated RTs, -400 and adding 400
RTs = RTs + noise % Add uniform noise to the generated RT values, can't have negative because 400 is lower than 700

[removedrts cleanedRts iterations total_removed] = findoutliers(RTs) %using my function (in another matlab sheet to generate my removed outliers (in which there will be none because it is uniform and my cleaned RT array)

%mean of cleaned list
clean_mean = mean(cleanedRts)

%message where it tells you the final mean, number of iterations, and
%number of outliers removed 
%.0f formats the mean as a number iwth two decimel places
message = sprintf('The final RT mean is: %.2f. \nThe number of iterations to clean the list was: %d. \nThe number of outliers removed was: %d. ', clean_mean, iterations, total_removed);

%displays the message on screen
disp(message); % Displays: the message above

%% Problem 5

%loading the data into matlab
load("C:Users\miche\OneDrive\Desktop\PSYC 5P02\experiment_data.mat")

fprintf('participants id is: %s \n',data(1).participant) %this prints the participant ID which is P001

%displaying the length of the trials (basically how many trials)
disp(length(data.trials))

%gets the mean of the rts from all of the trials recorded for the 1st
%participant and adds it to the new field mean_RT for that participants
%whole trials
data(1).mean_RT = mean([data(1).trials.rt])


%NOTE I do not know if yes is correct and no is incorrect but that is how I
%am interpertuting it becaue i do nto know what the conditions are and
%whats considered correct or incorrect in those conditions

%used chatGPT for the strcmp function as I did not know how to do a logic
%boolen for if statements using strings
%strcmp is for comparing strings and checks whether two strings are exactly
%the same (identical) and produces a true or false value depending on if its exactly teh same or not, this compares the whole string while == compares each character
%for each row in the trial structure
for i = 1:length(data(1).trials)
    %check and see if response is yes and if it is yes
    if strcmp(data(1).trials(i).response, 'yes')
        %set accuracy (creates a new column the first time) to 1 for that
        %row
        %1 means correct
        data(1).trials(i).accuracy = 1
     %if not set accuracy for that row to 0 meaning incorrect
    else
        data(1).trials(i).accuracy = 0
     %ending if statement
    end
%ending for loop
end

%to get the average accuracy take the mean from the all the rows of the
%newly created column accuracy that are either 1 (correct) or 0 (incorrect)
%and adds it to a new field called accuracy for the average accuracy for
%that participants whoel trials
data(1).accuracy = mean([data(1).trials.accuracy])

%creating a new participant called P002
data(2).participant = 'P002';

%creating a random array of 1 column and 10 rows of random rts from 480 -
%600 ms
P2_Rt = 480 + (600-480).*rand(10,1);

%for the length of P2_Rt which is 10
for t = 1:length(P2_Rt)
    %in the 2nd participants data in the trial fireld put one of the random
    %numbers that was generated from P2_Rt into trials in the rt column
    data(2).trials(t).rt = P2_Rt(t);
end %end for statement



