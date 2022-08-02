# The libraries are specified here. The json library is used to access json data used in this script.  

import json
import os
from unicodedata import name

# This script, at its most basic performs the following actions. 
# 1. Open the Data.json file. 
# 2. extract the data from the json file for each NIST SP 800-160 construct type (i.e. Goals, Objectives).
# 3. For each construct type, create class object for each of these individual element (i.e objective - Prevent/avoid).
# 4. Insert these class objects into a list for that construct. 
# 5. With the class objects in a class. It is then easier to compare constructs and their interactions. 


with open('Data.json', 'r') as f:

    data = json.load(f)

# The empty lists for the NIST SP 800 - 160 constructs are created here.  

list_goals = []
list_objectives = []
list_strat_principles = []
list_struct_principles = []
list_techniques = []
list_approaches = []



# The class objects are defined here for each construct. defaults have been put in for each attribute of the class. 
# i.e dicts and strings. Dicts are used to store mapping, while the strings are used to put in text. 
# The names of the classes are self explanitory.  

class Nist_800_160_Goal:
    def __init__(self,name = "name",  objectives = {} ):
        self.name = name
        self.objectives = objectives 

class Nist_800_160_Objective:
    def __init__(self, name = "", description = "", discussion =""):
        self.name = name
        self.description = description
        self.discussion = discussion

class Nist_800_160_Stategic_design_principle:
    def __init__(self, name = "", risk_response_priorities = {}):
        self.name = name 
        self.risk_response_priorities = risk_response_priorities

class Nist_800_160_Structural_design_principle: 
    def __init__(self, name = "", strategic_design_principles = {}):
        self.name = name 
        self.strategic_design_principles = strategic_design_principles

class NIST_800_160_Technique: 
    def __init__(self, name = "", definition = "", purpose = "", objectives = {}, approaches = {} ):
        self.name = name 
        self.defintion = definition
        self.purpose = purpose
        self.objectives = objectives
        self.approaches = approaches  

class NIST_800_160_Approach:
    def __init__(self, name = "" , definition = "", purpose = "", objectives = {}, approaches = {}):
        self.name = name
        self.defintion = definition
        self.purpose = purpose
        self.objectives = objectives 
        self.approaches = approaches 


# This objectives list, is used later in the script so that users of the script can define their chosen objectives. 
# by default, they are set fo 'false'.  

objectives_list = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False
}

#for i in objectives_list:
    #print(objectives_list[i])


# The functions below that are prefixed with 'get' are focused on the collection of data located in the Data.json file. 
# All of these functions are based around the same function. The description of how the function works is outlined in the first 
# function, this is the same for the rest of the 'get' functions. 

def get_goals_data():
    
    # This identifies where in the json file to collect data from. 

    goals = data["NIST 800-160 Goals"]
 
    # For each goal outlined in data.json do the following. 
    
    for goal in goals:
        
        name = goal["name"]
        list_goals.append( Nist_800_160_Goal(name)) # Add the name collected to the name attribute. 
        
        for y in list_goals:
            if len(y.objectives) == 0:
                y.objectives = goal["objectives"] # If the objective is empty, assign the value of objectives. 
            else:
                pass 

def get_objectives_data():
    objectives = data["NIST 800-160 Objectives"]

    for obj in objectives:
        name = obj["name"]
        list_objectives.append (Nist_800_160_Objective(name))

        for y in list_objectives:
            if len(y.description) == 0:
                y.description = obj["Description"]
            if len(y.discussion) == 0:
                y.discussion = obj["Discussion"]

def get_stat_design_principles():
    stat_design = data["NIST 800-160 Stategic design principles"]

    for principle in stat_design:
        name = principle["name"]
        list_strat_principles.append (Nist_800_160_Stategic_design_principle(name))

        for y in list_strat_principles:
            if len(y.risk_response_priorities) == 0:
                y.risk_response_priorities = principle["Risk response priorities"]        
        
def get_struct_design_principles():
    struct_design = data["NIST 800-160 Structural Design Principles"]
    for principle in struct_design:

        name = principle["name"]
        list_struct_principles.append(Nist_800_160_Structural_design_principle(name))

        for y in list_struct_principles:
            if len(y.strategic_design_principles) == 0:
                y.strategic_design_principles = principle["strategic design principles"] 


