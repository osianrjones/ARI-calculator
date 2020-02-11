#ARI course work
import string 
import math

def read_from_file(): 
    with open ('ARI text file.txt') as file:
        for line in file:
                line=line.rstrip('\n') #Removes the \n, causing a new line
                texttitle,text,IntendedReadingAge,keywordsinput1,keywordsinput2,keywordsinput3, stringARI = line.split('/') #Splits the 7 values in the text file 
                textsList.append(text)                     ##
                TitleTextList.append(texttitle)             #   
                intendedRAList.append(IntendedReadingAge)   #
                keywordList1.append(keywordsinput1)         ###### Adds all 7 values to seperate lists 
                keywordList2.append(keywordsinput2)         #
                keywordList3.append(keywordsinput3)         #
                finalARIList.append(stringARI)             ##

def write_to_file():
    with open('ARI text file.txt','a') as Text:
        stringARI=str(ARI)
        Text.write("\n" + texttitle + "/" + text + "/" + IntendedReadingAge + "/" + keywordsinput1 + "/" + keywordsinput2 + "/" + keywordsinput3 + "/" + stringARI)
                    

TitleTextList=[]   ## 
intendedRAList=[]   #
keywordList1=[]     ### Lists where all the calculated data from the text is stored.
keywordList2=[]     #
keywordList3=[]     #
textsList=[]        ############
finalARIList=[]                # 
punctuationList=[".","?","!"]  # 


characters=0
words=0
sentences=0
ARIage=0

loop=True               ##
IRAverif=False           #
keywordsverif=False      ### Verification set to false as they have not been calculated correctly yet. 
textverif=False          #
keywordsnumverif=False   #
ARIverif=False           #
ARIageverif=False       ##    

print("Welcome to the ARI calculator")

#Loop allows program to restart without closing and losing current data.
while loop is True:
    choice=input("Would you like to: \n1.Search for a text and it's ARI \n2.Find the ARI of a specific text \n:")

