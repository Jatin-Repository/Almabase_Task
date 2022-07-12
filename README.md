# Almabase_Task
Looking at the task, my approch was start forward to create a 
  1) class of **Profile**
  2) I have consider input as txt file (input) and later under **InputFileImpementation class**
     i)   created method **read_input_file** I converted whole input file as string
     ii)  later I created method **extract_profiles** method , where I removed unwanted characters from string  and later 
          made a dictionery with  name **entries** where the profile_number(key) and details(which is in string) act as value for dictionary
          entries **{profile number : details}**
    iii)  later with the help of **assign_details_to_profile** method further cleaning string and took another dictionary by profile
          **{id:x,email:e,first_name:y,last_name:z,class_year:a,date_of_birth:d}**
    iv)   later **updated the entries dictionery** as:
          **{profile number : profile}**
    v)    Now finally, after taking entries dictionary keys as input to list2, taking two Profile object x and y for two profile at a time to 
          checked_dupilcates among two and iteratively over all the possible combinations, with the help of method **check_duplicate(x, y)** 
          The ouput of the method is list where **[score,[matched_attribute],[non_matched_attribute],[skiped_attribute]]**
          
  # Sample Input : 1
    
      profile 1 - { id: 1, email: 'knowkanhai@gmail.com', first_nam
      e: ‘Kanhai’, last_name: ‘Shah’, class_year: 2012, date_of_birt
      h: ’1990-10-11’, }
      profile 2 - { id: 2, email: 'knowkanhai@gmail.com', first_nam
      e: ‘Kanhai1’, last_name: ‘Shah’, class_year: 2012, date_of_bir
      th: ’1990-10-11’}
      
   # Sample Output : 1
     
      ["https://github.com/Jatin-Repository/Almabase_Task/blob/master/screen_shot/Sample_Output_1.pdf"](Output)

        
