class Project: # Example class
    def __init__(self, name=""):
        self.name = name # Instance variable
        
    def compile (self , projectName = ""): # Example method
        if projectName == "" or not projectName:
            projectName = self.name
        
        print("Project " + str(projectName) + " is now compiling")
        
project2 = Project(name = "project2")
project1 = Project(name = "project1") # Creating the objects 

project1.compile() # projectName is now project1
project2.name = "test_for_project_2" # We are overriding the name variable. The default value must be project2
Project.compile(project2) # projectName is now test_for_project_2