def compare():

    Anticipate = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}
    Withstand = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}
    Recover = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}
    Adapt = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}

    for x in list_goals: 

        for y in x.objectives: 

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Adapt":
                Adapt[y] = True
               

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Recover":
                Recover[y] = True
             

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Withstand":
                Withstand[y] = True
            

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Anticipate":
                Anticipate[y] = True
          
    
    anticipate_list = []

    adapt_list = []
  
    recover_list = []

    withstand_list =[]

    
    for key,value in Anticipate.items():
        if value == True: 
           
            anticipate_list.append(key) 

    for key,value in Adapt.items():
        if value == True: 
       
            adapt_list.append(key)  

    for key,value in Recover.items():
        if value == True: 
         
            recover_list.append(key)  

    for key,value in Withstand.items():
        if value == True: 
    
            withstand_list.append(key) 

    goal_ctr = {"Anticipate":len(anticipate_list), "Adapt":len(adapt_list), "Recover":len(recover_list), "Withstand":len(withstand_list)}

    goal_ctr = (sorted(goal_ctr.items(),key=lambda x:x[1], reverse=True)) 
 

    print("")
    print(("The {} GOAL Meets: {} NIST 800-160 OBJECTIVES.").format(goal_ctr[0][0],goal_ctr[0][1]))
    print("These are:")
    print("")

    if goal_ctr[0][0] == "Anticipate":
        for i in anticipate_list:
            print(("         * {}").format(i))
    
    if goal_ctr[0][0] == "Adapt":
        for i in adapt_list:
            print(("         * {}").format(i))
    
    if goal_ctr[0][0] == "Recover":
        for i in recover_list:
            print(("         * {}").format(i))
    
    if goal_ctr[0][0] == "Withstand":
        for i in withstand_list:
            print(("         * {}").format(i))

    print("")

    print(("The {} GOAL Meets: {} NIST 800-160 OBJECTIVES.").format(goal_ctr[1][0],goal_ctr[1][1]))
    print("These are:")
    print("")

    if goal_ctr[1][0] == "Anticipate":
        for i in anticipate_list:
            print(("         * {}").format(i))
    
    if goal_ctr[1][0] == "Adapt":
        for i in adapt_list:
            print(("         * {}").format(i))
    
    if goal_ctr[1][0] == "Recover":
        for i in recover_list:
            print(("         * {}").format(i))
    
    if goal_ctr[1][0] == "Withstand":
        for i in withstand_list:
            print(("         * {}").format(i))

    print("")

    print(("The {} GOAL Meets: {} NIST 800-160 OBJECTIVES.").format(goal_ctr[2][0],goal_ctr[2][1]))
    print("These are:")
    print("")

    if goal_ctr[2][0] == "Anticipate":
        for i in anticipate_list:
            print(("         * {}").format(i))
    
    if goal_ctr[2][0] == "Adapt":
        for i in adapt_list:
            print(("         * {}").format(i))
    
    if goal_ctr[2][0] == "Recover":
        for i in recover_list:
            print(("         * {}").format(i))
    
    if goal_ctr[2][0] == "Withstand":
        for i in withstand_list:
            print(("         * {}").format(i))

    print("")


    print(("The {} GOAL Meets: {} NIST 800-160 OBJECTIVES.").format(goal_ctr[3][0],goal_ctr[3][1]))
    print("These are:")
    print("")

    if goal_ctr[3][0] == "Anticipate":
        for i in anticipate_list:
            print(("         * {}").format(i))
    
    if goal_ctr[3][0] == "Adapt":
        for i in adapt_list:
            print(("         * {}").format(i))
    
    if goal_ctr[3][0] == "Recover":
        for i in recover_list:
            print(("         * {}").format(i))
    
    if goal_ctr[3][0] == "Withstand":
        for i in withstand_list:
            print(("         * {}").format(i))

    print("")


