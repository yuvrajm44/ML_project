import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utlis import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformartion:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ['reading score','writing score']
            categorical_columns = ['gender', 
                                   'race/ethnicity', 
                                   'parental level of education', 
                                   'lunch',
                                   'test preparation course']
            num_pipeline = Pipeline(
                steps= [
                ("imputer", SimpleImputer(strategy= "median")),
                ("scaler", StandardScaler(with_mean=True))
                ] )

            cat_pipeline = Pipeline(
                steps= [
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehotencoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
                ]

            )
            
            logging.info("numerical col. standared scaling completed")
            logging.info("Categorical col. encoding completed")

            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline, numerical_columns),
                ("car_pipeline", cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor
    
        except Exception as e:
            raise CustomException(e , sys)
        

    def initiate_data_transformation(self, train_path,test_path):
        
        try :
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("obtaining pre processing object")

            preprocessing_obj = self.get_data_transformer_object()

            input_features_train_df = train_df.drop(columns= ["math score"])
            target_features_train_df = train_df["math score"]

            input_features_test_df = test_df.drop(columns= ["math score"])
            target_features_test_df = test_df["math score"]

            logging.info(" Applying preprocessing on training and testing dataset")

            input_features_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[input_features_train_arr, np.array(target_features_train_df)]
            test_arr = np.c_[input_features_test_arr, np.array(target_features_test_df)]

            logging.info("saved preprocessed object")

            save_object ( file_path =self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj )
            

            return (
            train_arr,
            test_arr,
            self.data_transformation_config.preprocessor_obj_file_path
            )
            
            
        
        except Exception as e:
            raise CustomException(e,sys)






