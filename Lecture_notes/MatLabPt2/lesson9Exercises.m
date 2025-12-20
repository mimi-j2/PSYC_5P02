% Lesson 9 - in class exercises
%% 9.1 - making if statements
% Let's start by shuffling the rng
rng('shuffle');

a = rand();
myVar = 1==1;

if a < 0.3  %if the value a is less than .33 (if it returns true)
    b = a.^2;  %square
elseif a >= 0.33 & a <= .66    
    another = true;
    b = 0;
else % if everything returned false
    b = a.^.5; %squareroot
end; %the end of my first if statment 

%% 9.2 - Switch/case

k = randi(6); % make a variable

switch k %start of switch
    case {1,2}
        VWMCapacity = 'low';
    case {3,4}
        VWMCapacity = 'med';
    otherwise
        VWMCapacity = 'high';  
    
end % end of switch

%% 9.3 - For Loops


var = 11:21 % create a vector

for i = 1:length(var) %loop through elements of that vector
    
    i
    a = i^2
    
end % loop

%% 9.4 comparing indexing to loops

tic % start clock
a = zeros(1,10); % pre-allocating a variable
toc %end clock

b = [];
tic
for i = 1:10
    b(i) = i^2; %adding elements to b
end
toc

tic
for i = 1:10
    a(i) = i^2; %inserting elements into pre-allocated a
end
toc

%% 9.5 Embedding while loops

%while loops keep going forever until some condition is evaluated as false%
%matlab does not rely on indention 

numLoops = 0;
a = 0;        %give it a start value
numLoops2 = 0;
numLoops3 = 0;

while a < .9    %make it meat some condition
    numLoops = numLoops + 1;
    a = rand();  %reset value of a
        if a < .5
            numLoops2 = numLoops2 + 1;
            if a < .1
                continue; %continue will exit the if statement but continue the loop 
                numLoops3 = numLoops3 + 1;     
            end %ends second if statement
        end %ends top if statement
        if a == .7    %here's an if statement that will break out of the loop
            break; %breaks exits completley out of a late
        end %last if statement end
end %whil loop end

%% 9. 6 -  indexing

x = round(10 + randn(100,1))  %random normal numbers centered on 10

%true means that x is equal to 10,
(x==10)

%returns the values of x at the indices where the value of x is equal to 10
x(x==10)

%where you want to find places where x is equal to 10, returns the locations where x is
%equal to 10
find(x==10)

%returns the values at those index locations
x([1 5 10 15:20])

%any and all

%boolen where if any are equal to 10 returns True (1)
any(x==10)

%boolen where if all are equal to 10 returns True and if not all the
%numbers are equal to 10 returns False
all(x==10)

%% 9.7 - Functions

%functions are similar to pythons but in matpat there are no returns 
%instead you put what you want to return (in this case outputArray) in your
%function after function
function outputArray = subtractOne(inputArray)
    outputArray = inputArray - 1; % Subtract one from each element of the input array
end;

%subtracts one from each number in my array
subtractOne([10:3:33])

function myfcn(arg1,arg2,arg3)
if nargin < 3
    arg3 = some_value;
end;
if nargin < 2
    arg2 = some_other_value;
end;
end;

%nargn can make other arguments optional, create defaukts to make function
%flexible

%input can prompt input from user and use their input
subjectNum = input('Please enter the subject number: ');

%% 9.8 - text

%comparing strings:
'apples' == 'oranges'
strcmp('apples', 'oranges')

%can ignore case with strcmpi

%string find:

strfind('where in the world is carmen sandiego', 'carmen sandiego')

%string replace:

strrep('a a a a ', ' ', [])


% writing to a file:

fid = fopen('myFile.txt', 'wt');
rr = 1.1:5.1;

fprintf(fid,'%3.2f\t',rr);
fprintf(fid,'\n');
fprintf(fid,'%3.2f\t',rr + 2);

fclose(fid);

%% 9.9 - eval


numArrays = 10; 
A = cell(numArrays,1);
for n = 1:numArrays 
	A{n} = magic(n); 
    Eval(['A', int2str(n), ' = magic(n)']);
End

A{5}


Eval(['A', int2str(n), ' = magic(n)']);

%% structures and cells
