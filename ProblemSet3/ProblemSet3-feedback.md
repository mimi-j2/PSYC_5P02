# PSYC 5P02- Introduction to Programming for Psychology
## Fall 2025

### Problem Set #3

### Rubric:
* Accuracy & Efficiency: 50%
* Explanation and documentation: 50%

--- 
###  Feedback:

* Good use of global variables for things like `stim_size`
* I like that you tried to randomize locations and prevent them from overlapping, but I think because you're sampling from the list without replacement it's not *fully* random (you can't have some combinations of coordinates). May not be a problem here but that's the kind of thing that can be a gremlin that can cause confounds if you're not careful. Perhaps a tupple of coordinate pairs would work?
* Good use of functions (defs). 
* When defining correct and incorrect trials, you could make it shorter by combining conditions (i.e., `if (resp == 'd' and targ_there == 1) or (resp =='a' and targ_there == 0):`
* for this code:
> ``#set total trials from the range of 1 to the trials input at start dialog box + 1 since range will always stop short of the last number
total_trials = range(1, trials + 1)``

You could just use `range(trials)` since that goes from 0 to trials - 1.
* I appreciated that you shuffled the conditions, although I wonder if it would make more sense to just randomize all the trials so the trial types are fully random? 
* I found a bug that when I made a response after it said I hadn't made a response in time it then gave me feedback on the response, and caclulated the RT as 0.0. Those RTs were included in the data file and in the final RT calculation! I couldn't quite diagnose the problem quickly, so I had chatGPT do it for me. Here's what it said: https://chatgpt.com/s/t_6900fe6e10f881919dfab3b2fe7897dd
* 
* When I quit the experiment early the window isn't killed (I needed to run the command `win.close()` to get it to go away.

* **Overall:** Good work. I like the use of the functions to improve efficiency and make it modular. Experiment logic is solid. I think one area to improve is the names you're giving your variables as they're overlapping sometimes and risk being confusing. 

**Accuracy & Efficiency:** 20/25
**Explanation and documentation:** 25/25
**Total:** 45/50
