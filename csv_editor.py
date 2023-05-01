import pandas as pd
import glob
import os
import csv
import numpy as np


class ChangeCsv:
    def __init__ (self):
        self.folder_name = ""
        
        self.main_order = ["dst_port", "flow_duration", "flow_byts_s", "flow_pkts_s", "fwd_pkts_s", "bwd_pkts_s", "tot_fwd_pkts",
        "tot_bwd_pkts", "totlen_fwd_pkts", "totlen_bwd_pkts", "fwd_pkt_len_max", "fwd_pkt_len_min",
        "fwd_pkt_len_mean", "fwd_pkt_len_std", "bwd_pkt_len_max", "bwd_pkt_len_min", "bwd_pkt_len_mean",
        "bwd_pkt_len_std", "pkt_len_max", "pkt_len_min", "pkt_len_mean", "pkt_len_std", "pkt_len_var",
        "fwd_header_len", "bwd_header_len", "fwd_seg_size_min", "fwd_act_data_pkts", "flow_iat_mean",
        "flow_iat_max", "flow_iat_min", "flow_iat_std", "fwd_iat_tot", "fwd_iat_max", "fwd_iat_min",
        "fwd_iat_mean", "fwd_iat_std", "bwd_iat_tot", "bwd_iat_max", "bwd_iat_min", "bwd_iat_mean",
        "bwd_iat_std", "fwd_psh_flags", "bwd_psh_flags", "fwd_urg_flags", "bwd_urg_flags", "fin_flag_cnt",
        "syn_flag_cnt", "rst_flag_cnt", "psh_flag_cnt", "ack_flag_cnt", "urg_flag_cnt", "ece_flag_cnt",
        "down_up_ratio", "pkt_size_avg", "init_fwd_win_byts", "init_bwd_win_byts", "active_max",
        "active_min", "active_mean", "active_std", "idle_max", "idle_min", "idle_mean", "idle_std",
        "fwd_byts_b_avg", "fwd_pkts_b_avg", "bwd_byts_b_avg", "bwd_pkts_b_avg", "fwd_blk_rate_avg",
        "bwd_blk_rate_avg", "fwd_seg_size_avg", "bwd_seg_size_avg", "cwe_flag_count", "subflow_fwd_pkts",
        "subflow_bwd_pkts", "subflow_fwd_byts", "subflow_bwd_byts"]
        
        
        
        
        
    #used for switching the order of columns in the cicd2017 university dataset inorder to make it match the cicflowmeter flow generation csv's column order.    
    def swapColumn(self, df):

        column_order = self.main_order
        df = df[column_order]

        return df
    
    def concatFiles(self, folder_name):
        # setting the path for joining multiple files
        files = os.path.join(folder_name, "*.csv")

        # list of merged files returned
        files = glob.glob(files)


        # joining files with concat and read_csv

        df = pd.concat([pd.read_csv(f) for f in files])
        #no need to use a seperator arg isnce the concat files already have it
        df.to_csv('dataset/cicflow2017/merged.csv', index=False)

    
    #used on the cicflow2017 university dataset 
    def replaceColumnNames(self, folder_name, column_names):
        # setting the path for joining multiple files
        files = os.path.join(folder_name, "*.csv")

        # list of merged files returned
        files = glob.glob(files)
    
        i = 0
    
        for file in files:
            i += 1 
            
            print(file)
            df = pd.read_csv(file)
            df.columns = column_names

            df.to_csv('dataset/cicflow2017/renamed'+str(i)+".csv", index=False)
            


    #remove the first column in a single csv file or all csv files in a folder
    def removeFirstColumn(self, df = pd.DataFrame(list()), file_name="capturedFlows.csv", folder_name=""):

        if (folder_name != ""):
        # setting the path for joining multiple files
            files = os.path.join(folder_name, "*.csv")
    
            # list of merged files returned
            files = glob.glob(files)
        
            i = 0
        
            for file in files:
                i += 1 
                
                print(file)
                df = pd.read_csv(file)
              
                df.to_csv('dataset/cicflow2017/renamedRemoved'+str(i)+".csv", sep=';', index=False, encoding='utf-8')
       
        else:
            #get first column
            first_column = df.columns[0]
            # Delete first
            df = df.drop([first_column], axis=1)
            df.to_csv(file_name)
             
            
            
            
            

    #make a csv file
    def createCSVFile(self, write_or_append, data, mode=0, file_name="capturedFlows.csv"):

  
        if write_or_append == "append" or write_or_append == "a": 
            df = data
            
            if (mode == 0):
                df.to_csv(file_name, mode='a', index=False)
            else:
                df.to_csv(file_name, mode='a', header=False, index=False)
                
            
        else: 
            df = data
            
            if mode == 0:
                df.to_csv(file_name, mode='w', index=False)
            else:
                df.to_csv(file_name, mode='w', header=False, index=False)
            
            
        
        
        

    #remove the columns from cicflowmeter's flow captures so it matches the trained models'
    def removeColumns(self, df, columns=["src_ip", "dst_ip", "src_port", "protocol", "timestamp"]):

        for column in columns:
            df = df.drop(column, axis=1)
            
        return df
        
        
