import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import vlc
import datetime
import os
import time

# FUNCTIONS -----------------------------------------------------------------
hasModelRan = False
#creates the general information display button
def generalInfoButtonCommand():
    #remove the buttons frame
    InfoButtonsFrame.pack_forget()

    inputInfoFrame.pack_forget()
    generalInfoFrame.pack(side="top", pady=10)#add the general and inputs info frames
    

    InfoButtonsFrame.pack(side = "top",pady = 10,padx = 10)#re add the buttons frame

def inputsInfoButtonCommand():
    #remove the buttons frame
    InfoButtonsFrame.pack_forget()

    generalInfoFrame.pack_forget()
    inputInfoFrame.pack(side="top", pady=10)
    

    InfoButtonsFrame.pack(side = "top",pady = 10,padx = 10)#re add the buttons frame

def generalButtonCommand():
    #forgets all the menus except the general menu
    if(hasModelRan == False): #checks if the regression model has ran
        rightSideContainer1.pack_forget()
        rightSideContainer2.pack_forget()
        rightSideContainer3.pack_forget()
        rightSideContainer4.pack_forget()
        rightSideContainer5.pack_forget()
        resultContainer.pack_forget()

        rightSideContainer1.pack(side="right", anchor="ne", padx=10, pady=10)#packs the general menu
    else:
        rightSideContainer1.pack_forget()
        rightSideContainer2.pack_forget()
        rightSideContainer3.pack_forget()
        rightSideContainer4.pack_forget()
        rightSideContainer5.pack_forget()
        resultContainer.pack_forget()

        resultContainer.pack(padx=10, pady=10)

def informationButtonCommand():
    hideAllRightSide()
    rightSideContainer1.pack_forget()
    rightSideContainer3.pack_forget()
    rightSideContainer4.pack_forget()
    rightSideContainer5.pack_forget()
    resultContainer.pack_forget()
    rightSideContainer2.pack(side="right", anchor="ne", padx=10, pady=10)



# Add login functionality
def loginButtonCommand():
    # Hide all other containers and show login container
    hideAllRightSide()
    rightSideContainer1.pack_forget()
    rightSideContainer2.pack_forget()
    rightSideContainer3.pack_forget()
    rightSideContainer5.pack_forget()
    resultContainer.pack_forget()
    rightSideContainer4.pack(side="right", anchor="ne", padx=10, pady=10)


def settingsButtonCommand():
    rightSideContainer1.pack_forget()
    rightSideContainer2.pack_forget()
    rightSideContainer3.pack_forget()
    rightSideContainer4.pack_forget()
    resultContainer.pack_forget()

    rightSideContainer5.pack(side="right", anchor="ne", padx=10, pady=10)#packs the settings menu

def hideAllRightSide():
    rightSideContainer1.pack_forget()
    rightSideContainer2.pack_forget()
    rightSideContainer3.pack_forget()
    rightSideContainer4.pack_forget()
    rightSideContainer5.pack_forget()
    resultContainer.pack_forget()

# FUNCTIONS -----------------------------------------------------------------



root = tk.Tk()#this instantiates the class that creates a screen 

root.geometry("800x750")#pass the dimensions of the window as a string

root.title("C.H.E.A.P")#creates a title for the menu

#defining the fonts that are used throughout the program 
titleFont = tkFont.Font(family="Bell MT", size=20)
bodyFont = tkFont.Font(family="Bell MT", size=12)
smallFont = tkFont.Font(family="Bell MT", size=9)
smallFontBold = tkFont.Font(family="Bell MT", size=9,weight = "bold")
HeartDisplayFont = tkFont.Font(family = "Bell MT",size = 30,weight = "bold")


mainTitle = tk.Label(root, text="Welcome to C.H.E.A.P - Cardiovascular \n Health Early Assessment Program",font = (titleFont),width= 32,borderwidth=1,relief="solid")
mainTitle.pack() # adds it to the menu

disclaimer = tk.Label(root, text = "This program does not provide a certified medical diagnosis",font = (smallFontBold))
disclaimer.pack(pady=10)#adds a vertial pack with size '10'

#creating the buttons for each page
menus = tk.Frame(root)
generalButton = tk.Button(menus,text = "General",font = (bodyFont,12), command= generalButtonCommand)
informationButton = tk.Button(menus,text = "Information",font = (bodyFont,12), command = informationButtonCommand)
#algorithmButon = tk.Button(menus,text = "Algorithm",font = (bodyFont,12))
loginButton = tk.Button(menus,text = "Login",font = (bodyFont,12),command =loginButtonCommand)
settingsButton = tk.Button(menus,text = "Settings",font = (bodyFont,12),command = settingsButtonCommand)

#placing the buttons

menus.pack(pady=10)


generalButton.pack(side="left",expand=True,padx= 10)
informationButton.pack(side="left",expand=True,padx= 10)
#algorithmButon.pack(side="left",expand=True,padx= 10)
loginButton.pack(side="left",expand=True,padx= 10)
settingsButton.pack(side="left",expand=True,padx= 10)


# Create a container for the right side (for info + buttons)
rightSideContainer1 = tk.Frame(root)#general menu
rightSideContainer1.pack(side="right", anchor="ne", padx=10, pady=10)

# Information Tab in rightSideContainer2
rightSideContainer2 = tk.Frame(root)  # Information menu


# Main bordered frame
infoWrapper = tk.Frame(
    rightSideContainer2,
    bd=2,
    relief="groove",
    padx=15,
    pady=15
)
infoWrapper.pack(anchor="nw", padx=10, pady=10, fill="both")

#define the content area
infoWidth = 700  
wrapLen = infoWidth - 40


# SECTION 1 — What does C.H.E.A.P diagnose?
section1 = tk.Frame(infoWrapper)
section1.pack(anchor="w", pady=(0, 20), fill="x")

tk.Label(section1, text="What does C.H.E.A.P diagnose?", font=smallFontBold).pack(anchor="w")
tk.Label(
    section1,
    text="C.H.E.A.P is used to diagnose and predict different cardiovascular diseases such as:\n"
        "- Stroke\n"
        "- Angina\n"
        "- Heart attacks",
    font=bodyFont,
    justify="left",
    wraplength=wrapLen
).pack(anchor="w")


