# End to end Machine Learning project
# Student Performance Indicator
## Overview
The Student Performance Indicator project aims to analyze how various factors influence student test scores. Using data that includes variables like gender, parental education, ethnicity, and lunch status, this project builds a model to understand which factors significantly impact student performance. By identifying these influences, the project provides insights that could be used to support academic interventions and improve student outcomes.

## Dataset
The dataset consists of 1,000 student records with 8 columns, capturing demographic and performance-related attributes. Columns are categorized as Categorical or Numerical:

Categorical Columns:
Gender: The gender of the student.
Race/Ethnicity: The student's race or ethnic background.
Parental Level of Education: The highest education level achieved by the student's parent(s).
Lunch: Indicates whether the student receives free/reduced lunch or has a standard lunch.
Test Preparation Course: Indicates if the student completed a test preparation course.

Numerical Columns:
Math Score: The student’s score in math.
Reading Score: The student’s score in reading.
Writing Score: The student’s score in writing.
The dataset can be accessed here : https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

**Target variable is selected as maths score (you can select any other score if you like)**

## Pre-processing
* Verified that the dataset had no missing or duplicate values, ensuring it was clean and ready for analysis.
* A Column Transformer was created to apply different preprocessing techniques to numerical and categorical features:
  * Used StandardScaler to standardize numerical features.
  * Used OneHotEncoder to convert categorical variables into a format suitable for machine learning. 


## EDA
### Distribution of average scores across all students and  histogram illustrating average scores with a hue representing gender.
![{96AF5931-E7E4-4988-8C96-669B638DDA5B}](https://github.com/user-attachments/assets/d50d78d4-6395-4727-bd42-fb3fe6ea7825)
* Females performs better than males in terms of both total and average scores.

### Role of lunch on Avg. marks
![{7E0A9005-5570-4435-91C2-E9DAD853C1A8}](https://github.com/user-attachments/assets/0d76e638-ca16-4794-b044-7530b29d96fc)
* Standard lunch helps perform well in exams be it a male or a female.

### Role of Parents Education
![{70305B2C-2B2C-4146-A1BD-DBAFC06436F4}](https://github.com/user-attachments/assets/7d7d863a-58af-4345-814c-e60bb458cef8)
* In general parent's education don't help student perform well in exam.
* 2nd plot shows that parent's whose education is of associate's degree or master's degree their male child tend to perform well in exam
* 3rd plot we can see there is no effect of parent's education on female students.

### Histogram on Ethinic groups affecting Studemt scores
![{8DC04FA8-4E82-479E-8658-62367202B77C}](https://github.com/user-attachments/assets/37a996f6-08fc-492d-bb4a-69c98859fc4b)
* Students of group A and group E tends to perform poorly in exam irrespective of whether they are male or female

### Impact of lunch on student performance
![{C9ECC4B3-C541-405A-8592-96A6D1ABCCEF}](https://github.com/user-attachments/assets/c1cc7a7b-b5bd-42be-beca-d14293004f5b)
* Students who get Standard Lunch tend to perform better than students who got free/reduced lunch

### Test preperation cource effect on student performance
![{75A6526D-BE5F-406B-94B1-987137E0E6A9}](https://github.com/user-attachments/assets/36717e9e-e049-466f-8ab4-d6f79ab07cc8)
* Students who have completed the Test Prepration Course have scores higher in all three categories than those who haven't taken the course.

### MUTIVARIATE ANALYSIS USING PAIRPLOT
![{C441D050-5E6E-4C40-B2FC-D8B2D94EDC45}](https://github.com/user-attachments/assets/3d3b605c-f94f-4b96-83c9-946e82844d48)
* From the above plot it is clear that all the scores increase linearly with each other.

## Modeling
### Train-test split
### Used models like **Ridge Regression**, **Linear Regression**, **Random Forest**, **Lasso Regression**, **K-Nearest Neighbors (KNN)**, **Decision Tree** to predict results

![{3DA9C054-DB98-4B74-9AFB-DAC045275559}](https://github.com/user-attachments/assets/bbba3cd1-3e2d-4fa3-971d-f81270b12396)

* **Ridge and Linear Regression models performed the best, indicating a strong relationship between the features and student performance.**


## Flask Application
### How to Run the Application
1. Ensure that Flask is installed in your environment.
2. Run the application with the command:
   ```bash
   python app.py
3. Open your web browser and navigate to http://127.0.0.1:8080/ to access the app.

![{45FD7167-20BB-4679-86DB-3714DAB4F5C3}](https://github.com/user-attachments/assets/6539eb9f-da48-4776-ae61-17dcae232c82)

## Deployment in Azure webapp
### Create an Azure container registory 
![{907D5C79-EC00-4C00-8BB7-38C5A62720FF}](https://github.com/user-attachments/assets/7a34141e-0b11-45f3-8023-0852e0780b15)

### Create a docker in VS code terminal
docker build -t testdockeryuvraj.azurecr.io/mltest:latest .
docker login testdockeryuvraj.azurecr.io
docker push testdockeryuvraj.azurecr.io/mltest:latest

### Create a Azure Web App 
![{8812D0E7-5057-4B99-A433-CD3568FEF02F}](https://github.com/user-attachments/assets/367483ff-307c-4141-a4c0-ffcc5004c431)

### Link it to github repo and from actions make sure it is running fine
![{5B810E3D-B280-4CFE-821D-2EA973135574}](https://github.com/user-attachments/assets/4f72d575-877b-408c-aa29-73b36485e3bc)