"""


ar = ["dst_port", "flow_duration", "flow_byts_s", "flow_pkts_s", "fwd_pkts_s", "bwd_pkts_s", "tot_fwd_pkts",
        "tot_bwd_pkts", "totlen_fwd_pkts", "totlen_bwd_pkts", "fwd_pkt_len_max", "fwd_pkt_len_min",
        "fwd_pkt_len_mean", "fwd_pkt_len_std", "bwd_pkt_len_max", "bwd_pkt_len_min", "bwd_pkt_len_mean",
        "bwd_pkt_len_std", "pkt_len_max", "pkt_len_min", "pkt_len_mean", "pkt_len_std", "pkt_len_var",
        "fwd_header_len", "bwd_header_len", "fwd_seg_size_min", "fwd_act_data_pkts", "flow_iat_mean",
        "flow_iat_max", "flow_iat_min", "flow_iat_std", "fwd_iat_tot", "fwd_iat_max", "fwd_iat_min",
        "fwd_iat_mean", "fwd_iat_std", "bwd_iat_tot", "bwd_iat_max", "bwd_iat_min", "bwd_iat_mean",
        "bwd_iat_std", "fwd_psh_flags", "bwd_psh_flags", "fwd_urg_flags", "bwd_urg_flags", "fin_flag_cnt",
        "syn_flag_cnt", "rst_flag_cnt", "psh_flag_cnt", "ack_flag_cnt", "urg_flag_cnt", "ece_flag_cnt",
        "down_up_ratio", "pkt_size_avg", "init_fwd_win_byts", "init_bwd_win_byts", "active_max",
        "active_min", "active_mean", "active_std", "idle_max", "idle_min", "idle_mean", "idle_std",
        "fwd_byts_b_avg", "fwd_pkts_b_avg", "bwd_byts_b_avg", "bwd_pkts_b_avg", "fwd_blk_rate_avg",
        "bwd_blk_rate_avg", "fwd_seg_size_avg", "bwd_seg_size_avg", "cwe_flag_count", "subflow_fwd_pkts",
        "subflow_bwd_pkts", "subflow_fwd_byts", "subflow_bwd_byts", "label"]





ar2 = ["src_ip", "dst_ip", "src_port", "dst_port", "src_mac", "dst_mac", "protocol", "timestamp", 
        "flow_duration", "flow_byts_s", "flow_pkts_s", "fwd_pkts_s", "bwd_pkts_s", "tot_fwd_pkts",
        "tot_bwd_pkts", "totlen_fwd_pkts", "totlen_bwd_pkts", "fwd_pkt_len_max", "fwd_pkt_len_min",
        "fwd_pkt_len_mean", "fwd_pkt_len_std", "bwd_pkt_len_max", "bwd_pkt_len_min", "bwd_pkt_len_mean",
        "bwd_pkt_len_std", "pkt_len_max", "pkt_len_min", "pkt_len_mean", "pkt_len_std", "pkt_len_var",
        "fwd_header_len", "bwd_header_len", "fwd_seg_size_min", "fwd_act_data_pkts", "flow_iat_mean",
        "flow_iat_max", "flow_iat_min", "flow_iat_std", "fwd_iat_tot", "fwd_iat_max", "fwd_iat_min",
        "fwd_iat_mean", "fwd_iat_std", "bwd_iat_tot", "bwd_iat_max", "bwd_iat_min", "bwd_iat_mean",
        "bwd_iat_std", "fwd_psh_flags", "bwd_psh_flags", "fwd_urg_flags", "bwd_urg_flags", "fin_flag_cnt",
        "syn_flag_cnt", "rst_flag_cnt", "psh_flag_cnt", "ack_flag_cnt", "urg_flag_cnt", "ece_flag_cnt",
        "down_up_ratio", "pkt_size_avg", "init_fwd_win_byts", "init_bwd_win_byts", "active_max",
        "active_min", "active_mean", "active_std", "idle_max", "idle_min", "idle_mean", "idle_std",
        "fwd_byts_b_avg", "fwd_pkts_b_avg", "bwd_byts_b_avg", "bwd_pkts_b_avg", "fwd_blk_rate_avg",
        "bwd_blk_rate_avg", "fwd_seg_size_avg", "bwd_seg_size_avg", "cwe_flag_count", "subflow_fwd_pkts",
        "subflow_bwd_pkts", "subflow_fwd_byts", "subflow_bwd_byts", "label"]


dst_port	flow_duration	flow_byts_s	flow_pkts_s	fwd_pkts_s	bwd_pkts_s	tot_fwd_pkts	tot_bwd_pkts	totlen_fwd_pkts	totlen_bwd_pkts	fwd_pkt_len_max	fwd_pkt_len_min	fwd_pkt_len_mean	fwd_pkt_len_std	bwd_pkt_len_max	bwd_pkt_len_min	bwd_pkt_len_mean	bwd_pkt_len_std	pkt_len_max	pkt_len_min	pkt_len_mean	pkt_len_std	pkt_len_var	fwd_header_len	bwd_header_len	fwd_seg_size_min	fwd_act_data_pkts	flow_iat_mean	flow_iat_max	flow_iat_min	flow_iat_std	fwd_iat_tot	fwd_iat_max	fwd_iat_min	fwd_iat_mean	fwd_iat_std	bwd_iat_tot	bwd_iat_max	bwd_iat_min	bwd_iat_mean	bwd_iat_std	fwd_psh_flags	bwd_psh_flags	fwd_urg_flags	bwd_urg_flags	fin_flag_cnt	syn_flag_cnt	rst_flag_cnt	psh_flag_cnt	ack_flag_cnt	urg_flag_cnt	ece_flag_cnt	down_up_ratio	pkt_size_avg	init_fwd_win_byts	init_bwd_win_byts	active_max	active_min	active_mean	active_std	idle_max	idle_min	idle_mean	idle_std	fwd_byts_b_avg	fwd_pkts_b_avg	bwd_byts_b_avg	bwd_pkts_b_avg	fwd_blk_rate_avg	bwd_blk_rate_avg	fwd_seg_size_avg	bwd_seg_size_avg	cwe_flag_count	subflow_fwd_pkts	subflow_bwd_pkts	subflow_fwd_byts	subflow_bwd_byts	label


"""