# SECTION 2 — How was the algorithm trained?
section2 = tk.Frame(infoWrapper)
section2.pack(anchor="w", pady=(0, 20), fill="x")

tk.Label(section2, text="How was the algorithm trained?", font=smallFontBold).pack(anchor="w")

tk.Label(
    section2,
    text=
        "This dataset contains the relevant health factors which the program used to determine a "
        "regression line based on the data. Since each data point associates to the presence of "
        "cardiovascular disease or not, you can create coefficients for each input based on how "
        "much they factor towards the estimate.\n\n"
        "Since your assessment involves interpolation, the intention is solely to estimate your "
        "cardiovascular health, as interpolation can never lead to definite results. Additionally, "
        "cardiovascular diseases and many other health-related information rely on your genes, "
        "hundreds of specific parameters and random factors — the assessment can never be a "
        "definite diagnosis.",
    font=bodyFont,
    justify="left",
    wraplength=wrapLen
).pack(anchor="w")


# SECTION 3 — How can you gain certain input data?
section3 = tk.Frame(infoWrapper)
section3.pack(anchor="w", fill="x")

tk.Label(section3, text="How can you gain certain input data?", font=smallFontBold).pack(anchor="w")

tk.Label(
    section3,
    text="Obtaining the majority of the data required is intuitive and simple. However, obtaining "
        "certain optional data and some specific input data can be challenging.\n\n"
        "• Cholesterol: measured through a blood test through the NHS or GP.\n\n"
        "• Blood pressure: measured using a blood pressure machine from the NHS or GP.",
    font=bodyFont,
    justify="left",
    wraplength=wrapLen
).pack(anchor="w")



rightSideContainer3 = tk.Frame(root)#algorithm menu


rightSideContainer4 = tk.Frame(root)#login menu

userUsername = ""
userPassword = ""

loginTitle = tk.Label(rightSideContainer4, text="Login to Diary", font=titleFont)
loginTitle.pack(pady=10,padx=10)#create the title for the diary login

usernameLoginFrame = tk.Frame(rightSideContainer4)
usernameLoginLabel = tk.Label(usernameLoginFrame, text="Username:", font=bodyFont)
usernameLoginEntry = tk.Entry(usernameLoginFrame, width=20, font=bodyFont)
usernameLoginFrame.pack(pady=5)
usernameLoginLabel.pack(side="left", padx=5)
usernameLoginEntry.pack(side="left", padx=5)
#create similar entry labels as the sign up area


passwordLoginFrame = tk.Frame(rightSideContainer4)
passwordLoginLabel = tk.Label(passwordLoginFrame, text="Password:", font=bodyFont)
passwordLoginEntry = tk.Entry(passwordLoginFrame, width=20, font=bodyFont, show="*")
passwordLoginFrame.pack(pady=5)
passwordLoginLabel.pack(side="left", padx=5)
passwordLoginEntry.pack(side="left", padx=5)

#check if the variables are not empty
def attemptLogin():
    AttemptUsername = usernameLoginEntry.get().strip()
    AttemptPassword = passwordLoginEntry.get().strip()
    if userUsername != "" and userPassword != "" and AttemptUsername == userUsername and AttemptPassword == userPassword:
        messagebox.showinfo("Success", "Login successful!")
        showDiaryContent()
        
    else:
        messagebox.showerror("Error", "Invalid username or password.")


loginButton = tk.Button(rightSideContainer4, text="Login", font=bodyFont, command=attemptLogin)
loginButton.pack(pady=10,padx=10)


def showDiaryContent():
    # Clear the login frame first
    for widget in rightSideContainer4.winfo_children():
        widget.destroy()
    
    # Create main container for diary with two columns
    mainDiaryFrame = tk.Frame(rightSideContainer4)
    mainDiaryFrame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Left column for health markers
    leftColumn = tk.Frame(mainDiaryFrame, borderwidth=1, relief="solid")
    leftColumn.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    
    # Right column for diary
    rightColumn = tk.Frame(mainDiaryFrame, borderwidth=1, relief="solid")
    rightColumn.pack(side="right", fill="both", expand=True, padx=5, pady=5)
    
    # Health markers in left column
    healthTitle = tk.Label(leftColumn, text="Your Health Summary", font=titleFont)
    healthTitle.pack(pady=10)
    
    healthDataText = f"""
    Age: {int(inputs[0]/365)} years
    Sex: {'Male' if inputs[1] == 2 else 'Female'}
    Height: {inputs[2]} cm
    Weight: {inputs[3]} kg
    BMI: {inputs[3] / ((inputs[2]/100) ** 2):.1f}
    Smoking: {'Yes' if inputs[4] == 1 else 'No'}
    Alcohol: {'Yes' if inputs[5] == 1 else 'No'}
    Physical Activity: {'Yes' if inputs[6] == 1 else 'No'}
    Guide: {"https://www.health.harvard.edu/healthbeat/10-small-steps-for-better-heart-health"}
    """
    
    healthLabel = tk.Label(leftColumn, text=healthDataText, font=bodyFont, justify="left")
    healthLabel.pack(pady=10, padx=10)
    
    # Add some spacing and additional health information if available
    if inputs[7] != -1:  # Systolic BP
        bpText = f"Systolic BP: {inputs[7]} mm/Hg\n"
        if inputs[8] != -1:  # Diastolic BP
            bpText += f"Diastolic BP: {inputs[8]} mm/Hg"
        bpLabel = tk.Label(leftColumn, text=bpText, font=bodyFont, justify="left")
        bpLabel.pack(pady=5, padx=10)
    
    if inputs[9] != -1:  # Cholesterol
        cholLevels = ["Normal", "Above Normal", "Well Above Normal"]
        cholLabel = tk.Label(leftColumn, text=f"Cholesterol: {cholLevels[inputs[9]-1]}", font=bodyFont, justify="left")
        cholLabel.pack(pady=5, padx=10)
    
    if inputs[10] != -1:  # Glucose
        glucLevels = ["Normal", "Above Normal", "Well Above Normal"]
        glucLabel = tk.Label(leftColumn, text=f"Glucose: {glucLevels[inputs[10]-1]}", font=bodyFont, justify="left")
        glucLabel.pack(pady=5, padx=10)
    
    # Diary content in right column
    diaryTitle = tk.Label(rightColumn, text="Your Health Diary", font=titleFont)
    diaryTitle.pack(pady=10)
    
    diaryPrompt = tk.Label(rightColumn, text="How are you feeling today? Track your health journey:", font=bodyFont)
    diaryPrompt.pack(pady=5)
    
    # Create a frame for the text area and scrollbar
    textFrame = tk.Frame(rightColumn)
    textFrame.pack(pady=10, padx=10, fill="both", expand=True)
    
    # Create scrollbar
    scrollbar = tk.Scrollbar(textFrame)
    scrollbar.pack(side="right", fill="y")
    
    # Create text widget for diary entry 
    global diaryText
    diaryText = tk.Text(textFrame, 
        width=50, 
        height=15, 
        font=bodyFont,
        yscrollcommand=scrollbar.set,
        wrap="word",
        bg="white",
        fg="black",
        borderwidth=2,
        relief="solid")
    diaryText.pack(side="left", fill="both", expand=True)
    
    # Configure scrollbar
    scrollbar.config(command=diaryText.yview)
    
    # Load previous diary entries
    loadDiaryEntries()
    
    # Buttons frame
    diaryButtonsFrame = tk.Frame(rightColumn)
    diaryButtonsFrame.pack(pady=10)
    
    saveButton = tk.Button(diaryButtonsFrame, text="Save Entry", font=bodyFont, command=saveDiaryEntry)
    saveButton.pack(side="left", padx=5)
    
    viewButton = tk.Button(diaryButtonsFrame, text="View All Entries", font=bodyFont, command=viewAllEntries)
    viewButton.pack(side="left", padx=5)
    
    clearButton = tk.Button(diaryButtonsFrame, text="Clear", font=bodyFont, command=clearDiaryEntry)
    clearButton.pack(side="left", padx=5)

