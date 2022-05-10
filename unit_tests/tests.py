# import relevant packages
import unittest
from ml_helpers import fns
import pandas as pd
import numpy as np
import random
from nose.tools import assert_dict_equal
from numpy.testing import assert_array_equal
import warnings

# remove persistant warnings
warnings.filterwarnings("ignore")
np.seterr(divide = 'ignore')

class test_ml_helpers(unittest.TestCase):
  
  # set seed
  np.random.seed(24)
  
  # craete basic randomised data frame to use as function input
  original_df = pd.DataFrame({'id': list(range(1, 21)),
                              'label': np.random.random_integers(0, 1, 20),
                              'feat_1': np.random.random_sample(size = 20),
                              'feat_2': np.random.random_integers(-1000, 1000, 20),
                              'feat_3': np.random.random_integers(0, 1000, 20)})
  dates = ['2022-01-24', '2021-12-24', '2021-11-24', '2021-10-24']
  original_df['snap_d'] = dates * 5
  original_df['snap_d'] = pd.to_datetime(original_df['snap_d'],
                                         dayfirst = True)
  
  
  # label_file_summary test 1
  def test_label_file_summary(self):
    
    # prep data for tests
    ## define input data frame
    input_df = self.original_df.copy()
    # craete actual returned function output
    actual_df_summary =\
    fns.label_file_summary(df = input_df, id_col = 'id',
                           label_col = 'label',
                           date_col = 'snap_d',
                           outcome_class = 1,
                           monthly_f = False,
                           weights = False)
    
    ## create expected returned df_summary
    expected_df_summary =\
    pd.DataFrame({'volume' : [20],
                  'outcome_volume' : [15],
                  'outcome_volume_neg' : [5],
                  'outcome_rate': [15/20*100]})
    
    # tests
    ## test shape of returned df_summary
    assert_array_equal(actual_df_summary.shape,
                       expected_df_summary.shape,
                       "oops, there's a bug...")
    
    ## test exact output of returned df_summary
    assert_dict_equal(actual_df_summary.to_dict(),
                       expected_df_summary.to_dict(),
                       "oops, there's a bug...")
    
    
  # down sample test 1
  def test_down_sample(self):
    
    # prep data for tests
    ## define input data frame
    input_df = self.orginal_df.copy()
    
    ## create actual returned data frames
    actual_df = fns.down_sample(input_df, id_col = 'id',
                                label_col = 'label',
                                majority_class_label = 1,
                                x = 2.7)
    
    # tests
    ## test shape of returned ds_df
    assert_array_equal(actual_df.shape, (18, 6),
                       "oops, there's a bug...")
    
    
  # weights test 1
  def test_weights(self):
    
    # prep data for tests
    ## define input data frame
    input_ds_df = fns.down_sample(self.orginal_df, id_col = 'id',
                                label_col = 'label', date_col = 'snap_d'
                                majority_class_label = 1,
                                x = 1.9)[0]
    
    ## create actual returned data frames
    [actual_df_weighted, actual_weight_summary] =\
    fns.weights(self.orginal_df, input_ds_df, id_col = 'id',
                label_col = 'label', date_col = 'snap_d',
                monthly_f = False)
    
    ## create expected returned weight_summary
    expected_weight_summary =\
    pd.DataFrame({'label' : [0, 1],
                  'total_v' : [5, 15],
                  'down_sampled_v' : [5, 6],
                  'weight' : [1.0, 2.5]})
    
    
    # tests
    ## test shape of returned df_weighted
    assert_array_equal(actual_df_weighted.shape, (11, 4),
                       "oops, there's a bug...")
    
    
    ## test shape of returned weight_summary
    assert_array_equal(actual_weight_summary.shape,
                       expected_weight_summary.shape,
                       "oops, there's a bug...")
    
    
    ## test exact output of returned weight_summary
    assert_dict_equal(actual_weight_summary.to_dict(),
                       expected_weight_summary.to_dict(),
                       "oops, there's a bug...")
    
if __name__ == '__main__':
  unittest.main()
    
    
    
    
    
