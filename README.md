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
      
   # Sample Output: 1
      https://github.com/Jatin-Repository/Almabase_Task/blob/master/screen_shot/Sample_Output_1.pdf
      
   # Sample Input: 2
   
     profile 1 - { id: 1, email: 'knowkanhai@gmail.com', first_nam
     e: ‘Kanhai’, last_name: ‘Shah’, class_year: None, date_of_birt
     h: None}
     profile 2 - { id: 2, email: 'knowkanhai@gmail.com', first_nam
     e: ‘Kanhai1’, last_name: ‘Shah’, class_year: 2012, date_of_bir
     th: ’1990-10-11’}
     
   # Sample Output: 2
      https://github.com/Jatin-Repository/Almabase_Task/blob/master/screen_shot/Sample_Output_2.pdf
      
   # Sample Input : 3
  
      profile 1 - { id: 1. email: 'knowkanhai@gmail.com', first_nam
      e: ‘Kanhai’, last_name: ‘Shah’, class_year: None, date_of_birt
      h: None}
      profile 2 - { id: 2, email: 'knowkanhai+donotcompare@gmail.co
      m', first_name: ‘Kanhai1’, last_name: ‘Shah’, class_year: 201
      2, date_of_birth: ’1990-10-11’}
    
   # Sample Output : 3
     https://github.com/Jatin-Repository/Almabase_Task/blob/master/screen_shot/Sample_Output_3.pdf
     
   # Sample_Input :
      
     profile 1 - { id: 1, email: 'knowkanhai@gmail.com', first_nam
     e: ‘Kanhai’, last_name: ‘Shah’, class_year: None, date_of_birt
     h: None}
     profile 2 - { id: 2, email: 'knowkanhai+donotcompare@gmail.co
     m', first_name: ‘Kanhai1’, last_name: ‘Shah’, class_year: 201
     2, date_of_birth: ’1990-10-11’}
     profile 3 - { id: 5, email: 'jatindeepsingh500@gmail.co
     m', first_name: ‘Jatin15’, last_name: ‘Singh’, class_year: 200
     2, date_of_birth: ’1997-02-05’}
     profile 4 - { id: 9, email: 'jatideep500@mail.com",
     first_name: ‘Jatin’, last_name: ‘Singh500’, class_year: 202
     2, date_of_birth: ’1990-10-11’}
     
   # Sample_Output 
     https://github.com/Jatin-Repository/Almabase_Task/blob/master/screen_shot/Input_Output.pdf

   
   
     

     

        