def saveDiaryEntry():
    entryContent = diaryText.get("1.0", tk.END).strip()
    if not entryContent:
        messagebox.showwarning("Empty Entry", "Please write something before saving.")
        return
    
    # Create filename based on username
    filename = f"{userUsername}_diary.txt"
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare entry with timestamp
    diaryEntry = f"\n--- Entry on {timestamp} ---\n{entryContent}\n"
    
    try:
        # Append to file (create if doesn't exist)
        with open(filename, "a", encoding="utf-8") as file:
            file.write(diaryEntry)
        
        messagebox.showinfo("Success", "Diary entry saved successfully!")
        diaryText.delete("1.0", tk.END)  # Clear the text area
    except Exception as e:
        messagebox.showerror("Error", f"Could not save diary entry: {str(e)}")

def loadDiaryEntries():
    """Load the most recent diary entry to show context"""
    filename = f"{userUsername}_diary.txt"
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                # Get the last entry (last 2 sections)
                entries = content.split("--- Entry on ")[-2:]  # Get last 2 entries
                if entries:
                    last_entry = "--- Entry on " + "--- Entry on ".join(entries)
                    # Show a preview of the last entry
                    diaryText.insert("1.0", f"Last entry preview:\n{last_entry[:500]}...\n\n--- New Entry ---\n")
        except Exception as e:
            print(f"Could not load previous entries: {str(e)}")


def viewAllEntries():
    """Display all diary entries in a new window"""
    filename = f"{userUsername}_diary.txt"
    if not os.path.exists(filename):
        messagebox.showinfo("No Entries", "You haven't written any diary entries yet.")
        return
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Create new window to display all entries
        entries_window = tk.Toplevel(root)
        entries_window.title("Your Diary Entries")
        entries_window.geometry("600x400")
        
        # Create a frame for the text area and scrollbar
        text_frame = tk.Frame(entries_window)
        text_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Create scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")
        
        # Create text widget for displaying entries
        entries_text = tk.Text(text_frame, 
            width=70, 
            height=20, 
            font=bodyFont,
            yscrollcommand=scrollbar.set,
            wrap="word",
            bg="white",
            fg="black",
            borderwidth=2,
            relief="solid")
        entries_text.pack(side="left", fill="both", expand=True)
        
        # Configure scrollbar
        scrollbar.config(command=entries_text.yview)
        
        # Insert content and make read-only
        entries_text.insert("1.0", content)
        entries_text.config(state="disabled")  # Make it read-only
        
        close_button = tk.Button(entries_window, text="Close", font=bodyFont, command=entries_window.destroy)
        close_button.pack(pady=5)
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not read diary entries: {str(e)}")


def clearDiaryEntry():
    """Clear the current diary text"""
    if messagebox.askyesno("Clear", "Are you sure you want to clear your current entry?"):
        diaryText.delete("1.0", tk.END)



rightSideContainer5 = tk.Frame(root,border= 1,relief= "solid")#settings menu

#creating the left side container for the users input
leftSideContainer = tk.Frame(root,borderwidth=2,relief="solid")
leftSideContainer.pack(side="left", anchor="ne", padx=10, pady=10)


#create a frame for the general info
generalInfoFrame = tk.Frame(rightSideContainer1,borderwidth=1,relief="solid")

#details the functionality of the program
generalInfo1 = tk.Label(generalInfoFrame, text ="C.H.E.A.P calculates your risk of heart attack and \ncardiovascular related diseases and risks based on \nparameters that correlate closely to the presence \nor lack of cardiovascular disease.", font = (bodyFont),justify="left",anchor="e")       


#provides more information about the intentions of the program
generalInfo2 = tk.Label(generalInfoFrame, text = "Once your data is presented and analysed, your risk \nwill be presented with a traffic light system or heart\n age comparison based on your personal preference.\n\nC.H.E.A.P is solely a predictive program \nthat can be used as guidance before receiving\n professional advice from a practitioner. Early in \nC.H.E.A.P refers to the fact that the program \nacts as a precursor to medical assessment.",font = (bodyFont),justify="left",anchor="e")



generalInfo1.pack(side="top",padx = 5,pady = 5)
generalInfo2.pack(side="bottom",padx = 5,pady = 5)
#creates a horizontal and vertical pad with width and height 5 and packs it.