def show_selected_objectives():
    
    ob_prevent = " "
    ob_prepare = " "
    ob_continue = " "
    ob_constrain = " "
    ob_reconsitute = " "
    ob_understand = " " 
    ob_transform = " "
    ob_rearchitect = " "

    for key, value in objectives_list.items():
        if key == "Prevent/Avoid" and value == True:
            ob_prevent = "x"

        if key == "Prepare" and value == True:
            ob_prepare = "x"
        
        if key == "Continue" and value == True:
            ob_continue = "x"

        if key == "Constrain" and value == True:
            ob_constrain = "x"

        if key == "Reconstitute" and value == True:
            ob_reconsitute = "x"
        
        if key == "Understand" and value == True: 
            ob_understand = "x"

        if key == "Transform" and value == True:
            ob_transform = "x"
        
        if key == "Re-architect" and value == True:
            ob_rearchitect = "x" 

    print("")
    print("You have selected the following NIST SP 800-160 Objectives.")
    print (("Prevent/Avoid [{}] - Prepare [{}] - Continue [{}] - Constrain [{}] - Reconstitute [{}] - Understand [{}] - Transform [{}] - Re-architect [{}]").format(ob_prevent,ob_prepare,ob_continue,ob_constrain,ob_reconsitute,ob_understand,ob_transform,ob_rearchitect))
    print("")
   

def set_objectives():
    
    print("")
    print("---------- Console application ----------")
    print("")
    print("Choose NIST 800-160 objectives:")
    print("")
    
    ob_prevent = input("Prevent/Avoid? y for yes, n for no.")
    if ob_prevent == "y":
        objectives_list.update({"Prevent/Avoid": True})
    else:
        objectives_list.update({"Prevent/Avoid": False})

    ob_prepare = input("Prepare? y for yes, n for no.")
    if ob_prepare == "y":
        objectives_list.update({"Prepare": True})
    else:
        objectives_list.update({"Prepare": False})
    
    ob_continue = input("Continue? y for yes, n for no.")
    if ob_continue == "y":
        objectives_list.update({"Continue": True})
    else:
        objectives_list.update({"Continue": False})
    
    ob_constrain = input("Constrain? y for yes, n for no.")
    if ob_constrain == "y":
        objectives_list.update({"Constrain": True})
    else: 
        objectives_list.update({"Constrain": False})
    
    ob_reconsitute = input("Reconsitute? y for yes, n for no.")
    if ob_reconsitute == "y":
        objectives_list.update({"Reconstitute": True})
    else:
        objectives_list.update({"Reconstitute": False})
    
    ob_understand = input("Understand? y for yes, n for no.")
    if ob_understand == "y":
        objectives_list.update({"Understand": True})
    else:
        objectives_list.update({"Understand": False})
    
    ob_transform = input("Transform? y for yes, n for no.")
    if ob_transform == "y":
        objectives_list.update({"Transform": True})
    else: 
        objectives_list.update({"Transform": False})

    ob_rearchitect = input("Re-architect? y for yes, n of no.")
    if ob_rearchitect == "y":
        objectives_list.update({"Re-architect":True})
    else:
        objectives_list.update({"Re-architect":False})


def show(construct):

    if construct == "objectives":
        print("Objectives:")
        print("")
        for i in list_objectives:
            print(i.name)
        print("")
    
    if construct == "goals":
        print("Goals:")
        print("")
        for i in list_goals:
            print(i.name)
        print("")

    if construct == "strategic design principles":
        print("Stategic design principles:")
        print("")
        for i in list_strat_principles:
            print(i.name)
        print("")

    if construct == "structural design principles":
        print("Structural design principles")
        print("")
        for i in list_struct_principles:
            print(i.name)
        print("")

# Redundant function.

def console_read():
    os.system("cls")
    read = input("> ")
    
    while len(read) == 0:
        pass
    if read != 0:
        read = read.split(" ")

        if read[0] == "show": 

            
            if read[1] == "objectives":
                show(read[1])
                console_read()

            if read[1] == "goals":
                show(read[1])
                console_read()

            if read[1] == "strategic" and read[2] == "design" and read[3] == "principles":
                read = read[1] + " " + read[2] + " " + read[3]
                
                show(read)
                console_read()

            if read[1] == "structural" and read[2] == "design" and read[3] == "principles":
                read = read[1] + " " + read[2] + " " + read[3]
                print(read)
                show(read)
                console_read()

        else:
            print("Incorrect command.")
            input()
            os.system("cls")
            console_read()

get_stat_design_principles()

get_struct_design_principles()

get_goals_data()

get_objectives_data()
        
#os.system("clear")

#get_goals_data()

set_objectives()

#os.system("clear")

show_selected_objectives()

#input("Press ENTER to run analysis...")

#os.system("clear")

compare()




