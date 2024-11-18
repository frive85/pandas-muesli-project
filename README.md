# Project - Data Analysis

This project is centered around exploratory data 
analysis [(EDA)](./EDA_Checklist.pdf) techniques and statistical analysis.

## Topic and Task

Your task will be to complete a case study to answer specific questions of our stakeholder by performing data analysis and visualisation. 
You can find the detailed task description [here](./Assignment.md).

## Suggested workflow - MVP  

The work is timeboxed, and with that in mind, you need to change how you approach the task. You will want to employ an iterative approach. 

* Write a plan of how you will complete the project. Refer to this regularly.
* When unsure or facing overly complex topics: make assumptions or simplifications that allow you to move on with your plan.
* Make simple plots
* Main questions should be answered first -> Think MVP (minimum viable product) and POC (proof of concept) 
* Iterate: go deeper, go prettier, go better
* Clean up .. feel free to delete things that are not useful anymore (even if you spent loads of time on it!)

## Suggested workflow for git

* one person forks this repository
* include or check the .gitignore file in your repo. At the least your data folder should be listed, since you want to make sure not to push any data to GitHub.
* add the other team members as a collaborators
* recommended but not necessary: work on your own branch.
* create a new .ipynb file and start with your EDA!
  - it's a good idea to split different steps into different notebooks. You can save intermediate results as `.csv`-files.
  - when working seperately from team mates, use different files that can be combined later, or work carefully to avoid merge conflicts!
* split tasks in your group, push results and merge into main if other person needs your results.
* in the end: merge everything into the main branch
* at the final step ("after the project"), the team members can fork the final state of the repo so to copy it into their own GitHub.  

<!--
- Please create a new repository on GitHub and invite all team members to collaborate.
  - Include a .gitignore file to your repo. At the least your data folder should be listed, since you want to make sure not to push any data to GitHub.
- Start VS Code!
- Either use your base environment or if you want to experiment with new packages:
  - Create a new virtual environment, eg.:  
```BASH 
# Create new environment
$ conda create --name <env_name> python=3.9
# Activate environment 
$ conda activate <env_name>
# Installing packages 
$ conda install <package_name>
```
  - Also after having created this environment, you can install additional packages within it. **Make sure you have activated your environment before installing new packages within it**!
  - Work in branches and push your changes to the repository in order to keep your notebooks synchronised.
  - Create a new .ipynb file and start with your EDA!
  - It's a good idea to split different steps into different notebooks. Save intermediate results as `.csv`-files.
  - When working seperately from teammates use different files that can be combined later, or work carefully to avoid merge conflicts!
-->

**Have fun and do not stress yourself too much!!!**