#pack the frame and general info
generalInfoFrame.pack(side = "top",pady = 10,padx = 10)

#create the frame and label for input info
inputInfoFrame = tk.Frame(rightSideContainer1,borderwidth=1,relief="solid")
inputInfo = tk.Label(inputInfoFrame, text = "Compulsory Inputs:\n\nAge: your age in years, which must be between 18 and 90\nSex: your gender assigned at birth\nHeight: your last measured height (cm, integer)\nWeight: your most recent weight (kg, integer)\nSmoking: smoked (cigarettes) within the last 6 months\nAlcohol intake:12 units or more per week\nPhysical activity:180 minutes+ of sustained raised heart rate\n\nOptional Inputs:\n\nSystolic BP: the top number in a BP reading, units:(mm/Hg)\nDiastolic BP: bottom number in your BP reading (mm/Hg)\nGlucose: glucose levels in mg/dL (integer)\nCholesterol: cholesterol levels (LDL) in mg/dL (integer)\n",font = (bodyFont),justify = "left",anchor = "e")
inputInfo.pack(pady = 5,padx = 5)#packing the input information label

#creating and packing the information buttons
InfoButtonsFrame = tk.Frame(rightSideContainer1,borderwidth=1,relief="solid")#creating a frame for the info and general buttons

infoButtonstext = tk.Label(InfoButtonsFrame,text = "press the 'input Information' button to learn more about the listed inputs.",font = (smallFont))#creating some text for the infobuttons frame

generalInfoButton = tk.Button(InfoButtonsFrame,text = "General Information", command= generalInfoButtonCommand)#creating the general button

inputsInfoButton = tk.Button(InfoButtonsFrame, text = "Input Information",command= inputsInfoButtonCommand)#creatings inputs button


InfoButtonsFrame.pack(side = "top",pady = 10,padx = 10)
infoButtonstext.pack(side = "top",pady = 3,padx = 3)
generalInfoButton.pack(side="left",padx = 8,pady = 5)#packing the general button
inputsInfoButton.pack(side = "left",padx = 8,pady = 5)#packing info button


#settings menu font change functions
def fontChange(newFont):
    smallFont.config(family =newFont)
    smallFontBold.config(family= newFont)
    titleFont.config(family = newFont)
    bodyFont.config(family = newFont)

def fontSizeChange():
    #stores the title font, body font and small font sizes respectively
    #index 1 is comparison index
    userInput = fontSizeEntry.get().strip()#retrieve the user input from Entry object
    
    #validating userInput
    userValidation = True #currently the input is accepted
    
    if(userInput.isdigit() == False):
        userValidation = False  
    else:
        userInput = int(userInput)
    
    if(userValidation == True and (int(userInput) < 6 or int(userInput) > 18)):
        userValidation = False


    fontSizes = [titleFont.cget("size"),bodyFont.cget("size"),smallFont.cget("size"),smallFontBold.cget("size"),HeartDisplayFont.cget("size")]

    if userValidation ==True:
        if(fontSizes[1] > userInput):
            #need to reduce font sizes
            difference = fontSizes[1] - userInput
            for i in range(len(fontSizes)):
                fontSizes[i] -= difference
        else:
            difference = userInput - fontSizes[1]
            for i in range(len(fontSizes)):
                fontSizes[i] += difference

    titleFont.config(size = fontSizes[0])
    bodyFont.config(size = fontSizes[1])
    smallFont.config(size = fontSizes[2])
    smallFontBold.config(size = fontSizes[3])
    HeartDisplayFont.config(size = fontSizes[4])

FontChangeText = tk.Label(rightSideContainer5, text = "Use the following buttons to change the font used in the program:", font = bodyFont)
#different font choices
FontChangeText.pack(side="top", expand=True, pady=10)

# create a frame to hold all font buttons horizontally
fontButtonsFrame = tk.Frame(rightSideContainer5)
fontButtonsFrame.pack(side="top", pady=10)

DefaultFont = tk.Button(fontButtonsFrame, text="Default", font=("Bell MT", 12), command=lambda: fontChange("Bell MT"))
VerdanaFont = tk.Button(fontButtonsFrame, text="Verdana", font=("Verdana", 12), command=lambda: fontChange("Verdana"))
ProductSansFont = tk.Button(fontButtonsFrame, text="Calibri", font=("Calibri", 12), command=lambda: fontChange("Calibri"))
MontserratFont = tk.Button(fontButtonsFrame, text="Aptos", font=("Aptos", 12), command=lambda: fontChange("Aptos"))

# pack all buttons side by side in the sub-frame
DefaultFont.pack(side="left", expand=True, padx=10)
VerdanaFont.pack(side="left", expand=True, padx=10)
ProductSansFont.pack(side="left", expand=True, padx=10)
MontserratFont.pack(side="left", expand=True, padx=10)

#new frame below for the font size label and input box
fontSizeFrame = tk.Frame(rightSideContainer5)
fontSizeFrame.pack( pady=10)

fontSizeTextLabel = tk.Label(fontSizeFrame, text="Enter new font size:", font=bodyFont)
fontSizeTextLabel.pack(side="left", pady=5)

fontSizeEntry = tk.Entry(rightSideContainer5, width=10, font=bodyFont)
fontSizeEntry.pack(pady=5)

fontSizeEntry.bind("<Return>", lambda event: fontSizeChange())

#adding the input boxes in the left side container 

compulsoryInputParameters = tk.Frame(leftSideContainer,borderwidth = 1, relief = "solid")
optionalInputParameters = tk.Frame(leftSideContainer,borderwidth = 1, relief = "solid")

compulsoryInputParameters.pack(side = "top",pady = 10, padx = 10)
optionalInputParameters.pack(side = "top",pady = 10,padx = 10)#adding the input frames to the leftside container

userAge = 0



#title
compulsoryTitle = tk.Label(compulsoryInputParameters,text = "Compulsory Inputs:",font = bodyFont)

compulsoryTitle.pack(padx=5,pady =5)
#objects for age
ageFrame= tk.Frame(compulsoryInputParameters)
ageEntryLabel = tk.Label(ageFrame,text = "Age (18-90): ",font=bodyFont)#create the label displaying the age text
ageEntry = tk.Entry(ageFrame, width = 5,font = bodyFont)#create the entry box for taking users age

