% first number in a list is a 1, unlike python where it is a 0
% Matlab does not care about spacing - instead it uses the end keyword to terminate blocks of code
%Matlab treats everytjing as an arry while Python treats eveyrthing as a
%object

%Vectors and arrays are contained in square brackets- you do not need to
%seperate the values with commas like in Python but you can - its the same
%thing
%if you put semicolons it will not print the outcome of your code to the
%terminal but if you don't it will return eveyerthing you make
a = [1 2 3 4 5];
b = [1, 2, 3, 4, 5];

%clc clears the command window

%%
%if you don;t create a variable to assign a value to the value will be
%assigned to ans
1 + 1 %assigned to ans as it is not assigned to a varibale so Matlab makes one up (ans)

%% 
%This is a new section - %% is a section break

%%
%if you write your file name it will run the whole m (matlab file) as if it is a
%function
lecture8

%%
%whos tells you what your variables are and details about those variables
whos

%%
%can clear specific variables from your workspace
clear ans

%%
%semicolumns sepereate the rows
%commas seperate the columns
%follows a row by column structure
d = [1; 2; 3; 4; 5]

%%
%row by column size matrix
m = [1 2; 3 4; 5 6;]

%matrices must be retangular, so needs the same number of elements in each
%row/column

%%
%can use NaN for missing values
%NaN means not a number - NaN is quasinumertical it is not processed as
%text(string)
n = [1 2; NaN 4; 5 NaN]

%%
%indexing in Matlab is done with round brackets
a(3)
%returns the third value in my matrix a

n(3)
%goes down row by column if indexed individual elements

n(3, 1)
%goes row by column - so three down and 1 over
%(rows, columns)

%%
%the brakcets takes all the elelmenst in that vector in that colums
%so taking from the first column the 1st and 3rd item in those rows
n([1 3], 1)

%can make your variables that specify specific rows
trials = [1, 3]
%use the trial vector 
n(trials, 1)

%%
%column says give me everything in that row from that column
%empty : is all of row or in second position in bracket it is all columns
n(:, 2)

%goes from 2 to end of rows in the second column
n(2:end, 2)

%takes the values in the 2nd to 3rd row in the 2nd column
n(2:3, 2)

%%
% (start:step:end) goes from start to end stepping by 2
r = 1:2:10

%%
%matrix transpose - takes the rows and columns vectors and flips them
flip = a'

%%
%can concating different variables by combining them in same bracket
c = [a b]

%need to have the same amount of rows and columns in order to concatenate

%%
%cna add a value to a matrix
%current size of c
size(c)
%adds to the 5th value the thing we assigned it
c(5) = 5

%if go beyond what we have, will add 10 to the 14th column
c(14) = 10

%to delete the empty columns added can index those columns and make them
%equal to nothing with []
c(11:13) = []

%%
%better to swap between an existing array or to keep adding to an array
%can pre allocate specific values to array
%each of these creates a 5 by 5 array of only one number
%creates a 5 by 5 in all zeros
z0 = zeros(5,5)
%creates a 5 by 5 in all ones
z1 = ones(5, 5)
%creates a 5 by 5 in all NaNs
zNan = NaN(5, 5)

%%
%can flip, transpose, and rotate matrixes
flipa = [1 2; 3 4; 5 6]
%rot90 rotates the array 90 degrees
rot90(flipa)

%a * [1 2] returns an arry becuase by default multiplication and devision
%is done on all numbers in a matrix
%the . does the multiplication oon just one item
flipa .* [1 2]

%%
%can save variables
save('myfirstMat.mat')

% and can load the variables back up
load myfirstMat.mat

%to find help for functions just type help then function name, tells what
%number does, syntax, examples
help save

%can also specify what variables we want to save
save secondmat.mat a b

%%
%can do statistical descriptive math without a package installed 

%this takes the mean column wise 
mean(a)

%transpose the variable to take the mean row wise
mean(a')

%will do it across the whole matrix
mean(a','all')

%%
%some other useful functions is rand function which are also pre installed
%into matlab
%however in matlab random numbers arent truly random, to avoid this problem
%can reset the random number using rng('shuffle') - probably should this
%every time before you do anything
rng('shuffle')

%also can SEED random numbers you generated to a particular value
%rng(10) 
%this can be useful if you want to tie it to a particular subject and save
%what seed they get and view what seed they get

%this lets you see what is the current state of the random number generator
%(rng) when you assign it to a variable to view it
%asssigning the seed to a variable
rng_try = rng()

%gives you a random number
rand()

%applying the rng to the rng seed rng try
rng(rng_try)

%gives you the same random number as you set the seed
rand()