#User inputs the title of the text 


    if choice=="2":
        
        texttitle=input("What is the title of the text?: ") 
        TitleTextList.append(texttitle) #Adds the title of the text to the list.
       




        #Entering text and assessing punctuation in the text 

        while textverif is False:

            text=input("Enter the text: ")


            #Number of characters

            spaces=0 #Variable set to 0 so that we can have a running total of the spaces.

            for i in text:
                if i==" ": 
                    spaces=spaces+1 #Adds 1 to spaces variable if a space has been found in the text.
    


            characters=(len(text)-spaces) #Characters is found by subtracting the number of spaces from the length of the text.
            
            if characters<=100:
                print("Please use more than 100 words.")

            for i in string.punctuation:  #Checks that punctuation is correct. 
                x=text
                for k in x:
                    if i == k:
                       textsList.append(text) #Adds the text to the list if punctuation has been used.
                       textverif=True #This changes to True if there is punctuation contained in the text. This avoids inaccurate calculation.
            if textverif == False: #If no punctuation is used an error message will be displayed.
                print("Make sure you use correct punctuation.")
            
                
                  

        #Intended reading age input and verification

        while IRAverif is False: 

            IntendedReadingAge=input("What is the intended reading age of this piece of text?: ")

            if IntendedReadingAge.isdigit()==True:  #Verification that input is a digit.
                intendedRAList.append(IntendedReadingAge) #Adds intended reading age to the list. 
                IRAverif=True
                break

            if IntendedReadingAge.isalpha()==True:
                print("Make sure the intended reading age is a number.")
                continue










        #Enter keywords

             
        keywordsinput1=input("Enter keyword: ")

        #1 keyword
        
        if keywordsinput1.isalpha()==True:
                        keywordList1.append(keywordsinput1) #Adds FIRST keyword to the list.
                        

        if keywordsinput1.isdigit()==True: #Checks to make sure keyword is string. 
                    print("Make sure you use words")
                    continue
        #2 keyword

        keywordsinput2=input("Enter keyword: ")

        if keywordsinput2.isalpha()==True:
                        keywordList2.append(keywordsinput2) #Adds SECOND keyword to the keyword list.
                        

        if keywordsinput2.isdigit()==True: #Checks to make sure keyword is string.
                    print("Make sure you use words")
                    continue
        #3 keyword
        
        keywordsinput3=input("Enter keyword: ")

        if keywordsinput3.isalpha()==True:
                        keywordList3.append(keywordsinput3) #Adds THIRD keyword to the list.
                        

        if keywordsinput3.isdigit()==True: #Checks to make sure keyword is string otherwise the calculations can not take place. 
                    print("Make sure you use words")
                    continue




        #Number of characters

        spaces=0 #Variable set to 0 so that we can have a running total of the spaces.

        for i in text:
            if i==" ": 
                spaces=spaces+1 #Adds 1 to spaces variable if a space has been found in the text.

        


        #Number of words

        words=int(len(text.split())) #Number of words found by splitting the text at the start of a new word.

        #Number of sentences

        for i in punctuationList :
            for o in text:
                if i==o:
                    sentences= sentences+1 #When a punctuation letter is passed 1 is added to the sentences variable. 

        #Calculating ARI

        formula=(4.71*(characters)/(words)+0.5*(words)/(6)-21.43) #Formula that calculates the US grade from the text that has been inputed.

       

        ARI=math.ceil(formula+4) #Rounds the calulated reading age to the nearest whole number.

        

        finalARIList.append(ARI) #Adds the reading age to the reading age list.

        #Outputing calculations

        print("The US grade for this piece of text is",ARI,",The intended reading age was",IntendedReadingAge)
        print("There are",sentences,"sentences")
        print("There are",words,"words")
        print("There are",characters,"characters")

        

         
        

        #Writes all calculated data to the text file, using sub routine at the top of this program.
        
        write_to_file()

        #Takes all the data from the text file and adds it to the correct list.

        read_from_file()

        
        




           

    if choice=="1":
        
        textfromtextname=[] 






        # User decides desired method to find a specific text. 
        listsearch=input("Would you like to: \n1)Search for a text using keywords \n2)Search for a text using text name \n3)Search for a text using US grade calculated reading age \n:  ")


        
        
        if listsearch=="1":
            keywordsearch=input("What keyword would you like to search for?: ")

            searchingforkeyword=True

            #Searches through each keyword list to find which one contains keyword.
            while searchingforkeyword is True:
                
               

                if keywordsearch in keywordList1:
                    num1 = keywordList1.index(keywordsearch) #Finds index of keyword in list.
                    print("Keyword found! Here is your text:","\n",textsList[num1]) #Finds corresponding text from keyword index.
                    searchingforkeyword=False
                    loop=False

                if keywordsearch in keywordList2:
                    num2 = keywordList2.index(keywordsearch) #Finds index of keyword in list.
                    print("Keyword found! Here is your text:","\n",textsList[num2]) #Finds corresponding text from keyword index.
                    searchingforkeyword=False
                    loop=False

                if keywordsearch in keywordList3:
                    num3 = keywordList3.index(keywordsearch)  #Finds index of keyword in list.
                    print("Keyword found! Here is your text:","\n",textsList[num3]) #Finds corresponding text from keyword index. 
                    searchingforkeyword=False
                    loop=False

                else:
                    print("Keyword not found, please search again")
                    searchingforkeyword=False


        if listsearch=="2":
            textnamesearch=input("What is the name of the text?: ")
             #Finds index of title in list.

           
           
            while textnamesearch in TitleTextList:
                num = TitleTextList.index(textnamesearch)

                print("Text found! Here is your text:","\n",textsList[num])  #Finds corresponding text from title index.
                textnamesearch=False
                loop=False
            if textnamesearch.isdigit():
                print("Make sure you do not use any numbers")

            else:
                #verification that input is in the list.
                print("Text not found, please try again")
                textnamesearch=input("What is the name of the text?: ")

        if listsearch=="3":
            readingagesearch=input("What is the reading age you are looking for?: ")
             #Finds index of ARI in list.

            if readingagesearch.isalpha():
                print("Make sure the input is a number") #verification that input is in the list.
                readingagesearch=input("What is the reading age you are looking for?: ")

            if readingagesearch in finalARIList:
                num = finalARIList.index(readingagesearch)
                print("Text found! Here is your text:","\n", textsList[num])#Finds corresponding text from ARI index.
                readingagesearch=False
                loop=False

            if readingagesearch=="0" or "22":
                print("Please enter a US grade from 1-22")
                continue