ageFrame.pack(side = "top")
ageEntryLabel.pack(padx=2,pady=5,side = "left")
ageEntry.pack(padx= 5,pady = 5)

#objects for users sex
sexFrame = tk.Frame(compulsoryInputParameters)
sexEntryLabel = tk.Label(sexFrame, text="Sex:", font=bodyFont)

# Use an IntVar (or StringVar) for shared state
sexVar = tk.StringVar(value="None")

sexButtonMale = tk.Radiobutton(
    sexFrame, text="Male", variable=sexVar, value="Male", font=bodyFont
)
sexButtonFemale = tk.Radiobutton(
    sexFrame, text="Female", variable=sexVar, value="Female", font=bodyFont
)

sexFrame.pack(side="top")
sexEntryLabel.pack(padx=2, pady=5, side="left")
sexButtonMale.pack(padx=5, pady=5, side="left")
sexButtonFemale.pack(padx=2, pady=5, side="left")

#objects for height

heightFrame = tk.Frame(compulsoryInputParameters)
heightEntryLabel = tk.Label(heightFrame, text = "Height (cm): ",font = bodyFont)
heightEntry = tk.Entry(heightFrame,width = 5,font=bodyFont)


heightFrame.pack(side = "top")
heightEntryLabel.pack(padx=2,pady = 5,side = "left")
heightEntry.pack(padx =5,pady = 5)

#objects for weight

weightFrame = tk.Frame(compulsoryInputParameters)
weightEntryLabel = tk.Label(weightFrame, text = "Weight (kg): ",font = bodyFont)
weightEntry = tk.Entry(weightFrame,width = 5,font = bodyFont)

weightFrame.pack(side = "top")
weightEntryLabel.pack(padx =2,pady = 5,side = "left")
weightEntry.pack(padx = 5, pady = 5)

#objects for smoking
smokingFrame = tk.Frame(compulsoryInputParameters)
smokingEntryLabel = tk.Label(smokingFrame, text="Do you smoke?", font=bodyFont)
smokingVar = tk.StringVar(value="None")
smokeYes = tk.Radiobutton(smokingFrame, text="Yes", variable=smokingVar, value="Yes", font=bodyFont)
smokeNo = tk.Radiobutton(smokingFrame, text="No", variable=smokingVar, value="No", font=bodyFont)


smokingFrame.pack(side="top")
smokingEntryLabel.pack(padx=5, pady=5, side="left")
smokeYes.pack(padx=5, pady=5, side="left")
smokeNo.pack(padx=5, pady=5, side="left")

#objects for alcohol
alcoholFrame = tk.Frame(compulsoryInputParameters)
alcoholEntryLabel = tk.Label(alcoholFrame, text="Do you drink alcohol?", font=bodyFont)
alcoholVar = tk.StringVar(value="None")
alcoholYes = tk.Radiobutton(alcoholFrame, text="Yes", variable=alcoholVar, value="Yes", font=bodyFont)
alcoholNo = tk.Radiobutton(alcoholFrame, text="No", variable=alcoholVar, value="No", font=bodyFont)


alcoholFrame.pack(side="top")
alcoholEntryLabel.pack(padx=5, pady=5, side="left")
alcoholYes.pack(padx=5, pady=5, side="left")
alcoholNo.pack(padx=5, pady=5, side="left")

#objects for sedentary
activityFrame = tk.Frame(compulsoryInputParameters)
activityEntryLabel = tk.Label(activityFrame, text="Are you physically active?", font=bodyFont)
activityVar = tk.StringVar(value="None")
activityYes = tk.Radiobutton(activityFrame, text="Yes", variable=activityVar, value="Yes", font=bodyFont)
activityNo = tk.Radiobutton(activityFrame, text="No", variable=activityVar, value="No", font=bodyFont)


activityFrame.pack(side="top")
activityEntryLabel.pack(padx=5, pady=5, side="left")
activityYes.pack(padx=5, pady=5, side="left")
activityNo.pack(padx=5, pady=5, side="left")


#optional titles
optionalTitle = tk.Label(optionalInputParameters,text = "Optional Inputs:", font = bodyFont)

optionalTitle.pack(padx=5,pady =5)


#objects for systolic blood pressure
systolicFrame = tk.Frame(optionalInputParameters)
systolicEntryLabel = tk.Label(systolicFrame,text = "Systolic blood pressure (mm / Hg): ",font = bodyFont)
systolicEntry = tk.Entry(systolicFrame,width = 5, font = bodyFont)

systolicFrame.pack(side = "top")
systolicEntryLabel.pack(padx = 5,pady = 5, side = "left")
systolicEntry.pack(padx = 5, pady =5)

#objects for diastolic blood pressure
diastolicFrame = tk.Frame(optionalInputParameters)
diastolicEntryLabel = tk.Label(diastolicFrame, text = "Diastolic bood pressure (mm / Hg): ", font = bodyFont)
diastolicEntry = tk.Entry(diastolicFrame,width = 5,font = bodyFont)

diastolicFrame.pack(side = "top")
diastolicEntryLabel.pack(padx=5,pady= 5,side = "left")
diastolicEntry.pack(padx = 5,pady =5)

#objects for glucose 
glucoseFrame = tk.Frame(optionalInputParameters)
glucoseEntryLabel = tk.Label(glucoseFrame,text = "Glucose Levels (mg/dL): ",font = bodyFont)
glucoseEntry = tk.Entry(glucoseFrame,width = 5,font = bodyFont)

glucoseFrame.pack(side = "top")
glucoseEntryLabel.pack(padx = 5, pady = 5, side = "left")
glucoseEntry.pack(padx = 5,pady = 5)

#objects for cholesterol
cholesterolFrame = tk.Frame(optionalInputParameters)
cholesterolEntryLabel = tk.Label(cholesterolFrame,text = "Cholesterol Level (mg/dL):",font = bodyFont)
cholesterolEntry = tk.Entry(cholesterolFrame,width = 5, font = bodyFont)

