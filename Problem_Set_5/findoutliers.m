%function that removes outlier RTS and produces a clean list of RTs (cleanedRTs) that
%fit within 2 sds of the mean, 
% produces the removed outlier rt list - removedRTs
%total counter of how many times it had to iterate - counter
%total number removed outliers - total_removed
function [removedRTs, cleanedRTs, counter, total_removed] = findoutliers(inputArray)

%data to manipulate
data = inputArray;

%initating empty list for removed RTS
removedRTs = [];

%counts how many iterations of outlier removal there were
counter = 0;

%seeting our standard deviation limit
sd = 2;

%while loop to remove outliers and put them in a list and clean output
while true

    %setting the mean to the data mean
    Actual_mean = mean(data);

    %setting the standard deviation units to the datas standard deviaiton
    stdRT = std(data);

    %calculating the lower bound of 2 sds below
    lower_bound = Actual_mean - sd * stdRT;

    %calculating the upper bound of 2 sds above
    upper_bound = Actual_mean + sd * stdRT;

    %the cleaned Rts are data that is within the lower bound and upper
    %bound of the data
    cleanedRTs = data(data >= lower_bound & data <= upper_bound);

    %outliers are the data points that are below the lower bound and above
    %the upper bound
    outliers = data(data < lower_bound | data > upper_bound);

    %removed RTS takes the previous RT list and combines it with the
    %outliers that are found, so it builds on top of each other as it will
    %always take the last list and add onto it with the outlier additon
    %its an array made up of previously removed and this iteration removed
    removedRTs = [removedRTs; outliers];

    %adds 1 to the counter for every iteration
    counter = counter + 1;
    %if the length of cleaned rts is = to the length of the data (means no
    %outliers were removed this iteration becuase there was none left
    if length(cleanedRTs) == length(data)
        %count total removed outliers
        total_removed = length(removedRTs)
        %break from loop when there no more outliers to remove
        break;
     %ends if statement
    else
    %if there were not teh same size means outliers were removed so make
    %the data = to the clean data and try again
        data = cleanedRTs;
        continue; %break loop but continue in while loop
    end %end if statement
end %end while statement

end %end function