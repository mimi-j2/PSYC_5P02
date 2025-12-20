%{
everything in here is a comment 
%}

%path - the matlab files that are in the path currently - matlab will only know that files in the path exists - good to add pathways that script is conginent on %

%{
to add files in the path:
    - Use GUI to set path
    - run the command addpath(genpath('~/Documents/')) 
    - If you add file startup.m to run it eveyrtime you open it 
%}

%%

%%REVIEW OF LAST WEEK%%

%definining variables use square brackets and spaces and columsn seperate columns and semicolons seperate rows%
%rows have to have the same amount of items in each row%

myVar = [1 2 3 4 5; 6 7 8 9 10]

%plots in matlab work same as myplotlib in which you have a plot, figure

% indexing is done with row and then column
%start at 1 in matlab, while start at 0 in python

myVar(2, 3)

%indexing the WHOLE first row
myVar(1,:)

%for yhe first row, go to 1 to 5 by 2
myVar(1, 1:2:5)

%apostrophe transposes the variable - flipes rows and columsn
newVar = myVar'

%needs to be a rectangler matrix so if you add a value into a place like
%done below it will add a 0 in row 1 so the rows have the same number of
%values in each row
myVar(2, 6) = 11

%replaces the var in row 1 at column 6 with NaN
myVar(1, 6) = NaN

%to get rid of a column or value need to use [] brackets- replacing it with
%empty

%this removes the sixth column
myVar(:, 6) = []

%this saves the variables myVar and newVar to myFiles
save myFiles myVar newVar

%loads the vairables from myFiles to use
load myFiles.mat

%MatLab does Matrix math (does it with the whole matrix)
% need to add . to make it item wise

myVar / newVar'

myVar ./ newVar'

%this returns the help file to see what a function does
help randperm

%%

%Logical functions - most of them are similar to Python %

%TRUE or FALSE (boolen)

%this is similar to python where it is asking is 1 == 0, if True returns
%1 and if False returns 0
True = 1 == 1

False = 1 == 4

% There are some differences 
% OR is |
% AND is &

%%

%Matlab does not care about indentation or spaces
%in If statements start with an if and ends with an end

%this is to make sure it is random each time and starts with a different
%SEEd each time
rng('shuffle');

% the ; suppresses the print (so it does not print in the command window)
a = rand();
myVar = 1;

if a < 0.3 %if the value a is less than .33 (if it returrns true)
    b = a.^2; %square
elseif a >= 0.33 && a <= .66
    another = true; %creates a variable called another that is equal to true if the elseif statement is true
    b = 0;
else % if everything returned false
    b = a.^.5;  %squareroot
end; %the end of my first if statement

%%

var= 11:21;

%length is the range (like range in python)
for i = 1:length(var) %loop through elements in that vector, loop through the locations of that specific variable
    
    i

end

%%

%tic toc functions evaluate how long it takes  to go between tic and toc

%parfor can run jobs in parallel to analyze multiple subjects at a time -
%allocates different cores to different loops - speeds up how long it takes
%to run those loops


%%

%this creates a mask
setSize = [2 2 4 4 2 6 6 4 2 6 6 4];
ssFour = [setSize == 4]


%%

%try - catch - it will try something and if it does not work it will do
%something else


%%

%spaces count as spaces strings as considered char in Matlab
myText = ('This is some text')

myText(10)

%can change text into ascii values 
%double returns the values which are called ascii values- each specific
%character is assigned a specific number and these are the ascii values
double(myText)

%single quotes return a vector of logical array 
%single quotes are conisderd a collection of chars
'apples' == 'applez'

%double quotes compares the entire string to each other
%double quotes is a 1 by 1 string = a string is a collection of chars but
%consisered one thing
"apples" == "applez"

%%

%sprint is the string print function is where it will format it in a string
%and print it (which could be used with input function)

%fid = fprintf(fid, '%3.2f\t', rr)


%%

%cells are there own thing in matlab - this below would be a 1 by 2 cell
%cells are similar to spreadhseets where each cell contains some elements
%of a variable
%in cells the values of each array do not need to be equal
cell1 = {[1 2 3 4], [1 2 3 4 5 6]}

%cells are indexed with curly brackets instead of round brackets
cell1{1}

%in cell1 index the first cell and index in that element of the array
%has to be cury brackets for cell number and round brackets for indexing in
%specific place in that cell
cell1{1}(5)

%can mix and match like dataframes and have strings, and numbers together
cell1{3} = "does this work?"

%% structures


%this creates a structure with currently only one field which is subject
%which contained within subject is a 1x1 structure
%inside subject is a field called block which is 1 1x2 structure
%inside that is a 1x50 structrue called trial

%each level is a containment box that can have different levels inside it
%or variables
data2.subject(1).block(2).trial(50).RT = .765

data2.title = 'y = sin(x)'


data.rt = [0.9, 1.2]
data.subject = "SME"

data.subject(2) = 'MME'
%data is the structure, the 2nd variable for subject (subject is our
%channel)
%creates a new subject called MME
data(2).subject = 'MME'

data(:).subject %this shows you all of your subject