cholesterolFrame.pack(side = "top")
cholesterolEntryLabel.pack(padx =5,pady = 5, side = "left")
cholesterolEntry.pack(padx=5, pady =5)

#move resultContainer outside of the function
resultContainer = tk.Frame(root,borderwidth = 1, relief = "solid")

inputs = [-1] * 11
#Validation
def validateCompulsoryInputs():
    errors = []# array of errors
    #age
    ageVal = ageEntry.get().strip()
    if not ageVal.isdigit():
        errors.append("Age must be a number.")
    elif not (18 <= int(ageVal) <= 90):
        errors.append("Age must be between 18 and 90.")
    else:
        inputs[0] = int(ageVal) * 365

    #sex
    if sexVar.get() not in ["Male", "Female"]:
        errors.append("Please select your sex.")
    else:
        if sexVar.get() == "Female":
            inputs[1] = 1
        else:
            inputs[1] = 2
    
    #height
    heightVal = heightEntry.get().strip()
    if not heightVal.isdigit() or not (90 <= int(heightVal)<= 250):
        errors.append("Height must be a integer between 90 and 250cm.")
    else:
        inputs[2] = int(heightVal)
    
    #weight
    weightVal = weightEntry.get().strip()
    if not weightVal.isdigit() or not (40 <= int(weightVal) <= 240):
        errors.append("Weight must be a integer between 40 and 240kg.")
    else:
        inputs[3] = int(weightVal)
    
    #smoking
    if smokingVar.get() not in ["Yes", "No"]:
        errors.append("Please indicate if you smoke.")
    else:
        if smokingVar.get() == "No":
            inputs[4] = 0
        else:
            inputs[4] = 1
    
    #alcohol
    if alcoholVar.get() not in ["Yes", "No"]:
        errors.append("Please indicate if you drink alcohol.")
    else:
        if alcoholVar.get() == "No":
            inputs[5] = 0
        else:
            inputs[5] = 1
    
    #activity
    if activityVar.get() not in ["Yes", "No"]:
        errors.append("Please indicate if you are physically active.")
    else:
        if activityVar.get() == "No":
            inputs[6] = 0
        else:
            inputs[6] = 1
    

    #optional inputs
    #systolic BP
    sysBP = systolicEntry.get().strip()
    if sysBP != "" and not sysBP.isdigit():
        errors.append("Systolic blood pressure must be numeric.")

    elif sysBP  != "" and not (70 <= int(sysBP) <= 175):
        errors.append("Systolic blood pressure must be between 70 and 175 mm/Hg.")

    elif sysBP != "":
        inputs[7] = int(sysBP)
    
    #diastolic BP
    diaBP = diastolicEntry.get().strip()
    if diaBP != "" and not diaBP.isdigit():
        errors.append("Diastolic blood pressure must be numeric.")

    elif diaBP  != "" and not(50 <= int(diaBP) <= 110):
        errors.append("Diastolic blood pressure must be between 50 and 110 mm/Hg.")

    elif diaBP != "":
        inputs[8] = int(diaBP)

    
    #cholesterol
    cholesterol = cholesterolEntry.get().strip()
    if cholesterol != "" and not cholesterol.isdigit():
        errors.append("Cholesterol must be numeric.")
    elif cholesterol != "" and not(80 <= int(cholesterol)<= 280):
        errors.append("Cholesterol must be between 80 and 280 mg/dL.")
    elif cholesterol != "":  
        if int(cholesterol) <= 200:
            inputs[9] = 1
        elif int(cholesterol) > 200 and int(cholesterol) <= 240:
            inputs[9] = 2
        else:
            inputs[9] = 3
    
    #glucose
    glucose = glucoseEntry.get().strip()
    if glucose != "" and not glucose.isdigit():
        errors.append("Glucose must be numeric.")
    elif glucose  != "" and not(50 <= int(glucose)<= 160):
        errors.append("Glucose levels (LDL) must be between 50 and 160 mm/dL.")
    elif glucose != "":
        if int(glucose) <= 100:
            inputs[10] = 1
        elif int(glucose) > 100 and int(glucose) <= 125:
            inputs[10] = 2
        else:
            inputs[10] = 3

    if errors:
        messagebox.showerror("Input Error", "\n".join(errors))
    else:
        root.state("zoomed")
        messagebox.showinfo("Loading...", "Calculating your diagnosis. Please wait.")
        regressionModel()

#submit button
submitButton = tk.Button(optionalInputParameters, text="Submit", font=bodyFont, command = validateCompulsoryInputs)
submitButton.pack(pady=5)


