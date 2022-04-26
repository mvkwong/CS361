import pandas as pd
from pandas.core.frame import DataFrame

class Recommender:
    def __init__(self, head_size, length, strung_weight, balance, bal_option) -> None:
        pref_head_size = float(head_size)
        pref_length = float(length)
        pref_strung_weight = float(strung_weight)
        if balance == "Head light":
            pref_balance = abs(float(bal_option))
        elif balance == "Head heavy":
            pref_balance = -abs(float(bal_option))
        else:
            pref_balance = 0
        self.pref_list = [pref_head_size, pref_length, pref_strung_weight, pref_balance]

    #Create racquet shortlist based on immutable specs (head size, length)
    def create_shortlist(self):
        column_names = ['Racquet', 'Head Size (in)', 'Length', 'Strung Weight (g)', 'Balance']
        df = pd.read_csv('cleaned_racquet_data.csv')
        rac_shortlist = df[column_names]
        #rac_shortlist = rac_shortlist[rac_shortlist['Head Size (in)'] == self.pref_list[0]]
        #rac_shortlist = rac_shortlist[rac_shortlist['Length'] == self.pref_list[1]].reset_index(drop=True)
        return rac_shortlist

    #Calc Euclidean distance score for each racquet by comparing each specification value against user pref
    def calc_scores(self, rac_shortlist):
        sim_score_list = []
        for i in range(len(rac_shortlist.index)):
            similarity_score = 0
            for j in range(1, len(rac_shortlist.columns)):
                similarity_score += (abs(self.pref_list[j-1] - rac_shortlist.loc[i, rac_shortlist.columns[j]]))**2
            similarity_score = similarity_score**0.5
            sim_score_list.append([similarity_score, rac_shortlist.loc[i, rac_shortlist.columns[0]]])
        sim_score_list.sort()
        return sim_score_list

    def get_recs(self):
        """print(f"The 5 racquets that are most similar to what you're looking for are: ")
        for i in range(min(5, len(score_list))):
            print(f"{i+1}. {score_list[i][1]}")"""
        shortlist = self.create_shortlist()
        score_list = self.calc_scores(shortlist)
        result = []
        for i in range(min(5, len(score_list))):
            result.append(score_list[i][1])
        return result

#user_pref = get_user_prefs()
#rac_shortlist = create_shortlist()
#score_list = calc_scores()
#get_recs()