def regressionModel():
    global hasModelRan

    hasModelRan = True
    userInputs = {
        "age": [inputs[0]],
        "gender": [inputs[1]],
        "height": [inputs[2]],
        "weight": [inputs[3]],
        "smoke": [inputs[4]],
        "alco": [inputs[5]],
        "active": [inputs[6]],
        "ap_hi": [inputs[7]],
        "ap_lo": [inputs[8]],
        "cholesterol": [inputs[9]],
        "gluc": [inputs[10]]
    }

    optional_indices = {
    7: "ap_hi",
    8: "ap_lo",
    9: "cholesterol",
    10: "gluc"
    }

    colsToDrop = [col for idx, col in optional_indices.items() if inputs[idx] == -1]
    
    userDataFrame = pd.DataFrame(userInputs)

    userDataFrame['BMI'] = userDataFrame['weight'] / ((userDataFrame['height']/100) ** 2)

    

    
    #IMPLEMENTING THE REGRESSION MODEL
    from full_logistic_model import fullLogisticModel#import the class containing the regression model

    data = pd.read_csv("cleaned_cardio_train3.csv")#read the data from the cleaned cardiovascular dataset

    data['BMI'] = data['weight'] / ((data['height']/100) **2) #creates a column called BMI using the weight and height columns



    #dropped unecessary columns from the datasets
    userDataFrame = userDataFrame.drop(colsToDrop,axis = 1)

    cardioData = data.drop(colsToDrop, axis = 1)
    cardioData = cardioData.drop(["id", "cardio","height","weight"], axis=1) #contains all the records for every column except 'id', 'cardio', 'height' and 'weight'
    userDataFrame = userDataFrame.drop(["height", "weight"],axis = 1)
    
    cardioValue = data["cardio"].values #contains all the values for the 'cardio' column

    #align the columns
    userDataFrame = userDataFrame.reindex(columns = cardioData.columns)


    scaler = StandardScaler()
    cardioData_train = scaler.fit_transform(cardioData)
    #scales the data down using a standard scaler (Z-world)
    
    userDataFrame = scaler.transform(userDataFrame)
    # Train model
    model = fullLogisticModel(lr=0.01, numIters=5000)
    model.fit(cardioData_train, cardioValue)

    # Test model
    cardioValue_pred = model.predict(userDataFrame)
    hideAllRightSide()
    actualProb = model.probability(userDataFrame)
    print(cardioValue_pred)
    print("actual probability:",actualProb)

    #can create the heart age real age comparison
    resultContainerHeartAge = tk.Frame(resultContainer)
    
    n = 18
    healthyUserProbabilities = []

    while (n <= 90):
        healthyUser = {
            "age": [int(n*365)],
            "gender": [int(2)],
            "ap_hi": [int(120)],
            "ap_lo": [int(80)],
            "cholesterol": [int(1)],
            "gluc": [int(1)],
            "smoke": [int(0)],
            "alco": [int(0)],
            "active": [int(1)],
            "BMI": [int(22)]
        }

        healthyUserFrame = pd.DataFrame(healthyUser)
        healthyUserFrame = healthyUserFrame.reindex(columns=cardioData.columns)
        healthyUserFrame = scaler.transform(healthyUserFrame)

        prob = model.probability(healthyUserFrame)
        healthyUserProbabilities.append(float(prob))
        n += 1


    probDifference = 1
    heartAge = -1

    for i in range(len(healthyUserProbabilities)):
        newDifference = abs(actualProb - healthyUserProbabilities[i])
        if newDifference < probDifference:
            probDifference = newDifference
            heartAge = i + 18   # index 0 = age 18



    # The result container 
    resultContainerTraffic = tk.Frame(resultContainer)

    # Create a row for the buttons
    buttonRow = tk.Frame(resultContainer)
    buttonRow.pack(fill="x", pady=10)

    from tkinter import PhotoImage

    greenImg = PhotoImage(file="greenLight.png")
    amberImg = PhotoImage(file="amberLight.png")
    redImg = PhotoImage(file="redLight.png")

    # Create horizontal row for (image + text)
    lightRow = tk.Frame(resultContainerTraffic)
    heartRow = tk.Frame(resultContainerHeartAge)
    # Traffic light label inside its own container
    trafficLightLabel = tk.Label(lightRow)
    heartAgeDisplay = tk.Label(heartRow , font=HeartDisplayFont, borderwidth=2, relief="solid")

    #explanationLabelTraffic
    explanationTrafficLabel = tk.Label(lightRow, font=bodyFont, borderwidth=1, relief="solid")

    #explanation for Heart
    explanationHeartLabel = tk.Label(heartRow,font = bodyFont,borderwidth = 1, relief= "solid")

    #functions for display
    def showHeartAge():
        hideAllRightSide()
        resultContainer.pack(padx = 10,pady = 10)
        resultContainerTraffic.pack_forget()
        resultContainerHeartAge.pack_forget()


        heartAgeDisplay.config(text = heartAge)
        explanation = ""
        if abs(heartAge - int(inputs[0])) <= 3:
            explanation = "Your relative risk for developing cardiovascular disease is low, and your health markers\n do not correlate with measurements that factor\n into the development of cardiovascular diseases."
        elif abs(heartAge - int(inputs[0])) > 3 and abs(heartAge - int(inputs[0])) <= 10:
            explanation = "Your relative risk for developing a cardiovascular disease should be brought to your attention.\n Although you don’t fall within the dangerous range for cardiovascular disease development\n, you should actively work towards a healthier lifestyle for your future."
        else:
            explanation = "Your relative risk for developing a cardiovascular disease is high. If you haven’t already,\n consult a medical practitioner for an assessment and potentially \nfurther guidance to better your cardiovascular health."
        
        #packing the row
        heartRow.pack(fill = "x",pady = 10)

        #packing containers
        explanationHeartLabel.config(text = explanation)
        resultContainerHeartAge.pack(pady=10,padx = 2 )
        heartAgeDisplay.pack(side = "top", padx=2,pady=2)
        explanationHeartLabel.pack(side = "left", padx = 10)


    def showRiskLight():
        hideAllRightSide()
        resultContainer.pack(padx=10,pady = 10)
        resultContainerHeartAge.pack_forget()

        # Reset previous contents
        resultContainerTraffic.pack_forget()

        # Pack below buttons
        resultContainerTraffic.pack(fill="both", pady=10)
        

        lightRow.pack(fill="x", pady=10)
        
        # Choose correct traffic light
        explanation = ""
        if actualProb < 0.33:
            trafficLightLabel.config(image=greenImg)
            explanation = "Your relative risk for developing a cardiovascular disease is low.\n Your health markers do not correlate with measurements\n that factor into the development of cardiovascular diseases."
        elif actualProb < 0.66:
            trafficLightLabel.config(image=amberImg)
            explanation = "Your relative risk for developing a cardiovascular disease \nshould be brought to your attention. Although you don’t fall\n within the dangerous range for cardiovascular disease development,\n you should actively work towards a healthier lifestyle for your future."
        else:
            trafficLightLabel.config(image=redImg)
            explanation = "Your relative risk for developing a cardiovascular disease is high.\n If you haven’t already, consult a medical practitioner for an assessment\n and potentially further guidance to better your cardiovascular health."



        # Pack image + explanation side by side
        trafficLightLabel.pack(side="left", padx=10)
        explanationTrafficLabel.config(text=explanation)
        explanationTrafficLabel.pack(side="left", padx=10)

    #buttons
    trafficLightButton = tk.Button(buttonRow, text="Traffic Light Display",font=bodyFont, command=showRiskLight)
    heartAgeButton = tk.Button(buttonRow, text="Heart Age Display", font=bodyFont, command=showHeartAge)

    trafficLightButton.pack(side="left", expand=True, padx=10)
    heartAgeButton.pack(side="left", expand=True, padx=10)

    showRiskLight()
    #packing main container
    resultContainer.pack(padx=10, pady=10)


    #video player

    # Heart Row
    heartVideoFrame = tk.Frame(heartRow, borderwidth=1, relief="solid")
    heartVideoPanel = tk.Frame(heartVideoFrame, width=300, height=180, bg="black")
    heartVideoPanel.pack(pady=10, padx=10)

    heartVideoFrame.pack(pady=10, padx=10, side="right")

    heartVLC = vlc.Instance("--no-xlib")
    heartPlayer = heartVLC.media_player_new()
    heartPlayer.set_hwnd(heartVideoPanel.winfo_id())

    # Light Row
    lightVideoFrame = tk.Frame(lightRow, borderwidth=1, relief="solid")
    lightVideoPanel = tk.Frame(lightVideoFrame, width=300, height=180, bg="black")
    lightVideoPanel.pack(pady=10, padx=10)

    lightVideoFrame.pack(pady=10, padx=10, side="right")

    lightVLC = vlc.Instance("--no-xlib")
    lightPlayer = lightVLC.media_player_new()
    lightPlayer.set_hwnd(lightVideoPanel.winfo_id())

    # Playback functions for heart row
    def playHeartVideo():
        media = heartVLC.media_new("cardiovascularVideo.mp4")
        heartPlayer.set_media(media)
        heartPlayer.play()

    def pauseHeartVideo():
        heartPlayer.pause()

    def stopHeartVideo():
        heartPlayer.stop()

    # Playback functions for light row
    def playLightVideo():
        media = lightVLC.media_new("cardiovascularVideo.mp4")
        lightPlayer.set_media(media)
        lightPlayer.play()

    def pauseLightVideo():
        lightPlayer.pause()

    def stopLightVideo():
        lightPlayer.stop()

    # Buttons
    tk.Button(heartVideoFrame, text="Play", font=bodyFont, command=playHeartVideo).pack(side="left", padx=5)
    tk.Button(heartVideoFrame, text="Pause", font=bodyFont, command=pauseHeartVideo).pack(side="left", padx=5)
    tk.Button(heartVideoFrame, text="Stop", font=bodyFont, command=stopHeartVideo).pack(side="left", padx=5)

    tk.Button(lightVideoFrame, text="Play", font=bodyFont, command=playLightVideo).pack(side="left", padx=5)
    tk.Button(lightVideoFrame, text="Pause", font=bodyFont, command=pauseLightVideo).pack(side="left", padx=5)
    tk.Button(lightVideoFrame, text="Stop", font=bodyFont, command=stopLightVideo).pack(side="left", padx=5)

    
    #supporting text
    videoText = "This video explores the science behind the human cardiovascular system\n and health risks/factors. Watch to see how these scientific principles\n directly relate to assessing your cardiovascular health."


    videoRowHeart = tk.Frame(resultContainerHeartAge)
    videoRowLight = tk.Frame(resultContainerTraffic)

    videoRowHeart.pack(padx=10,pady=10,side ="bottom",anchor = "e")
    videoRowLight.pack(padx=10,pady=10,side = "right")

    heartVideoTextLabel = tk.Label(
        videoRowHeart,
        text=videoText,
        font=bodyFont,
        justify="left",
        borderwidth = 1,
        relief = "solid"
    )
    heartVideoTextLabel.pack(fill = "x", padx=5, pady=5,side = "right")

    #For Traffic Light Display


    lightVideoTextLabel = tk.Label(
        videoRowLight,
        text=videoText,
        font=bodyFont,
        justify="left",
        borderwidth = 1,
        relief = "solid"
    )
    lightVideoTextLabel.pack(fill = "x",padx=5, pady=5,side = "right")


    #adding the area where you can sign up for diary
    diaryToolFrame = tk.Frame(resultContainer, borderwidth=1, relief="solid")

    # At the end of regressionModel()
    diaryToolFrame.pack(padx=10, pady=10, side="bottom", fill="x")

    diaryExplanationLabel = tk.Label(diaryToolFrame, text="Opening a diary within C.H.E.A.P is a great way to track your progress\n as you work towards a healthier lifestyle. C.H.E.A.P will provide the data\n you entered within your diary as well as a general plan for you.", font=bodyFont, justify="left")

    # Create a frame for the input fields
    diaryInputFrame = tk.Frame(diaryToolFrame, borderwidth=1, relief="solid")

    # Username input
    usernameFrame = tk.Frame(diaryInputFrame)
    usernameLabel = tk.Label(usernameFrame, text="Username:", font=bodyFont)
    usernameEntry = tk.Entry(usernameFrame, width=20, font=bodyFont)

    usernameFrame.pack(pady=5)
    usernameLabel.pack(side="left", padx=5)
    usernameEntry.pack(side="left", padx=5)

    # Password input
    passwordFrame = tk.Frame(diaryInputFrame)
    passwordLabel = tk.Label(passwordFrame, text="Password:", font=bodyFont)
    passwordEntry = tk.Entry(passwordFrame, width=20, font=bodyFont)

    passwordFrame.pack(pady=5)
    passwordLabel.pack(side="left", padx=5)
    passwordEntry.pack(side="left", padx=5)


    def signUpCommand():
        errors = []

        userName = usernameEntry.get().strip()
        if(userName == ""):
            errors.append("User name must be present.")
        elif (len(userName) <= 5):
            errors.append("User name must be greater than 5 characters.")
        
        password = passwordEntry.get().strip()
        
        if(password == ""):
            errors.append("Password must be present.")
        elif (len(password) <= 5):
            errors.append("Password must be greater than 5 characters.")
        
        if errors:
            messagebox.showerror("Sign Up Error", "\n".join(errors))
        else:
            messagebox.showinfo("Success", "Information Saved.")
            global userUsername
            global userPassword
            userUsername = userName
            userPassword = password
            





    # Sign up button
    signUpButton = tk.Button(diaryInputFrame, text="Sign Up for Diary", font=bodyFont, command = signUpCommand)
    signUpButton.pack(pady=10)

    # Pack the diary components
    diaryExplanationLabel.pack(padx=5, pady=5, side="right")
    diaryInputFrame.pack(padx=5, pady=5, side="left")

root.mainloop()
